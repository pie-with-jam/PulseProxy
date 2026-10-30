<p align="center">
  <a href="https://github.com/pie-with-jam/PulseProxy"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <img src="https://img.shields.io/github/last-commit/pie-with-jam/PulseProxy?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/pie-with-jam/PulseProxy?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/stars/pie-with-jam/PulseProxy?style=for-the-badge" alt="Stars">
</p>

<p align="center">
  <a href="./README.md">🇷🇺 Русский</a> · <b>🇬🇧 English</b> · <a href="./README.zh.md">🇨🇳 中文</a> · <a href="./README.fa.md">🇮🇷 فارسی</a>
</p>

> 📌 This is a translation of the canonical [Russian README](./README.md). Subscription links are identical and always up to date; client download links in this translation may be outdated — check the Russian README for the latest releases.

# 📖 About the Project

An automatically updated collection of public VPN configs (`V2Ray` / `VLESS` / `VMess` / `Trojan` / `Shadowsocks` / `Hysteria2` / `Tuic` / `Reality`) for getting around blocks, including configs for bypassing SNI/CIDR white lists and country lists for China and Iran.

Every config is a TXT subscription that can be imported into virtually any modern client (`v2rayNG`, `Throne`, `v2rayN`, `V2Box`, `Hiddify`, `Karing`, `Streisand`, etc.).

Configs are updated **automatically every ~30 minutes** (GitHub Actions + an external trigger), run a **liveness check** (healthcheck) and **structural validation**, so the links in the **"📋 Complete List of All Always-Current Configs"** section are always up to date.

