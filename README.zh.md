<p align="center">
  <a href="https://github.com/pie-with-jam/PulseProxy"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <img src="https://img.shields.io/github/last-commit/pie-with-jam/PulseProxy?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/pie-with-jam/PulseProxy?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/stars/pie-with-jam/PulseProxy?style=for-the-badge" alt="Stars">
</p>

<p align="center">
  <a href="./README.md">🇷🇺 Русский</a> · <a href="./README.en.md">🇬🇧 English</a> · <b>🇨🇳 中文</b> · <a href="./README.fa.md">🇮🇷 فارسی</a>
</p>

> 📌 本文是[俄语 README](./README.md)（canonical 源文件）的翻译。订阅链接与原文完全一致且始终最新；本译文中的客户端下载链接可能已过时——最新版本请参阅俄语 README。

# 📖 项目简介

一个自动更新的公共 VPN 配置集合（`V2Ray` / `VLESS` / `VMess` / `Trojan` / `Shadowsocks` / `Hysteria2` / `Tuic` / `Reality`），用于绕过封锁，其中还包括用于绕过 SNI/CIDR 白名单的配置，以及面向中国和伊朗的国别列表。

每个配置都是一条 TXT 订阅，几乎可以导入任何现代客户端（`v2rayNG`、`Throne`、`v2rayN`、`V2Box`、`Hiddify`、`Karing`、`Streisand` 等）。

配置**每约 30 分钟自动更新**（GitHub Actions + 外部触发器），并且会通过**健康检查（healthcheck）**和**结构校验**，因此 **「📋 所有永久有效配置的总列表」** 一节中的链接始终有效。

