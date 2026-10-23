<p align="center">
  <a href="https://github.com/pie-with-jam/PulseProxy"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <img src="https://img.shields.io/github/last-commit/pie-with-jam/PulseProxy?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/pie-with-jam/PulseProxy?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/stars/pie-with-jam/PulseProxy?style=for-the-badge" alt="Stars">
</p>

<p align="center">
  <b>🇷🇺 Русский</b> · <a href="./README.en.md">🇬🇧 English</a> · <a href="./README.zh.md">🇨🇳 中文</a> · <a href="./README.fa.md">🇮🇷 فارسی</a>
</p>

# 📖 Описание проекта

Автоматически обновляемая коллекция публичных VPN-конфигов (`V2Ray` / `VLESS` / `VMess` / `Trojan` / `Shadowsocks` / `Hysteria2` / `Tuic` / `Reality`) для обхода блокировок, включая конфиги для обхода SNI/CIDR белых списков и страновые списки для Китая и Ирана.

Каждый конфиг — это TXT-подписка, которую можно импортировать практически в любой современный клиент (`v2rayNG`, `Throne`, `v2rayN`, `V2Box`, `Hiddify`, `Karing`, `Streisand` и др.).

Конфиги обновляются **автоматически каждые ~30 минут** (GitHub Actions + внешний триггер), проходят **проверку на живость** (healthcheck) и **структурную валидацию**, поэтому ссылки из раздела **«📋 Общий список всех вечно актуальных конфигов»** всегда актуальны.

