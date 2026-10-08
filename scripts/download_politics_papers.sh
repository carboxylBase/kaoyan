#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out_dir="$root/resources/raw_papers/politics"
mkdir -p "$out_dir"

download() {
  local year="$1"
  local url="$2"
  curl -L --fail --retry 3 --connect-timeout 20 --max-time 180 \
    -A "Mozilla/5.0" \
    "$url" \
    -o "$out_dir/${year}_politics.pdf"
}

download 2014 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/80fce00922d3521e.pdf"
download 2015 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fd8d31fce1370441.pdf"
download 2016 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/52bc1b34ce1420ac.pdf"
download 2017 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/ef7e656229b14ffe.pdf"
download 2018 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/aa722ead55dc4dbc.pdf"
download 2019 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fe440afcb892077f.pdf"
download 2020 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fb8a3633a8df34d0.pdf"
download 2021 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/12a2177b1eec778a.pdf"
download 2022 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/dba47a0f0e542aa0.pdf"
download 2023 "https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/148ebcad6cdfd251.pdf"