## 📑 目录
- [🚀 快速开始](#-快速开始)
- [📊 配置状态](#-配置状态)
- [🔓 文件 №30 — 绕过 SNI/CIDR 白名单](#-文件-30--绕过-snicidr-白名单)
- [🇨🇳🇮🇷 文件 №31 与 №32 — 中国与伊朗专用](#-文件-31-与-32--中国与伊朗专用)
- [⚙️ 工作原理](#️-工作原理)
- [🗂 仓库结构](#-仓库结构)
- [🔧 本地运行生成器](#-本地运行生成器)
- [📋 所有永久有效配置的总列表](#-所有永久有效配置的总列表)
- [📷 QR 码](#-qr-码)
- [🗂️ 客户端指南](#️-客户端指南)
- [📱 Android 版 v2rayNG 路由规则](#-android-版-v2rayng-路由规则)
- [⚠️ 常见问题排查](#️-常见问题排查)
- [⚠️ 免责声明](#️-免责声明)
- [🙏 致谢](#-致谢)
- [📜 许可证](#-许可证)

---

## 🚀 快速开始
1. 从 **「📋 所有永久有效配置的总列表」** 一节复制需要的链接。
2. 将其导入你的 **VPN 客户端**（参见下文的指南）。
3. 测量配置的延迟，选择 ping 最低的服务器并连接。

> 💡 **在俄罗斯使用移动网络时**，请先从文件 **[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** 开始 —— 这是按 SNI/CIDR 白名单筛选并通过存活检查的列表。
>
> 💡 **中国**用文件 **[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**，**伊朗**用 **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)**（不含这两个国家境内的服务器）。

---

## 📊 配置状态

> **⚠️ 注意！** 本表展示的是**来源**和当前的配置数量。**不要从这里复制链接！** 用于导入的链接在下方的 **「📋 所有永久有效配置的总列表」** 一节。

| 编号 | 文件 | 来源 | 配置数 |
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
| 30 | [`30.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt) | **特殊文件：绕过 SNI/CIDR 白名单**（来源 1–29 + `30_urls.json` + `storage.json`，健康检查） | 1 094 |
| 31 | [`31.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt) | **中国专用**（按 `cn_cidr.txt` 排除中国境内的服务器，健康检查） | 977 |
| 32 | [`32.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt) | **伊朗专用**（按 `ir_cidr.txt` 排除伊朗境内的服务器，健康检查） | 945 |

> 配置数量统计截至 **13.10.2026**，并在每次构建循环时更新。

---

## 🔓 文件 №30 — 绕过 SNI/CIDR 白名单

**[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** —— 一个用于白名单环境的独立特殊文件（移动网络、无人值守模式）：

- 候选配置收集自文件 **1–29** 以及 **`30_urls.json`** 列表中的额外来源（现成的绕行订阅）；
- 过滤掉不符合 **CIDR/SNI 白名单**（`cidrwhitelist.txt`、`sni_domains.json`）的配置；
- 每个配置都要经过**结构校验**：修复粘连的 `&amp;` → `&` 链接，丢弃损坏的 URL（无效的 UUID、缺少 `pbk` 的 reality、损坏的 Base64 等）；
- 进行**健康检查**存活验证（每个配置建立一次 TCP/TLS 连接）；
- 与 **`storage.json`** —— 个人已验证的配置 —— 合并。

> 如果普通文件（1–29）中的配置通不过白名单，请改用 **30.txt**。

### 🪞 俄罗斯镜像 / 订阅 №30 的绕行方式（无人值守模式）

如果 `raw.githubusercontent.com` 链接本身打不开（白名单模式 / 无人值守模式），请使用 **Yandex 翻译代理链接** 在客户端中更新订阅 №30：

1. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fraw.githack.com%2Fpie-with-jam%2FPulseProxy%2Frefs%2Fheads%2Fmain%2Fgithubmirror%2F30.txt&lang=de-de`
2. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpie-with-jam%2FPulseProxy%40main%2Fgithubmirror%2F30.txt&lang=de-de`

> ✦ 这些链接的内容与 `30.txt` 完全一致，并与之同步更新 —— 请把其中一条粘贴到订阅 URL 字段中，替代普通链接。
>
> ✦ 有效的正是 **Yandex +**（`raw.githack.com` / `cdn.jsdelivr.net`）这一组合；其他与 Yandex 的组合可能会破坏配置。
>
> ✦ 如果第一条链接打不开，请尝试第二条（反之亦然）。在客户端更新之后请重新连接。

---

## 🇨🇳🇮🇷 文件 №31 与 №32 — 中国与伊朗专用

**[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)** 和 **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** —— 面对国家级防火墙的用户（中国、伊朗）的国别订阅：

- 候选配置收集自文件 **1–29** 和 `storage.json`（去重、结构校验）；
- **排除本国境内的服务器**：IP 来自 `cn_cidr.txt` / `ir_cidr.txt`（8 802 / 1 901 个子网）的配置会被静态过滤，域名则在健康检查时根据连接的真实 IP 校验 —— 连接自己国家境内的服务器去绕过本国的封锁毫无意义；**香港、澳门和台湾**（`hk_cidr.txt` / `mo_cidr.txt` / `tw_cidr.txt`）不计入境内排除：它们位于 GFW 之外，仍然是有用的就近出口；
- 进行**健康检查**（TCP/TLS 握手），每个文件最多均匀抽取 4 000 个候选（1–29 的完整池太大，无法全部检查；可通过 `COUNTRY_PROBE_LIMIT` 调整上限）。

> ⚠️ **重要：** 存活检查是在 **GitHub Actions 的服务器上执行的，而不是在中国/伊朗境内** —— 防火长城（GFW）/伊朗过滤器可能会屏蔽一部分在别处正常可用的配置。文件提供的是经过筛选的候选，而不是境内可用性的保证；如果无法连接，请尝试列表中的下一个服务器。

> 🔒 **别忘了 DoH（DNS over HTTPS）：** GFW 和伊朗过滤器会污染普通 DNS。请把 Remote DNS 切换为 `https://dns.google/dns-query`（Google）或 `https://cloudflare-dns.com/dns-query`（Cloudflare）—— 否则域名在连接代理之前就会被篡改。

> 💡 在下文的 v2rayNG 路由一节中，这两个文件同样推荐给来自这些国家的用户。

---

## ⚙️ 工作原理
1. **GitHub Actions**（`.github/workflows/auto_update.yml`）**按计划每约 30 分钟**触发一次构建（UTC 每小时的 `:07` 和 `:37`），另外外部服务器上的触发器会在 `:25` 和 `:55` 调用该 workflow。也支持手动触发（`manual_update.yml`）。
2. 脚本并行下载 **29 个公共来源**（`urls.json`）的配置，使用 ETag/If-Modified-Since（内容无变化的重复下载不会消耗流量）。
3. 每个配置都会被过滤：解码 Base64、检查协议是否存在（`vmess://`、`vless://`、`trojan://`、`ss://`、`hysteria2://`、`tuic://` 等）、删除不安全的配置（`allowInsecure=1`）、去重。
4. **文件 №30** 单独生成：从 1–29 + `30_urls.json` 收集候选 → 按 CIDR/SNI 白名单过滤 → 结构校验 → 健康检查 → 与 `storage.json` 合并。
5. **文件 №31（中国）和 №32（伊朗）** 由 1–29 + `storage.json` 生成 → 按 CIDR（`cn_cidr.txt` / `ir_cidr.txt`）排除境内服务器 → 校验 → 健康检查（最多抽取 4 000 个候选）。
6. 生成 **QR 码**（`qr-codes/1.png` … `32.png`）—— 编码订阅 URL。
7. 所有变更都会提交并推送到仓库 —— README 中的链接始终是最新的。

## 🗂 仓库结构
```text
.github/workflows/   — GitHub Actions CI/CD
 ├─ auto_update.yml     — 按计划每约 30 分钟自动更新（+ workflow_dispatch）
 └─ manual_update.yml   — 手动触发构建
githubmirror/        — 生成的 .txt 订阅（32 个文件）
qr-codes/            — 用于导入的订阅 QR 码（32 张 PNG）
source/              — 生成器的源代码与配置
 ├─ main.py             — 主生成脚本
 ├─ requirements.txt    — Python 依赖
 ├─ config/
 │   ├─ urls.json           — 29 个公共来源（文件 1–29）
 │   ├─ 30_urls.json        — 特殊文件 №30 的白名单来源
 │   ├─ storage.json        — 个人已验证的配置（合并进 30.txt）
 │   ├─ cidrwhitelist.txt   — CIDR 白名单（绕过封锁）
 │   ├─ cn_cidr.txt         — 中国的 CIDR 网段（用于文件 №31）
 │   ├─ hk_cidr.txt         — 香港的 CIDR 网段（№31 排除项）
 │   ├─ mo_cidr.txt         — 澳门的 CIDR 网段（№31 排除项）
 │   ├─ tw_cidr.txt         — 台湾的 CIDR 网段（№31 排除项）
 │   ├─ ir_cidr.txt         — 伊朗的 CIDR 网段（用于文件 №32）
 │   └─ sni_domains.json    — SNI 域名白名单
 └─ src/
     ├─ __init__.py
     ├─ config.py           — 配置路径与加载
     ├─ file_manager.py     — 下载、过滤、白名单、文件组装
     ├─ validator.py        — 配置结构校验
     ├─ healthcheck.py      — 存活检查（TCP/TLS）
     ├─ cidr.py             — CIDR 列表处理
     ├─ parser.py           — 不安全配置过滤
     ├─ network.py          — 带 retry/ETag 的 HTTP 会话
     ├─ qr_generator.py     — QR 码生成
     ├─ git_ops.py          — 提交并推送变更
     ├─ github_api.py       — GitHub API
     ├─ readme_updater.py   — README 自动更新
     ├─ release_fetcher.py  — 客户端的最新下载链接
     ├─ logger.py           — 日志
     └─ github_api.py       — 仓库统计
 LICENSE               — GPL-3.0 许可证
 README.md             — 本文件（俄语）
 README.en.md          — 英语翻译
 README.zh.md          — 简体中文翻译
 README.fa.md          — 波斯语翻译（فارسی）
```

---

## 🔧 本地运行生成器

```bash
git clone https://github.com/pie-with-jam/PulseProxy.git
cd PulseProxy/source
python -m pip install -r requirements.txt
export MY_TOKEN=<GITHUB_TOKEN>   # 具有 contents:write 权限的 PAT，用于推送变更
python main.py                   # 配置将生成到 ../githubmirror
```

> **重要！** 没有 `MY_TOKEN` 生成器也能运行，但不会执行提交/推送变更。

---

# 📋 所有永久有效配置的总列表

> 推荐列表：**[1](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt)**、**[6](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt)**、**[22](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt)**、**[23](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt)**、**[24](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt)** 和 **[25](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt)**。

> 绕过 SNI/CIDR 白名单：**[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**。

> 中国用：**[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**，伊朗用：**[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** —— 不含这两个国家境内的服务器。

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

> 🔗 [永久有效配置的 QR 码链接](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes)

---

# 📷 QR 码

所有订阅的 QR 码都存放在 [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) 文件夹中 —— `1.png` … `32.png`。QR 编码的是**订阅链接**，因此适合导入移动客户端和 Android TV（这些地方不方便以文本形式粘贴链接）。

---

# 🗂️ 客户端指南

<details>

<summary>📱 Android 指南（v2rayNG）</summary>

**1.** 下载 **「v2rayNG」** —— [最新版本](https://github.com/2dust/v2rayNG/releases)（APK `arm64-v8a`）。

**2.** 从 **「📋 所有永久有效配置的总列表」** 一节复制需要的链接到剪贴板。

**3.** 打开 **「v2rayNG」** 应用，点击右上角的 ➕，然后选择 **「从剪贴板导入」**。

**4.** 点击右上角的 **「三个点」** → **「测试配置延迟」**；完成后在同一菜单中点击 **「按测试结果排序」**。

**5.** 选择需要的服务器，点击右下角的 ▶️ 按钮。

**更新配置：** 左上角的 **「三条横线」** 菜单 → **「分组」** → 右上角的 **「圆圈箭头」** 图标 → 等待更新完成。

> 🧭 **建议：** 配置好**路由规则**（伊朗/中国/俄罗斯的流量直连，其余走代理），并关闭 **mux** 和**分片** —— 参见 [「📱 Android 版 v2rayNG 路由规则」](#-android-版-v2rayng-路由规则)。

</details>

<details>

<summary>📺 Android TV 指南</summary>

**1.** 下载 **「v2rayNG」** —— [最新版本](https://github.com/2dust/v2rayNG/releases)（APK `armeabi-v7a`）。

**2.** 从 [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) 文件夹下载需要的 **QR 码**。

**3.** 打开 **「v2rayNG」** → ➕ → **「从 QR 码导入」** → 选择图片（右上角的照片图标）。

**4.** **「三个点」** → **「测试配置延迟」** → **「按测试结果排序」**。

**5.** 选择服务器并点击 ▶️。

</details>

<details>

<summary>🖥 Windows、Linux 指南（Throne）</summary>

**1.** 下载 **「Throne」** —— [最新版本](https://github.com/throneproj/Throne/releases)（`windows64` / `windowslegacy64` / `linux-amd64`）。

**2.** 从 **「📋 所有永久有效配置的总列表……」** 一节复制需要的链接到剪贴板。

**3.** **「配置文件」** → **「从剪贴板添加配置文件」**。

**4.** 按 **Ctrl+A** 全选所有配置，然后 **「配置文件」** → **「测试所选配置的延迟（ping）」** 并等待完成（「日志」中会出现「延迟（ping）测试已完成！」）。

**5.** 点击 **「延迟（ping）」** 列进行排序。

**6.** 在窗口顶部启用 **「TUN 模式」**（打勾）。

**7.** 选择 ping 最低的配置 → **鼠标左键** → **「启动」**。

**更新配置：** 「设置」→「分组」→ **「更新所有订阅」**。

</details>

<details>

<summary>☎ iOS、iPadOS 指南（V2Box）</summary>

**1.** 下载 **「V2Box - V2ray Client」** —— [App Store](https://apps.apple.com/ru/app/v2box-v2ray-client/id6446814690)。

**2.** 从 **「📋 所有永久有效配置的总列表……」** 一节复制需要的链接到剪贴板。

**3.** 在应用中切换到 **「Config」** 标签页 → 右上角的加号 → **「添加订阅」** → 输入名称并把链接粘贴到 **「URL」** 字段。

**4.** 等待检查完成，点击名称选择配置。

**5.** 点击底部面板的 **「连接」**。

**更新配置：** 「Config」标签页 → 分组名称左侧的更新图标。

</details>

<details>

<summary>💻 MacOS 指南（Hiddify）</summary>

**1.** 下载 **「Hiddify」** —— [最新版本](https://github.com/hiddify/hiddify-app/releases)（`Hiddify-MacOS.dmg`）。

**2.** 点击 **「新建配置文件」** → **「从剪贴板添加」**（链接从 **「📋 所有永久有效配置的总列表……」** 一节复制）。

**3.** **「设置」** → **「路由方案」** → 选择合适的地区。

**4.** 左上角的设置图标 → **「VPN 服务」** → 打开 **「VPN」**（中间的图标）。

**5.** 如需更换服务器：**「代理」** 标签页。

**更新配置：** 选择配置文件 → 名称左侧的更新图标。

</details>

---

# 📱 Android 版 v2rayNG 路由规则

在 Android 上，我们推荐 **[v2rayNG](https://github.com/2dust/v2rayNG/releases)** 搭配**路由规则**使用：本地（伊朗、中国、俄罗斯）以及「自己人」的流量**直连**，只有真正需要绕过的内容才走代理。这样更稳定、更快，代理的负担也更小。

### 🧭 现成的路由文件

**[`routing/v2rayng-routing.json`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/routing/v2rayng-routing.json)** —— 可导入 v2rayNG 的规则（首条匹配生效）：

- **直连（direct）：**
  - 局域网（LAN）；
  - **伊朗**（`geoip:ir` + 后缀 `domain:ir`）、**中国**（`geoip:cn` / `geosite:cn`）、**俄罗斯**（`geoip:ru` + 后缀 `domain:ru` / `domain:su`）；
  - 中国和俄罗斯的公共 DNS（AliDNS、DNSPod、Yandex、SafeDNS）；
  - IP 与 DNS 泄漏检测服务 —— **ipify.org, 2ip.io, icanhazip.com, ifconfig.me, ipleak.net, dnsleaktest.com** 等（用于查看**真实** IP）；
  - 应用商店 —— **F-Droid, Huawei, Xiaomi**、Samsung、Amazon（巨大的下载流量不走代理）。
- **阻断：** QUIC（`UDP 443`）—— 流量被强制转为 TCP，有助于绕过 DPI（在伊朗/俄罗斯很常见）。
- **其余全部 → 走代理**（默认行为，无需额外设置）。

**导入方式：** 复制 JSON 内容 → 在 v2rayNG 中点击左上角 **「三条横线」** → **「设置」** → **「Routing」** → **「⋮」** → **「从剪贴板导入」**。规则顺序很重要 —— 请勿打乱或删除 `geoip:private` 块。

> ✅ **在 v2rayNG 正式版中稳定运行：** 本文件只使用标准 `geosite.dat` 中确实存在的分类（`geosite:private`、`geosite:cn`）以及 TLD 后缀 `domain:ir` / `domain:ru`。标准 `geosite.dat` 中**没有** `geosite:ir` 和 `geosite:ru` 分类 —— 任何引用它们的规则都会导致配置失败并报错 `code not found in geosite.dat: IR`。如果导入第三方或旧版规则后出现该错误 —— 请删除含 `geosite:ir` / `geosite:ru` 的规则，或重新导入本文件（无需更新 Geo 文件：任何标准构建中都不存在这些分类）。

> ⚠️ **重要：无论你身在何处，都要启用全部路由规则（`enabled: true`）。** 不要关闭「别国」的规则 —— 它们不会造成干扰，只是让需要的流量绕过代理（例如，你可以住在俄罗斯，但保留伊朗/中国的规则处于开启状态）。

### ⚙️ 客户端推荐设置

- **订阅：** 来自**中国**用文件 **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**，来自**伊朗**用文件 **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)**（不含这两个国家境内的服务器）；来自俄罗斯请从文件 **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** 开始。
- **Mux** —— **关闭**（设置 → Mux → disable）。Mux 经常会弄坏 TLS 和网站。
- **分片（fragment）** —— **关闭**。仅在特定网站按 SNI 被切断时针对性开启。
- **Remote DNS：** 白名单模式（文件 **30**）用运营商 DNS 或 Yandex；普通模式用 DoH：`https://dns.google/dns-query`（Google）或 `https://cloudflare-dns.com/dns-query`（Cloudflare）。
- **域名策略**（「设置」→「Routing」→「Domain Strategy」）—— **`IPIfNonMatch`**：先按域名匹配，未命中任何规则的域名才解析 IP 检查 `geoip` 规则。不要保留 `AsIs`（默认值）—— 该模式下 `geoip:ir` / `geoip:cn` / `geoip:ru` 无法匹配域名，本地流量会走代理；`IPOnDemand` 则会对每个连接多余地解析 DNS。注意：`IPIfNonMatch` 会解析未命中的域名，因此 Remote DNS 必须用 DoH（见上）。

---

# ⚠️ 常见问题排查

<details>

<summary>⚠ v2rayNG 中「测试配置延迟」卡住（检查进行到 N 就「卡住」了）</summary>

公开配置数量庞大（有时数以千计），对每一个都做真实连接测试非常耗时。

**1.** 将 **v2rayNG** 更新到最新版本 —— [版本发布](https://github.com/2dust/v2rayNG/releases)。

**2.** 在检测菜单中把测试类型从 **REALITY/HTTP** 改为 **TCP ping** —— TCP ping 瞬间即可完成，配置不会「卡住」。

**3.** 或者干脆不等检测完成：导入订阅，等配置出现后直接连接需要的那个 —— 检测并非必需。

</details>

<details>

<summary>⚠ 在 v2rayNG 中添加订阅后没有出现配置</summary>

**1.** 点击左上角的 **「三条横线」**。

**2.** 打开 **「分组」**。

**3.** 点击右上角的 **「圆圈箭头」** 并等待更新完成。

</details>

<details>

<summary>⚠ 连接 VPN 后没有网络</summary>

**1.** 换用订阅中的另一个配置（关闭再打开 VPN，或选择 ping 更低的服务器）。

**2.** 如果 ping 正常但没有流量 —— 在客户端中把 **Remote DNS** 改为 DoH，例如 `https://dns.google/dns-query`（Google）或 `https://cloudflare-dns.com/dns-query`（Cloudflare）（v2rayNG 中：「设置」→「DNS 设置」→「Basic DNS Settings」）。

**3.** 白名单模式（文件 30）请使用运营商 DNS（或 Yandex）—— 境外 DNS 在白名单模式下无法工作。

</details>

<details>

<summary>⚠ 报错「net/http: 12x handshake timeout」和「io: read/write closed pipe」</summary>

**1.** 在桌面上长按 **「v2rayNG」** 图标 → **「应用信息」**。

**2.** 点击 **「强行停止」** 并重新启动应用。

**3.** 更新订阅（分组 → ⟳）并重新连接。

</details>

<details>

<summary>⚠ Windows 上 Throne 的 MSVCP/VCRUNTIME 错误</summary>

**1.** **Win+R** → `control` → **「程序和功能」**。

**2.** 在右侧搜索框中输入 **「Visual」**，卸载所有 **「Microsoft Visual C++」** 组件。

**3.** 下载并解压 **Visual C++ Runtimes All-in-One** 合集。

**4.** **以管理员身份运行** `install_bat.all`，等待安装完成。

</details>

---

# ⚠️ 免责声明

**使用本仓库及其配置，即表示你自行承担使用它们的全部责任。**

- 作者**不对**使用所发布配置的任何后果承担责任：这既包括可用性，也包括安全性，以及你的运营商或其他组织可能施加的限制。
- 所有配置都是部分**公开的** —— 它们由第三方发布和更新；本项目的作者只是收集、过滤并以方便的形式发布，不保证其内容、可用性和持续运行。
- 本项目**非商业性质，按「原样」提供**（`as is`）：不提供任何保证，对于任何损失、故障、封锁或其他后果均不承担责任。
- 你有责任自行评估风险并遵守所在国家的法律。

---

# 🙏 致谢

本项目的基本思路、结构和源代码取自 **[AvenCores / goida-vpn-configs](https://gitlab.com/avencores/goida-vpn-configs)** —— 非常**感谢作者 AvenCores** 所做的工作！ ❤️

PulseProxy 是一个带有改进的分支：加入了健康检查、配置结构校验、带 SNI/CIDR 白名单的特殊文件 №30、作者自用配置（`storage.json`），以及通过 GitHub Actions 每约 30 分钟更新一次。

---

# 📜 许可证

本项目以 **GPL-3.0** 许可证发布。许可证全文见 [`LICENSE`](LICENSE) 文件。

---

<!-- 💰 支持作者 -->

如果本项目对你有帮助，你可以支持它的发展：

| 网络 / 币种 | 转账地址 | QR 码 |
| :--- | :--- | :---: |
| **GRAM (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="GRAM TON QR"> |
| **USDT (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="USDT TON QR"> |
| **BTC (BitCoin network)** | `bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz" width="130" height="130" alt="BTC QR"> |
| **ETH (Etherium)** | `0xF162fb13798A7B177d9d7fB0C923779c1bFD0258` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=0xF162fb13798A7B177d9d7fB0C923779c1bFD0258" width="130" height="130" alt="ETH QR"> |

> ⚠️ **注意：** 请**只在指定的网络中**发送代币 —— GRAM/USDT 用 **TON** 网络，BTC 用 **BitCoin** 网络，ETH 用 **Etherium** 网络。