## 📑 Содержание
- [🚀 Быстрый старт](#-быстрый-старт)
- [📊 Статус конфигов](#-статус-конфигов)
- [🔓 Файл №30 — обход SNI/CIDR белых списков](#-файл-30--обход-snicidr-белых-списков)
- [🇨🇳🇮🇷 Файлы №31 и №32 — для Китая и Ирана](#-файлы-31-и-32--для-китая-и-ирана)
- [⚙️ Как это работает](#️-как-это-работает)
- [🗂 Структура репозитория](#-структура-репозитория)
- [🔧 Локальный запуск генератора](#-локальный-запуск-генератора)
- [📋 Общий список всех вечно актуальных конфигов](#-общий-список-всех-вечно-актуальных-конфигов)
- [📷 QR-коды](#-qr-коды)
- [🗂️ Гайды по клиентам](#️-гайды-по-клиентам)
- [📱 Маршрутизация v2rayNG для Android](#-маршрутизация-v2rayng-для-android)
- [⚠️ Решение типичных проблем](#️-решение-типичных-проблем)
- [⚠️ Отказ от ответственности](#️-отказ-от-ответственности)
- [🙏 Благодарности](#-благодарности)
- [📜 Лицензия](#-лицензия)

---

## 🚀 Быстрый старт
1. Скопируйте нужную ссылку из раздела **«📋 Общий список всех вечно актуальных конфигов»**.
2. Импортируйте её в ваш **VPN-клиент** (см. гайды ниже).
3. Проверьте задержку профилей, выберите сервер с минимальным пингом и подключайтесь.

> 💡 **Для мобильного интернета в РФ** начните с файла **[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** — это отобранный по белым спискам SNI/CIDR список, прошедший проверку живости.
>
> 💡 **Для Китая** — файл **[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, **для Ирана** — **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (без серверов внутри этих стран).

---

## 📊 Статус конфигов

> **⚠️ Внимание!** Эта таблица показывает **источники** и текущее количество конфигов. **Не копируйте ссылки отсюда!** Ссылки для импорта — в разделе **«📋 Общий список всех вечно актуальных конфигов»** ниже.

| № | Файл | Источник | Конфигов |
|--|--|--|--|
| 1 | [`1.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt) | [sakha1370/OpenRay](https://github.com/sakha1370/OpenRay/raw/refs/heads/main/output/all_valid_proxies.txt) | 10 553 |
| 2 | [`2.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/2.txt) | [sevcator/5ubscrpt10n](https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt) | 405 412 |
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
| 30 | [`30.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt) | **Спецфайл: обход SNI/CIDR белых списков** (источники 1–29 + `30_urls.json` + `storage.json`, healthcheck) | 1 094 |
| 31 | [`31.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt) | **Для Китая** (без серверов внутри CN по `cn_cidr.txt`, healthcheck) | 977 |
| 32 | [`32.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt) | **Для Ирана** (без серверов внутри IR по `ir_cidr.txt`, healthcheck) | 945 |

> Количество конфигов указано на **13.10.2026** и обновляется при каждом цикле сборки.

---

## 🔓 Файл №30 — обход SNI/CIDR белых списков

**[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** — отдельный спецфайл для работы через белые списки (мобильный интернет, режим «беспилотной опасности»):

- кандидаты собираются из файлов **1–29** и дополнительных источников списка **`30_urls.json`** (готовые обходные подписки);
- отсеиваются конфиги, не проходящие **белые списки CIDR/SNI** (`cidrwhitelist.txt`, `sni_domains.json`);
- каждый конфиг проходит **структурную валидацию**: чинятся склеенные ссылки `&amp;` → `&`, отбрасываются битые URL (невалидный UUID, reality без `pbk`, сломанный Base64 и т.п.);
- проходит **healthcheck** живости (одно TCP/TLS-соединение на конфиг);
- слияние с **`storage.json`** — личными проверенными конфигами.

> Если конфиги из обычных файлов (1–29) не проходят белые списки — используйте именно **30.txt**.

### 🪞 Русские зеркала / обходы для подписки №30 (режим беспилотной опасности)

Если сама ссылка `raw.githubusercontent.com` не открывается (режим белых списков / беспилотной опасности) — используйте **прокси-ссылки Яндекс.Переводчика** для обновления подписки №30 в клиенте:

1. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fraw.githack.com%2Fpie-with-jam%2FPulseProxy%2Frefs%2Fheads%2Fmain%2Fgithubmirror%2F30.txt&lang=de-de`
2. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpie-with-jam%2FPulseProxy%40main%2Fgithubmirror%2F30.txt&lang=de-de`

> ✦ Ссылки полностью повторяют содержимое `30.txt` и обновляются вместе с ним — вставьте одну из них в поле URL подписки вместо обычной ссылки.
>
> ✦ Работает именно связка **Yandex +** (`raw.githack.com` / `cdn.jsdelivr.net`); другие связки с Яндексом могут ломать конфигурации.
>
> ✦ Если первая ссылка не открывается — пробуйте вторую (и наоборот). После обновления в клиенте переподключитесь.

---

## 🇨🇳🇮🇷 Файлы №31 и №32 — для Китая и Ирана

**[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)** и **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — страновые подписки для пользователей за национальными файрволами (КНР, Иран):

- кандидаты собираются из файлов **1–29** и `storage.json` (дедупликация, структурная валидация);
- **исключаются серверы внутри страны**: конфиги с IP из `cn_cidr.txt` / `ir_cidr.txt` (8 802 / 1 901 подсетей) отсеиваются статически, а домены проверяются по реальному IP соединения при healthcheck — подключаться к серверу в своей же стране для обхода её же блокировок бессмысленно; **Гонконг, Макао и Тайвань** (`hk_cidr.txt` / `mo_cidr.txt` / `tw_cidr.txt`) из исключения исключены: они вне GFW и остаются полезными близкими выходами;
- проходит **healthcheck** живости (TCP/TLS-хендшейк) с равномерной выборкой до 4 000 кандидатов на файл (полный пул 1–29 слишком большой для проверки целиком; лимит настраивается `COUNTRY_PROBE_LIMIT`).

> ⚠️ **Важно:** живость проверяется **с серверов GitHub Actions, а не из Китая/Ирана** — GFW/иранский фильтр может блокировать часть работающих отовсюду конфигов. Файл — это отфильтрованный кандидат, а не гарантия доступности внутри страны; при недоступности пробуйте следующие серверы списка.

> 💡 Эти файлы также рекомендованы для пользователей из этих стран в разделе маршрутизации v2rayNG ниже.

---

## ⚙️ Как это работает
1. **GitHub Actions** (`.github/workflows/auto_update.yml`) запускает сборку **по расписанию каждые ~30 минут** (`:07` и `:37` каждого часа UTC), плюс внешний триггер с сервера дёргает workflow в `:25` и `:55`. Есть и ручной запуск (`manual_update.yml`).
2. Скрипт скачивает конфиги из **29 публичных источников** (`urls.json`) параллельно, используя ETag/If-Modified-Since (повторные скачивания без изменений не тратят трафик).
3. Каждый конфиг фильтруется: декодируется Base64, проверяется наличие протоколов (`vmess://`, `vless://`, `trojan://`, `ss://`, `hysteria2://`, `tuic://` и др.), удаляются небезопасные конфиги (`allowInsecure=1`), дедупликация.
4. **Файл №30** формируется отдельно: сбор кандидатов из 1–29 + `30_urls.json` → фильтр по белым спискам CIDR/SNI → структурная валидация → healthcheck → слияние с `storage.json`.
5. **Файлы №31 (Китай) и №32 (Иран)** формируются из 1–29 + `storage.json` → исключение серверов внутри страны по CIDR (`cn_cidr.txt` / `ir_cidr.txt`; для №31 исключения HK/MO/TW) → валидация → healthcheck (выборка до 4 000 кандидатов).
6. Генерируются **QR-коды** (`qr-codes/1.png` … `32.png`) — кодируют URL подписки.
7. Все изменения коммитятся и пушатся в репозиторий — ссылки в README всегда актуальны.

## 🗂 Структура репозитория
```text
.github/workflows/   — CI/CD GitHub Actions
 ├─ auto_update.yml     — авто-обновление каждые ~30 мин по расписанию (+ workflow_dispatch)
 └─ manual_update.yml   — ручной запуск сборки
githubmirror/        — сгенерированные .txt подписки (32 файла)
qr-codes/            — QR-коды подписок для импорта (32 PNG)
source/              — исходный код и конфигурации генератора
 ├─ main.py             — основной скрипт генерации
 ├─ requirements.txt    — зависимости Python
 ├─ config/
 │   ├─ urls.json           — 29 публичных источников (файлы 1–29)
 │   ├─ 30_urls.json        — источники белых списков для спецфайла №30
 │   ├─ storage.json        — личные проверенные конфиги (сливаются в 30.txt)
 │   ├─ cidrwhitelist.txt   — белый список CIDR (обход блокировок)
 │   ├─ cn_cidr.txt         — CIDR-сети Китая (для файла №31)
 │   ├─ hk_cidr.txt         — CIDR-сети Гонконга (исключение из №31)
 │   ├─ mo_cidr.txt         — CIDR-сети Макао (исключение из №31)
 │   ├─ tw_cidr.txt         — CIDR-сети Тайваня (исключение из №31)
 │   ├─ ir_cidr.txt         — CIDR-сети Ирана (для файла №32)
 │   └─ sni_domains.json    — белый список SNI-доменов
 └─ src/
     ├─ __init__.py
     ├─ config.py           — пути и загрузка конфигурации
     ├─ file_manager.py     — скачивание, фильтрация, белые списки, сборка файлов
     ├─ validator.py        — структурная валидация конфигов
     ├─ healthcheck.py      — проверка живости (TCP/TLS)
     ├─ cidr.py             — работа с CIDR-списками
     ├─ parser.py           — фильтрация небезопасных конфигов
     ├─ network.py          — HTTP-сессия с retry/ETag
     ├─ qr_generator.py     — генерация QR-кодов
     ├─ git_ops.py          — коммит и push изменений
     ├─ github_api.py       — GitHub API
     ├─ readme_updater.py   — автообновление README
     ├─ release_fetcher.py  — актуальные ссылки на скачивание клиентов
     ├─ logger.py           — логирование
     └─ github_api.py       — статистика репозитория
 LICENSE               — лицензия GPL-3.0
 README.md             — этот файл (русский)
 README.en.md          — перевод на английский
 README.zh.md          — перевод на упрощённый китайский
 README.fa.md          — персидский перевод (فارسی)
```

---

## 🔧 Локальный запуск генератора

```bash
git clone https://github.com/pie-with-jam/PulseProxy.git
cd PulseProxy/source
python -m pip install -r requirements.txt
export MY_TOKEN=<GITHUB_TOKEN>   # PAT с правами contents:write, чтобы пушить изменения
python main.py                   # конфиги появятся в ../githubmirror
```

> **Важно!** Без `MY_TOKEN` генерация работает, но коммит/push изменений выполняться не будет.

---

# 📋 Общий список всех вечно актуальных конфигов

> Рекомендованные списки: **[1](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt)**, **[6](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt)**, **[22](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt)**, **[23](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt)**, **[24](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt)** и **[25](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt)**.

> Обход SNI/CIDR белых списков: **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**.

> Для Китая: **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, для Ирана: **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — без серверов внутри этих стран.

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

> 🔗 [Ссылка на QR-коды вечно актуальных конфигов](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes)

---

# 📷 QR-коды

QR-коды всех подписок лежат в папке [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) — `1.png` … `32.png`. QR кодирует **ссылку на подписку**, поэтому подходит для импорта в мобильные клиенты и на Android TV (куда неудобно вставлять ссылку текстом).

---

# 🗂️ Гайды по клиентам

<details>

<summary>📱 Гайд для Android (v2rayNG)</summary>

**1.** Скачиваем **«v2rayNG»** — [Последний релиз](https://github.com/2dust/v2rayNG/releases) (APK `arm64-v8a`).

**2.** Копируем в буфер обмена нужную ссылку из раздела **«📋 Общий список всех вечно актуальных конфигов»**.

**3.** Заходим в приложение **«v2rayNG»** и в правом верхнем углу нажимаем на ➕, затем выбираем **«Импорт из буфера обмена»**.

**4.** Нажимаем **«три точки»** справа сверху → **«Проверить задержку профилей»**; после окончания в этом же меню нажмите **«Сортировать по результатам теста»**.

**5.** Выбираем нужный сервер и нажимаем кнопку ▶️ в правом нижнем углу.

**Обновление конфигов:** меню «три полоски» слева сверху → **«Группы»** → иконка «кружок со стрелкой» справа сверху → дождаться окончания обновления.

> 🧭 **Совет:** настройте **маршрутизацию** (трафик по Ирану/Китаю/России — напрямую, остальное — через прокси) и отключите **mux** и **фрагментацию** — см. раздел [«📱 Маршрутизация v2rayNG для Android»](#-маршрутизация-v2rayng-для-android).

</details>

<details>

<summary>📺 Гайд для Android TV</summary>

**1.** Скачиваем **«v2rayNG»** — [Последний релиз](https://github.com/2dust/v2rayNG/releases) (APK `armeabi-v7a`).

**2.** Скачиваем нужный **QR-код** из папки [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes).

**3.** Заходим в **«v2rayNG»** → ➕ → **«Импорт из QR-кода»** → выбираем картинку (иконка фото справа сверху).

**4.** «Три точки» → **«Проверить задержку профилей»** → **«Сортировать по результатам теста»**.

**5.** Выбираем сервер и нажимаем ▶️.

</details>

<details>

<summary>🖥 Гайд для Windows, Linux (Throne)</summary>

**1.** Скачиваем **«Throne»** — [Последний релиз](https://github.com/throneproj/Throne/releases) (`windows64` / `windowslegacy64` / `linux-amd64`).

**2.** Копируем в буфер обмена нужную ссылку из раздела **«📋 Общий список...»**.

**3.** **«Профили»** → **«Добавить профиль из буфера обмена»**.

**4.** Выделяем все конфиги **Ctrl+A**, затем **«Профили»** → **«Тест задержки (пинга) выбранного профиля»** и ждём окончания (в «Логах» появится «Тест задержек (пинга) завершён!»).

**5.** Кликаем по колонке **«Задержка (пинг)»** — сортировка.

**6.** Вверху окна включаем опцию **«Режим TUN»** (галочка).

**7.** Выбираем конфиг с наименьшим пингом → **ЛКМ** → **«Запустить»**.

**Обновление конфигов:** «Настройки» → «Группы» → **«Обновить все подписки»**.

</details>

<details>

<summary>☎ Гайд для iOS, iPadOS (V2Box)</summary>

**1.** Скачиваем **«V2Box - V2ray Client»** — [App Store](https://apps.apple.com/ru/app/v2box-v2ray-client/id6446814690).

**2.** Копируем в буфер обмена нужную ссылку из раздела **«📋 Общий список...»**.

**3.** В приложении переходим во вкладку **«Config»** → плюсик справа сверху → **«Добавить подписку»** → вводим название и вставляем ссылку в поле **«URL»**.

**4.** Ждём окончания проверки, выбираем конфиг нажатием на название.

**5.** В нижней панели нажимаем **«Подключиться»**.

**Обновление конфигов:** вкладка «Config» → иконка обновления слева от названия группы.

</details>

<details>

<summary>💻 Гайд для MacOS (Hiddify)</summary>

**1.** Скачиваем **«Hiddify»** — [Последний релиз](https://github.com/hiddify/hiddify-app/releases) (`Hiddify-MacOS.dmg`).

**2.** Нажимаем **«Новый профиль»** → **«Добавить из буфера обмена»** (ссылку копируем из раздела **«📋 Общий список...»**).

**3.** **«Настройки»** → **«Вариант маршрутизации»** → выбираем подходящий регион.

**4.** Иконка настроек слева сверху → **«VPN сервис»** → включаем **«VPN»** (иконка по центру).

**5.** Для смены сервера: вкладка **«Прокси»**.

**Обновление конфигов:** выберите профиль → иконка обновления слева от названия.

</details>

---

# 📱 Маршрутизация v2rayNG для Android

Для Android рекомендуем **[v2rayNG](https://github.com/2dust/v2rayNG/releases)** в связке с **правилами маршрутизации**: локальный (иранский, китайский, российский) и «свой» трафик идёт **напрямую**, а через прокси — только то, что действительно нужно обходить. Так стабильнее, быстрее и меньше нагрузка на прокси.

### 🧭 Готовый файл маршрутизации

**[`routing/v2rayng-routing.json`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/routing/v2rayng-routing.json)** — правила для импорта в v2rayNG (первое совпадение выигрывает):

- **Напрямую (direct):**
  - локальная сеть (LAN);
  - **Иран** (`geoip:ir` / `geosite:ir`), **Китай** (`geoip:cn` / `geosite:cn`), **Россия** (`geoip:ru` / `geosite:ru`);
  - китайские и российские публичные DNS (AliDNS, DNSPod, Яндекс, SafeDNS);
  - сервисы определения IP и утечек DNS — **ipify.org, 2ip.io, icanhazip.com, ifconfig.me, ipleak.net, dnsleaktest.com** и др. (чтобы видеть **реальный** IP);
  - магазины приложений — **F-Droid, Huawei, Xiaomi**, Samsung, Amazon (огромные загрузки не гоняются через прокси).
- **Блок:** QUIC (`UDP 443`) — трафик форсится в TCP, что помогает обходить DPI (часто в Иране/РФ).
- **Всё остальное → через прокси** (поведение по умолчанию — ничего дополнительно настраивать не нужно).

**Импорт:** скопируйте содержимое JSON → в v2rayNG «три полоски» слева → **«Настройки»** → **«Routing»** → **«⋮»** → **«Импорт из буфера обмена»**. Порядок правил важен — не перемешивайте и не удаляйте блок `geoip:private`.

> ⚠️ **Важно: включайте ВСЕ правила маршрутизации (`enabled: true`), независимо от того, где вы живёте.** Не отключайте правила «для чужих» стран — они не мешают, а просто пропускают мимо прокси только нужный трафик (например, вы можете жить в РФ, но правила для Ирана/Китая оставить включёнными).

### ⚙️ Рекомендуемые настройки клиента

- **Подписка:** из **Китая** — файл **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**, из **Ирана** — файл **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (без серверов внутри этих стран); из РФ начните с файла **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**.
- **Mux** — **выкл.** (Настройки → Mux → disable). Mux часто ломает TLS и сайты.
- **Фрагментация (fragment)** — **выкл.** Включайте точечно, только если конкретный сайт режется по SNI.
- **Remote DNS:** для белых списков (файл **30**) — DNS провайдера или Яндекс; для обычного режима — `https://dns.google/dns-query`.

---

# ⚠️ Решение типичных проблем

<details>

<summary>⚠ Зависает «Проверка задержки профилей» в v2rayNG (проверка дошла до N и «зависла»)</summary>

Публичных конфигов много (иногда тысячи), реальный тест соединения на каждом — очень долгий.

**1.** Обновите **v2rayNG** до последней версии — [Релизы](https://github.com/2dust/v2rayNG/releases).

**2.** В меню проверки смените тип теста с **REALITY/HTTP** на **TCP ping** — TCP-пинг проверяется мгновенно, конфиг не «висит».

**3.** Или не ждите полной проверки: импортируйте подписку, дождитесь появления конфигов и подключайтесь к нужному — проверка необязательна.

</details>

<details>

<summary>⚠ Не появились конфиги при добавлении подписки в v2rayNG</summary>

**1.** Нажмите **«три полоски»** в левом верхнем углу.

**2.** Открываем **«Группы»**.

**3.** Нажимаем **«кружок со стрелкой»** справа сверху и ждём окончания обновления.

</details>

<details>

<summary>⚠ Нет интернета при подключении к VPN</summary>

**1.** Попробуйте другой конфиг из подписки (включи/выключи VPN или выберите сервер с меньшим пингом).

**2.** Если пинг успешный, а трафика нет — смените **Remote DNS** в клиенте, например на `https://dns.google/dns-query` (в v2rayNG: «Настройки» → «Настройки DNS» → «Basic DNS Settings»).

**3.** Для белых списков (файл 30) используйте DNS провайдера (или Яндекс) — иностранные DNS в режиме БС не работают.

</details>

<details>

<summary>⚠ Ошибки «net/http: 12x handshake timeout» и «io: read/write closed pipe»</summary>

**1.** На рабочем столе зажмите иконку **«v2rayNG»** → **«О приложении»**.

**2.** Нажмите **«Остановить»** и заново запустите приложение.

**3.** Обновите подписку (Группы → ⟳) и подключитесь снова.

</details>

<details>

<summary>⚠ Ошибка MSVCP/VCRUNTIME в Throne на Windows</summary>

**1.** **Win+R** → `control` → **«Программы и компоненты»**.

**2.** В поиске справа впишите **«Visual»** и удалите все компоненты **«Microsoft Visual C++»**.

**3.** Скачайте и распакуйте сборку **Visual C++ Runtimes All-in-One**.

**4.** Запустите **от имени администратора** `install_bat.all` и дождитесь окончания установки.

</details>

---

# ⚠️ Отказ от ответственности

**Используя данный репозиторий и его конфигурации, вы принимаете на себя всю ответственность за их применение.**

- Автор **не несёт ответственности** за любые последствия использования опубликованных конфигураций: это касается и работоспособности, и безопасности, и возможных ограничений со стороны вашего провайдера или иных организаций.
- Все конфигурации являются частично **публичными** — их размещают и обновляют третьи лица; автор проекта только собирает, фильтрует и публикует их в удобном виде, не гарантируя их содержимое, доступность и непрерывную работу.
- Проект **некоммерческий и сделан «как есть»** (`as is`): гарантий не предоставляется, за любые убытки, сбои, блокировки или прочие последствия ответственность не несётся.
- Вы обязане самостоятельно оценивать риски и соблюдать законодательство своей страны.

---

# 🙏 Благодарности

Базовая идея, структура и исходный код этого проекта взяты у **[AvenCores / goida-vpn-configs](https://gitlab.com/avencores/goida-vpn-configs)** — огромное **спасибо автору AvenCores** за проделанную работу! ❤️

PulseProxy — форк с доработками: добавлены healthcheck, структурная валидация конфигов, спецфайл №30 с белыми списками SNI/CIDR, авторские конфиги (`storage.json`) и обновление каждые ~30 минут через GitHub Actions.

---

# 📜 Лицензия

Проект распространяется под лицензией **GPL-3.0**. Полный текст лицензии содержится в файле [`LICENSE`](LICENSE).

---

<!-- 💰 Поддержать автора -->

Если проект оказался полезным, вы можете поддержать его развитие:

| Сеть / Монета | Адрес для перевода | QR-код |
| :--- | :--- | :---: |
| **GRAM (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="GRAM TON QR"> |
| **USDT (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="USDT TON QR"> |
| **BTC (BitCoin network)** | `bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz" width="130" height="130" alt="BTC QR"> |
| **ETH (Etherium)** | `0xF162fb13798A7B177d9d7fB0C923779c1bFD0258` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=0xF162fb13798A7B177d9d7fB0C923779c1bFD0258" width="130" height="130" alt="ETH QR"> |

> ⚠️ **Внимание:** отправляйте монеты **только в указанных сетях** — GRAM/USDT в сети **TON**, BTC в сети **BitCoin**, ETH в сети **Etherium**.