## 📑 Table of Contents
- [🚀 Quick Start](#-quick-start)
- [📊 Config Status](#-config-status)
- [🔓 File #30 — SNI/CIDR White-list Bypass](#-file-30--snicidr-white-list-bypass)
- [🇨🇳🇮🇷 Files #31 and #32 — for China and Iran](#-files-31-and-32--for-china-and-iran)
- [⚙️ How It Works](#️-how-it-works)
- [🗂 Repository Structure](#-repository-structure)
- [🔧 Running the Generator Locally](#-running-the-generator-locally)
- [📋 Complete List of All Always-Current Configs](#-complete-list-of-all-always-current-configs)
- [📷 QR Codes](#-qr-codes)
- [🗂️ Client Guides](#️-client-guides)
- [📱 v2rayNG Routing for Android](#-v2rayng-routing-for-android)
- [⚠️ Troubleshooting](#️-troubleshooting)
- [⚠️ Disclaimer](#️-disclaimer)
- [🙏 Acknowledgements](#-acknowledgements)
- [📜 License](#-license)

---

## 🚀 Quick Start
1. Copy the link you need from the **"📋 Complete List of All Always-Current Configs"** section.
2. Import it into your **VPN client** (see the guides below).
3. Check the profile latency, pick the server with the lowest ping, and connect.

> 💡 **For mobile internet in Russia**, start with the file **[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** — a list filtered by SNI/CIDR white lists that has passed the liveness check.
>
> 💡 **For China** — the file **[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, **for Iran** — **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (no servers inside those countries).

---

## 📊 Config Status

> **⚠️ Warning!** This table shows the **sources** and the current number of configs. **Do not copy links from here!** The import links are in the **"📋 Complete List of All Always-Current Configs"** section below.

| № | File | Source | Configs |
|--|--|--|--|
| 1 | [`1.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt) | [sakha1370/OpenRay](https://github.com/sakha1370/OpenRay/raw/refs/heads/main/output/all_valid_proxies.txt) | 10 553 |
| 2 | [`2.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/2.txt) | [pie-with-jam/5ubscrpt10n-Reborn](https://raw.githubusercontent.com/pie-with-jam/5ubscrpt10n-Reborn/main/protocols/vl.txt) | 405 412 |
| 3 | [`3.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/3.txt) | [yitong2333/proxy-minging](https://raw.githubusercontent.com/yitong2333/proxy-minging/refs/heads/main/v2ray.txt) | 13 293 |
| 4 | [`4.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/4.txt) | [acymz/AutoVPN](https://raw.githubusercontent.com/acymz/AutoVPN/refs/heads/main/data/V2.txt) | 450 |
| 5 | [`5.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/5.txt) | [miladtahanian/V2RayCFGDumper](https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/main/sub.txt) | 389 |
| 6 | [`6.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt) | [roosterkid/openproxylist](https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt) | 148 |
| 7 | [`7.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/7.txt) | [Epodonios/v2ray-configs](https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt) | 556 |
| 8 | [`8.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/8.txt) | [ShatakVPN/ConfigForge-V2Ray](https://github.com/ShatakVPN/ConfigForge-V2Ray/raw/refs/heads/main/configs/vless.txt) | 277 |
| 9 | [`9.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/9.txt) | [mohamadfg-dev/telegram-v2ray-configs-collector](https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/refs/heads/main/category/vless.txt) | 290 |
| 10 | [`10.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/10.txt) | [mheidari98/.proxy](https://raw.githubusercontent.com/mheidari98/.proxy/refs/heads/main/vless) | 11 348 |
| 11 | [`11.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/11.txt) | [youfoundamin/V2rayCollector](https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt) | 603 |
| 12 | [`12.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/12.txt) | [VOID-Anonymity/V.O.I.D-VPN_Bypass](https://github.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/raw/refs/heads/main/url_work.txt) | 1 736 |
| 13 | [`13.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/13.txt) | [cbusifabcap/daily_free_vpn](https://github.com/cbusifabcap/daily_free_vpn/raw/refs/heads/main/Z.txt) | 3 528 |
| 14 | [`14.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/14.txt) | [LalatinaHub/Mineral](https://github.com/LalatinaHub/Mineral/raw/refs/heads/master/result/nodes) | 1 734 |
| 15 | [`15.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/15.txt) | [miladtahanian/Config-Collector](https://raw.githubusercontent.com/miladtahanian/Config-Collector/refs/heads/main/mixed_iran.txt) | 512 |
| 16 | [`16.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/16.txt) | [Pawdroid/Free-servers](https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub) | 9 |
| 17 | [`17.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/17.txt) | [MhdiTaheri/V2rayCollector_Py](https://github.com/MhdiTaheri/V2rayCollector_Py/raw/refs/heads/main/sub/Mix/mix.txt) | 1 904 |
| 18 | [`18.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/18.txt) | [free18/v2ray](https://raw.githubusercontent.com/free18/v2ray/refs/heads/main/v.txt) | 432 |
| 19 | [`19.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/19.txt) | [MhdiTaheri/V2rayCollector](https://github.com/MhdiTaheri/V2rayCollector/raw/refs/heads/main/sub/mix) | 1 830 |
| 20 | [`20.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/20.txt) | [Argh94/Proxy-List](https://github.com/Argh94/Proxy-List/raw/refs/heads/main/All_Config.txt) | 2 271 |
| 21 | [`21.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/21.txt) | [shabane/kamaji](https://raw.githubusercontent.com/shabane/kamaji/master/hub/merged.txt) | 48 877 |
| 22 | [`22.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt) | [wuqb2i4f/xray-config-toolkit](https://raw.githubusercontent.com/wuqb2i4f/xray-config-toolkit/main/output/base64/mix-uri) | 711 |
| 23 | [`23.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt) | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia/raw/refs/heads/main/BLACK_VLESS_RUS.txt) | 313 |
| 24 | [`24.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt) | [Mr-Meshky/vify](https://github.com/Mr-Meshky/vify/raw/refs/heads/main/configs/vless.txt) | 774 |
| 25 | [`25.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt) | [V2RayRoot/V2RayConfig](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/refs/heads/main/Config/vless.txt) | 258 |
| 26 | [`26.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/26.txt) | [flaafix/AetrisVPN-black-list](https://raw.githubusercontent.com/flaafix/AetrisVPN-black-list/refs/heads/main/configs.txt) | 104 |
| 27 | [`27.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/27.txt) | [slxkware/Vless-list](https://raw.githubusercontent.com/slxkware/Vless-list/refs/heads/main/Black%20Vless.txt) | 27 |
| 28 | [`28.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/28.txt) | [FLAT447/v2ray-lists](https://raw.githubusercontent.com/FLAT447/v2ray-lists/refs/heads/main/BLACK_FULL.txt) | 76 |
| 29 | [`29.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/29.txt) | [aviamastersgh/vpn-free-russia](https://raw.githubusercontent.com/aviamastersgh/vpn-free-russia/refs/heads/main/all_configs.txt) | 9 137 |
| 30 | [`30.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt) | **Special file: SNI/CIDR white-list bypass** (sources 1–29 + `30_urls.json` + `storage.json`, healthcheck) | 1 094 |
| 31 | [`31.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt) | **For China** (no servers inside CN per `cn_cidr.txt`, healthcheck) | 977 |
| 32 | [`32.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt) | **For Iran** (no servers inside IR per `ir_cidr.txt`, healthcheck) | 945 |

> Config counts are given as of **13.10.2026** and are refreshed with every build cycle.

---

## 🔓 File #30 — SNI/CIDR White-list Bypass

**[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** — a separate special file for working through white lists (mobile internet, "unattended mode"):

- candidates are gathered from files **1–29** plus the extra source list **`30_urls.json`** (ready-made bypass subscriptions);
- configs that don't pass the **CIDR/SNI white lists** (`cidrwhitelist.txt`, `sni_domains.json`) are filtered out;
- every config goes through **structural validation**: glued-together links `&amp;` → `&` are repaired, broken URLs are dropped (invalid UUID, reality without `pbk`, corrupted Base64, etc.);
- a **healthcheck** liveness check runs (one TCP/TLS connection per config);
- a merge with **`storage.json`** — your own personally verified configs.

> If configs from the regular files (1–29) don't pass the white lists, use **30.txt**.

### 🪞 Russian Mirrors / Bypasses for Subscription #30 (unattended mode)

If the `raw.githubusercontent.com` link itself won't open (white-list / unattended mode), use the **Yandex.Translate proxy links** to update subscription #30 in your client:

1. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fraw.githack.com%2Fpie-with-jam%2FPulseProxy%2Frefs%2Fheads%2Fmain%2Fgithubmirror%2F30.txt&lang=de-de`
2. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpie-with-jam%2FPulseProxy%40main%2Fgithubmirror%2F30.txt&lang=de-de`

> ✦ These links reproduce the contents of `30.txt` exactly and are updated along with it — paste one of them into the subscription URL field instead of the regular link.
>
> ✦ Only the **Yandex +** (`raw.githack.com` / `cdn.jsdelivr.net`) pairing works; other pairings with Yandex may break configurations.
>
> ✦ If the first link doesn't open, try the second (and vice versa). After updating in the client, reconnect.

---

## 🇨🇳🇮🇷 Files #31 and #32 — for China and Iran

**[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)** and **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — country-specific subscriptions for users behind national firewalls (China, Iran):

- candidates are gathered from files **1–29** and `storage.json` (deduplication, structural validation);
- **servers inside the country are excluded**: configs with IPs from `cn_cidr.txt` / `ir_cidr.txt` (8 802 / 1 901 subnets) are filtered out statically, and domains are checked against the connection's real IP during the healthcheck — connecting to a server in your own country to bypass that same country's blocks is pointless; **Hong Kong, Macau and Taiwan** (`hk_cidr.txt` / `mo_cidr.txt` / `tw_cidr.txt`) are exempted from the exclusion: they sit outside the GFW and remain useful nearby exits;
- a **healthcheck** liveness check runs (TCP/TLS handshake) on an evenly sampled batch of up to 4 000 candidates per file (the full 1–29 pool is too large to test entirely; the limit is configurable via `COUNTRY_PROBE_LIMIT`).

> ⚠️ **Important:** liveness is checked **from GitHub Actions servers, not from China/Iran** — the GFW / the Iranian filter may block some configs that work fine everywhere else. The file is a filtered candidate list, not a guarantee of availability inside the country; if something is unreachable, try the next servers in the list.

> 🔒 **Don't forget DoH (DNS over HTTPS):** the GFW and the Iranian filter poison plain DNS. Switch Remote DNS to `https://dns.google/dns-query` (Google) or `https://cloudflare-dns.com/dns-query` (Cloudflare) — otherwise domains get spoofed even before you connect to the proxy.

> 💡 These files are also recommended for users from these countries in the v2rayNG routing section below.

---

## ⚙️ How It Works
1. **GitHub Actions** (`.github/workflows/auto_update.yml`) runs the build **on a schedule every ~30 minutes** (`:07` and `:37` past every hour UTC), plus an external trigger from a server pokes the workflow at `:25` and `:55`. There's also a manual run (`manual_update.yml`).
2. The script downloads configs from **29 public sources** (`urls.json`) in parallel, using ETag/If-Modified-Since (re-downloads without changes don't waste traffic).
3. Each config is filtered: Base64 is decoded, protocol presence is checked (`vmess://`, `vless://`, `trojan://`, `ss://`, `hysteria2://`, `tuic://`, etc.), insecure configs (`allowInsecure=1`) are removed, duplicates are deduplicated.
4. **File #30** is built separately: candidates gathered from 1–29 + `30_urls.json` → CIDR/SNI white-list filter → structural validation → healthcheck → merge with `storage.json`.
5. **Files #31 (China) and #32 (Iran)** are built from 1–29 + `storage.json` → in-country servers excluded by CIDR (`cn_cidr.txt` / `ir_cidr.txt`) → validation → healthcheck (sample of up to 4 000 candidates).
6. **QR codes** are generated (`qr-codes/1.png` … `32.png`) — they encode the subscription URL.
7. All changes are committed and pushed to the repository — the links in the README are always up to date.

## 🗂 Repository Structure
```text
.github/workflows/   — GitHub Actions CI/CD
 ├─ auto_update.yml     — auto-update every ~30 min on schedule (+ workflow_dispatch)
 └─ manual_update.yml   — manual build run
githubmirror/        — generated .txt subscriptions (32 files)
qr-codes/            — QR codes of the subscriptions for import (32 PNG)
source/              — source code and generator configuration
 ├─ main.py             — main generation script
 ├─ requirements.txt    — Python dependencies
 ├─ config/
 │   ├─ urls.json           — 29 public sources (files 1–29)
 │   ├─ 30_urls.json        — white-list sources for special file #30
 │   ├─ storage.json        — personal verified configs (merged into 30.txt)
 │   ├─ cidrwhitelist.txt   — CIDR white list (block bypass)
 │   ├─ cn_cidr.txt         — China CIDR networks (for file #31)
 │   ├─ hk_cidr.txt         — Hong Kong CIDR networks (exempt from #31)
 │   ├─ mo_cidr.txt         — Macau CIDR networks (exempt from #31)
 │   ├─ tw_cidr.txt         — Taiwan CIDR networks (exempt from #31)
 │   ├─ ir_cidr.txt         — Iran CIDR networks (for file #32)
 │   └─ sni_domains.json    — SNI domain white list
 └─ src/
     ├─ __init__.py
     ├─ config.py           — paths and configuration loading
     ├─ file_manager.py     — downloading, filtering, white lists, file assembly
     ├─ validator.py        — structural validation of configs
     ├─ healthcheck.py      — liveness check (TCP/TLS)
     ├─ cidr.py             — working with CIDR lists
     ├─ parser.py           — filtering of insecure configs
     ├─ network.py          — HTTP session with retry/ETag
     ├─ qr_generator.py     — QR code generation
     ├─ git_ops.py          — commit and push of changes
     ├─ github_api.py       — GitHub API
     ├─ readme_updater.py   — automatic README updates
     ├─ release_fetcher.py  — up-to-date client download links
     ├─ logger.py           — logging
     └─ github_api.py       — repository statistics
 LICENSE               — GPL-3.0 license
 README.md             — this file (Russian)
 README.en.md          — English translation
 README.zh.md          — Simplified Chinese translation
 README.fa.md          — Persian translation (فارسی)
```

---

## 🔧 Running the Generator Locally

```bash
git clone https://github.com/pie-with-jam/PulseProxy.git
cd PulseProxy/source
python -m pip install -r requirements.txt
export MY_TOKEN=<GITHUB_TOKEN>   # a PAT with contents:write rights so changes can be pushed
python main.py                   # configs will appear in ../githubmirror
```

> **Important!** Without `MY_TOKEN` the generator still runs, but committing/pushing changes will not happen.

---

# 📋 Complete List of All Always-Current Configs

> Recommended lists: **[1](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt)**, **[6](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt)**, **[22](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt)**, **[23](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt)**, **[24](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt)** and **[25](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt)**.

> SNI/CIDR white-list bypass: **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**.

> For China: **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, for Iran: **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — no servers inside those countries.

 1) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt`
 2) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/2.txt`
 3) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/3.txt`
 4) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/4.txt`
 5) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/5.txt`
 6) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt`
 7) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/7.txt`
 8) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/8.txt`
 9) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/9.txt`
 10) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/10.txt`
 11) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/11.txt`
 12) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/12.txt`
 13) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/13.txt`
 14) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/14.txt`
 15) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/15.txt`
 16) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/16.txt`
 17) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/17.txt`
 18) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/18.txt`
 19) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/19.txt`
 20) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/20.txt`
 21) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/21.txt`
 22) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt`
 23) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt`
 24) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt`
 25) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt`
 26) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/26.txt`
 27) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/27.txt`
 28) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/28.txt`
 29) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/29.txt`
 30) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt`
 31) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt`
 32) `https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt`

> 🔗 [Link to the QR codes of the always-current configs](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes)

---

# 📷 QR Codes

The QR codes for all subscriptions live in the [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) folder — `1.png` … `32.png`. A QR encodes the **subscription link**, so it's handy for importing into mobile clients and Android TV (where pasting a link as text is awkward).

---

# 🗂️ Client Guides

<details>

<summary>📱 Android Guide (v2rayNG)</summary>

**1.** Download **"v2rayNG"** — [Latest release](https://github.com/2dust/v2rayNG/releases) (APK `arm64-v8a`).

**2.** Copy the link you need from the **"📋 Complete List of All Always-Current Configs"** section to the clipboard.

**3.** Open the **"v2rayNG"** app and tap ➕ in the top-right corner, then choose **"Import from clipboard"**.

**4.** Tap the **"three dots"** in the top right → **"Check profile latency"**; when it finishes, press **"Sort by test results"** in that same menu.

**5.** Pick the server you need and hit the ▶️ button in the bottom-right corner.

**Updating configs:** the **"three lines"** menu top left → **"Groups"** → the **"circle with an arrow"** icon top right → wait for the update to finish.

> 🧭 **Tip:** set up **routing** (traffic for Iran/China/Russia goes **direct**, everything else through the proxy) and turn off **mux** and **fragmentation** — see the [“📱 v2rayNG Routing for Android”](#-v2rayng-routing-for-android) section.

</details>

<details>

<summary>📺 Android TV Guide</summary>

**1.** Download **"v2rayNG"** — [Latest release](https://github.com/2dust/v2rayNG/releases) (APK `armeabi-v7a`).

**2.** Download the **QR code** you need from the [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) folder.

**3.** Open **"v2rayNG"** → ➕ → **"Import from QR code"** → pick the image (the photo icon top right).

**4.** "Three dots" → **"Check profile latency"** → **"Sort by test results"**.

**5.** Pick a server and hit ▶️.

</details>

<details>

<summary>🖥 Windows / Linux Guide (Throne)</summary>

**1.** Download **"Throne"** — [Latest release](https://github.com/throneproj/Throne/releases) (`windows64` / `windowslegacy64` / `linux-amd64`).

**2.** Copy the link you need from the **"📋 Complete List..."** section to the clipboard.

**3.** **"Profiles"** → **"Add profile from clipboard"**.

**4.** Select all configs with **Ctrl+A**, then **"Profiles"** → **"Latency (ping) test of the selected profile"** and wait for it to finish (the Logs will show "Latency (ping) test finished!").

**5.** Click the **"Latency (ping)"** column — it sorts.

**6.** At the top of the window, enable **"TUN mode"** (checkbox).

**7.** Pick the config with the lowest ping → **left-click** → **"Start"**.

**Updating configs:** "Settings" → "Groups" → **"Update all subscriptions"**.

</details>

<details>

<summary>☎ iOS / iPadOS Guide (V2Box)</summary>

**1.** Download **"V2Box - V2ray Client"** — [App Store](https://apps.apple.com/ru/app/v2box-v2ray-client/id6446814690).

**2.** Copy the link you need from the **"📋 Complete List..."** section to the clipboard.

**3.** In the app, go to the **"Config"** tab → the plus sign top right → **"Add subscription"** → enter a name and paste the link into the **"URL"** field.

**4.** Wait for the check to finish, then select a config by tapping its name.

**5.** Tap **"Connect"** in the bottom bar.

**Updating configs:** the "Config" tab → the refresh icon to the left of the group name.

</details>

<details>

<summary>💻 MacOS Guide (Hiddify)</summary>

**1.** Download **"Hiddify"** — [Latest release](https://github.com/hiddify/hiddify-app/releases) (`Hiddify-MacOS.dmg`).

**2.** Click **"New profile"** → **"Add from clipboard"** (copy the link from the **"📋 Complete List..."** section).

**3.** **"Settings"** → **"Routing option"** → pick the matching region.

**4.** The settings icon top left → **"VPN service"** → enable **"VPN"** (the icon in the center).

**5.** To switch servers: the **"Proxy"** tab.

**Updating configs:** select the profile → the refresh icon to the left of its name.

</details>

---

# 📱 v2rayNG Routing for Android

For Android we recommend **[v2rayNG](https://github.com/2dust/v2rayNG/releases)** combined with **routing rules**: local (Iranian, Chinese, Russian) and "your own" traffic goes **direct**, while only what actually needs bypassing goes through the proxy. That's more stable, faster, and easier on the proxy.

### 🧭 Ready-Made Routing File

**[`routing/v2rayng-routing.json`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/routing/v2rayng-routing.json)** — rules to import into v2rayNG (first match wins):

- **Direct (direct):**
  - the local network (LAN);
  - **Iran** (`geoip:ir` plus the `domain:ir` suffix), **China** (`geoip:cn` / `geosite:cn`), **Russia** (`geoip:ru` plus the `domain:ru` / `domain:su` suffixes);
  - Chinese and Russian public DNS (AliDNS, DNSPod, Yandex, SafeDNS);
  - IP-lookup and DNS-leak services — **ipify.org, 2ip.io, icanhazip.com, ifconfig.me, ipleak.net, dnsleaktest.com**, etc. (so you can see your **real** IP);
  - app stores — **F-Droid, Huawei, Xiaomi**, Samsung, Amazon (huge downloads don't get pushed through the proxy).
- **Block:** QUIC (`UDP 443`) — traffic is forced into TCP, which helps bypass DPI (common in Iran/Russia).
- **Everything else → through the proxy** (the default behavior — nothing extra to configure).

**Import:** copy the JSON contents → in v2rayNG open the "three lines" menu on the left → **"Settings"** → **"Routing"** → **"⋮"** → **"Import from clipboard"**. Rule order matters — don't shuffle or delete the `geoip:private` block.

> ✅ **Stable on stable v2rayNG releases:** the file only uses categories that actually exist in the standard `geosite.dat` (`geosite:private`, `geosite:cn`) plus the TLD suffixes `domain:ir` / `domain:ru`. The `geosite:ir` and `geosite:ru` categories do **not** exist in the standard `geosite.dat` — any rule referencing them breaks the config with `code not found in geosite.dat: IR`. If you see this error after importing third-party or older rules — delete the `geosite:ir` / `geosite:ru` rules or re-import our file (updating geo files won't help — these categories are absent from every standard build).

> ⚠️ **Important: turn ALL routing rules ON (`enabled: true`), no matter where you live.** Don't switch off the rules "for other" countries — they don't get in the way, they just keep only the needed traffic off the proxy (for example, you can live in Russia but leave the Iran/China rules enabled).

### ⚙️ Recommended Client Settings

- **Subscription:** from **China** — file **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, from **Iran** — file **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (no servers inside those countries); from Russia, start with file **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**.
- **Mux** — **off** (Settings → Mux → disable). Mux often breaks TLS and websites.
- **Fragmentation (fragment)** — **off**. Turn it on selectively, only when a specific site is being cut by SNI.
- **Remote DNS:** for white lists (file **30**) — your provider's DNS or Yandex; for the regular mode — DoH: `https://dns.google/dns-query` (Google) or `https://cloudflare-dns.com/dns-query` (Cloudflare).
- **Domain strategy** ("Settings" → "Routing" → "Domain Strategy") — **`IPIfNonMatch`**: domain rules match instantly, while `geoip` rules are checked only for domains that matched no rule at all. Don't leave `AsIs` (the default) — with it `geoip:ir` / `geoip:cn` / `geoip:ru` never match domains and local traffic goes through the proxy; `IPOnDemand` resolves every connection needlessly. Note: `IPIfNonMatch` resolves the unmatched domains, so your Remote DNS must be DoH (see above).

---

# ⚠️ Troubleshooting

<details>

<summary>⚠ "Check profile latency" hangs in v2rayNG (the check gets to N and then "hangs")</summary>

There are plenty of public configs (sometimes thousands), and running a real connection test on every one takes a very long time.

**1.** Update **v2rayNG** to the latest version — [Releases](https://github.com/2dust/v2rayNG/releases).

**2.** In the check menu, switch the test type from **REALITY/HTTP** to **TCP ping** — TCP ping is checked instantly, so configs don't "hang".

**3.** Or don't wait for the full check: import the subscription, wait for the configs to show up, and connect to the one you need — the check is optional.

</details>

<details>

<summary>⚠ No configs appear after adding a subscription in v2rayNG</summary>

**1.** Tap the **"three lines"** in the top-left corner.

**2.** Open **"Groups"**.

**3.** Tap the **"circle with an arrow"** top right and wait for the update to finish.

</details>

<details>

<summary>⚠ No internet when connecting to the VPN</summary>

**1.** Try another config from the subscription (toggle the VPN off and on, or pick a server with a lower ping).

**2.** If the ping succeeds but there's no traffic, change the **Remote DNS** in the client to DoH, e.g. `https://dns.google/dns-query` (Google) or `https://cloudflare-dns.com/dns-query` (Cloudflare) (in v2rayNG: "Settings" → "DNS Settings" → "Basic DNS Settings").

**3.** For white lists (file 30), use your provider's DNS (or Yandex) — foreign DNS doesn't work in white-list mode.

</details>

<details>

<summary>⚠ Errors "net/http: 12x handshake timeout" and "io: read/write closed pipe"</summary>

**1.** On the home screen, long-press the **"v2rayNG"** icon → **"About"**.

**2.** Tap **"Stop"** and start the app again.

**3.** Update the subscription (Groups → ⟳) and connect again.

</details>

<details>

<summary>⚠ MSVCP/VCRUNTIME error in Throne on Windows</summary>

**1.** **Win+R** → `control` → **"Programs and Features"**.

**2.** In the search box on the right, type **"Visual"** and remove every **"Microsoft Visual C++"** component.

**3.** Download and unpack the **Visual C++ Runtimes All-in-One** build.

**4.** Run `install_bat.all` **as administrator** and wait for the installation to finish.

</details>

---

# ⚠️ Disclaimer

**By using this repository and its configurations, you take full responsibility for applying them.**

- The author **bears no responsibility** for any consequences of using the published configurations: this covers functionality, security, and any possible restrictions from your provider or other organizations.
- All configurations are partly **public** — they are posted and updated by third parties; the project's author only collects, filters, and publishes them in a convenient form, without guaranteeing their content, availability, or uninterrupted operation.
- The project is **non-commercial and provided "as is"** (`as is`): no warranties are given, and no responsibility is taken for any losses, outages, blocks, or other consequences.
- You must assess the risks yourself and comply with the laws of your country.

---

# 🙏 Acknowledgements

The core idea, structure, and source code of this project were taken from **[AvenCores / goida-vpn-configs](https://gitlab.com/avencores/goida-vpn-configs)** — a huge **thank you to the author, AvenCores**, for the work they put in! ❤️

Thanks also to the maintainer of [LalatinaHub/Mineral](https://github.com/LalatinaHub/Mineral) (source #14 in the table): they replied to our [issue #6](https://github.com/LalatinaHub/Mineral/issues/6) about the broken scheduled workflow the very next day and fixed pushes to main.

PulseProxy is a fork with improvements: healthcheck, structural config validation, special file #30 with SNI/CIDR white lists, the author's own configs (`storage.json`), and updates every ~30 minutes via GitHub Actions.

---

# 📜 License

The project is distributed under the **GPL-3.0** license. The full license text is in the [`LICENSE`](LICENSE) file.

---

<!-- 💰 Support the author -->

If you found the project useful, you can support its development:

| Network / Coin | Transfer Address | QR Code |
| :--- | :--- | :---: |
| **GRAM (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="GRAM TON QR"> |
| **USDT (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="USDT TON QR"> |
| **BTC (BitCoin network)** | `bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz" width="130" height="130" alt="BTC QR"> |
| **ETH (Etherium)** | `0xF162fb13798A7B177d9d7fB0C923779c1bFD0258` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=0xF162fb13798A7B177d9d7fB0C923779c1bFD0258" width="130" height="130" alt="ETH QR"> |

> ⚠️ **Warning:** only send coins **in the specified networks** — GRAM/USDT on the **TON** network, BTC on the **BitCoin** network, ETH on the **Etherium** network.
