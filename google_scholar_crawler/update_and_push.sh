#!/bin/bash
# Fetch Google Scholar stats on this machine and publish them to the google-scholar-stats branch, then purge the
# jsDelivr cache so the homepage badge updates at once. Run daily by launchd (com.zhouyunsong.scholar-stats) from a
# copy in ~/Library/Application Support/scholar-stats (launchd may not read the external drive) — re-copy after edits;
# Scholar blocks GitHub's runners most days, which is why this runs locally.
set -euo pipefail
REPO="https://github.com/zhouyunsong/zhouyunsong.github.io.git"
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

cd "$WORK"
/usr/bin/python3 "$HERE/main.py"
cd results
git init -q
git add gs_data.json gs_data_shieldsio.json
git -c user.name="zhouyunsong" -c user.email="zhouyunsong@users.noreply.github.com" commit -q -m "Updated Citation Data"
git push -q --force "$REPO" HEAD:google-scholar-stats
for f in gs_data.json gs_data_shieldsio.json; do
  curl -s -o /dev/null "https://purge.jsdelivr.net/gh/zhouyunsong/zhouyunsong.github.io@google-scholar-stats/$f" || true
done
echo "$(date '+%F %T') pushed: $(cat gs_data_shieldsio.json)"
