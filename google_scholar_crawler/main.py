"""Fetch Google Scholar stats for the homepage badge and per-paper citation counts.

Reads the public profile page directly (standard library only — the `scholarly` package kept getting blocked from
GitHub Actions). Writes results/gs_data.json (citedby, hindex, i10index, publications{author_pub_id: num_citations})
and results/gs_data_shieldsio.json. Exits non-zero, writing nothing, if the page is blocked or cannot be parsed, so a
failed run never overwrites good data.
"""
import html
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")
SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "bTsmnwcAAAAJ")


def get(url, tries=3):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
            page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
            if "gsc_rsb_std" in page or "gsc_a_tr" in page:
                return page
            print(f"attempt {k + 1}: no profile data in response (blocked / captcha?)", file=sys.stderr)
        except Exception as e:                      # network errors, 429s
            print(f"attempt {k + 1}: {e}", file=sys.stderr)
        time.sleep(10 * (k + 1))
    sys.exit("Google Scholar profile could not be fetched; keeping the previous data")


def main():
    base = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
    first = get(base + "&cstart=0&pagesize=100")
    stats = [int(x) for x in re.findall(r'class="gsc_rsb_std">(\d+)<', first)]
    if len(stats) < 6:
        sys.exit("Could not parse the citation table; keeping the previous data")
    name = html.unescape(re.search(r'id="gsc_prf_in">([^<]+)<', first).group(1))

    publications, page, start = {}, first, 0
    while True:
        rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S)
        for row in rows:
            pid = re.search(r'citation_for_view=([\w-]+:[\w-]+)', row)
            if not pid:
                continue
            title = re.search(r'class="gsc_a_at">([^<]*)<', row)
            cites = re.search(r'class="gsc_a_ac gs_ibl"[^>]*>(\d*)<', row)
            publications[pid.group(1)] = {
                "author_pub_id": pid.group(1),
                "title": html.unescape(title.group(1)) if title else "",
                "num_citations": int(cites.group(1)) if cites and cites.group(1) else 0,
            }
        if len(rows) < 100:
            break
        start += 100
        time.sleep(3)
        page = get(base + f"&cstart={start}&pagesize=100")

    author = {
        "scholar_id": SCHOLAR_ID, "name": name, "updated": str(datetime.now()),
        "citedby": stats[0], "citedby5y": stats[1], "hindex": stats[2], "hindex5y": stats[3],
        "i10index": stats[4], "i10index5y": stats[5], "publications": publications,
    }
    print(json.dumps({k: v for k, v in author.items() if k != "publications"}, indent=2), f"\n{len(publications)} publications")
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as f:
        json.dump(author, f, ensure_ascii=False)
    with open("results/gs_data_shieldsio.json", "w") as f:
        json.dump({"schemaVersion": 1, "label": "citations", "message": f"{author['citedby']}"}, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
