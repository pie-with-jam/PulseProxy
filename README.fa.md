<p align="center">
  <a href="https://github.com/pie-with-jam/PulseProxy"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <img src="https://img.shields.io/github/last-commit/pie-with-jam/PulseProxy?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/pie-with-jam/PulseProxy?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/stars/pie-with-jam/PulseProxy?style=for-the-badge" alt="Stars">
</p>

<p align="center">
  <a href="./README.md">🇷🇺 Русский</a> · <a href="./README.en.md">🇬🇧 English</a> · <a href="./README.zh.md">🇨🇳 中文</a> · <b>🇮🇷 فارسی</b>
</p>

> 📌 این متن ترجمهٔ [README روسی](./README.md) (نسخهٔ اصلی) است. لینک‌های اشتراک یکسان و همیشه به‌روزند؛ ممکن است لینک‌های دانلود کلاینت در این ترجمه قدیمی باشند — برای نسخه‌های جدید به README روسی مراجعه کنید.

# 📖 توضیحات پروژه

مجموعه‌ای خودکار از کانفیگ‌های عمومی VPN (`V2Ray` / `VLESS` / `VMess` / `Trojan` / `Shadowsocks` / `Hysteria2` / `Tuic` / `Reality`) برای دور زدن محدودیت‌ها، شامل کانفیگ‌های دور زدن فهرست سفید SNI/CIDR و فهرست‌های کشوری برای چین و ایران.

هر کانفیگ یک اشتراک TXT است که تقریباً در هر کلاینت مدرنی می‌توان آن را وارد کرد (`v2rayNG`، `Throne`، `v2rayN`، `V2Box`، `Hiddify`، `Karing`، `Streisand` و غیره).

کانفیگ‌ها **به‌صورت خودکار هر ~30 دقیقه** (GitHub Actions + تریگر خارجی) به‌روزرسانی می‌شوند، **بررسی سلامت** (healthcheck) و **اعتبارسنجی ساختاری** را پشت سر می‌گذارند؛ بنابراین لینک‌های بخش **«📋 فهرست کلیه کانفیگ‌های همیشه به‌روز»** همیشه تازه‌اند.

## 📑 فهرست مطالب
- [🚀 شروع سریع](#-شروع-سریع)
- [📊 وضعیت کانفیگ‌ها](#-وضعیت-کانفیگها)
- [🔓 فایل شماره 30 — دور زدن فهرست سفید SNI/CIDR](#-فایل-شماره-30--دور-زدن-فهرست-سفید-snicidr)
- [🇨🇳🇮🇷 فایل‌های شماره 31 و 32 — برای چین و ایران](#-فایلهای-شماره-31-و-32--برای-چین-و-ایران)
- [⚙️ چگونه کار می‌کند](#️-چگونه-کار-میکند)
- [🗂 ساختار مخزن](#-ساختار-مخزن)
- [🔧 اجرای محلی ژنراتور](#-اجرای-محلی-ژنراتور)
- [📋 فهرست کلیه کانفیگ‌های همیشه به‌روز](#-فهرست-کلیه-کانفیگهای-همیشه-بهروز)
- [📷 کدهای QR](#-کدهای-qr)
- [🗂️ راهنماهای کلاینت‌ها](#️-راهنماهای-کلاینتها)
- [📱 مسیریابی v2rayNG برای اندروید](#-مسیریابی-v2rayng-برای-اندروید)
- [⚠️ رفع مشکلات رایج](#️-رفع-مشکلات-رایج)
- [⚠️ سلب مسئولیت](#️-سلب-مسئولیت)
- [🙏 قدردانی](#-قدردانی)
- [📜 مجوز](#-مجوز)

---

## 🚀 شروع سریع
1. لینک دلخواه را از بخش **«📋 فهرست کلیه کانفیگ‌های همیشه به‌روز»** کپی کنید.
2. آن را در **کلاینت VPN** خود وارد کنید (راهنماها در پایین).
3. تأخیر پروفایل‌ها را بررسی کنید، سروری با کمترین پینگ انتخاب کنید و متصل شوید.

> 💡 **برای اینترنت موبایل در روسیه** از فایل **[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** شروع کنید — این فهرستی گزینش‌شده بر اساس فهرست سفید SNI/CIDR است که بررسی سلامت را گذرانده است.
>
> 💡 **برای چین** — فایل **[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**، **برای ایران** — **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (بدون سرورهای داخل این کشورها).

---

## 📊 وضعیت کانفیگ‌ها

> **⚠️ توجه!** این جدول **منابع** و تعداد فعلی کانفیگ‌ها را نشان می‌دهد. **لینک‌ها را از اینجا کپی نکنید!** لینک‌های واردکردن در بخش **«📋 فهرست کلیه کانفیگ‌های همیشه به‌روز»** در پایین است.

| شماره | فایل | منبع | تعداد کانفیگ |
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
| 30 | [`30.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt) | **فایل ویژه: دور زدن فهرست سفید SNI/CIDR** (منابع 1–29 + `30_urls.json` + `storage.json`، healthcheck) | 1 094 |
| 31 | [`31.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt) | **برای چین** (بدون سرورهای داخل CN بر اساس `cn_cidr.txt`، healthcheck) | 977 |
| 32 | [`32.txt`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt) | **برای ایران** (بدون سرورهای داخل IR بر اساس `ir_cidr.txt`، healthcheck) | 945 |

> تعداد کانفیگ‌ها مربوط به تاریخ **13.10.2026** است و در هر چرخهٔ ساخت به‌روزرسانی می‌شود.

---

## 🔓 فایل شماره 30 — دور زدن فهرست سفید SNI/CIDR

**[30.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** — فایل ویژهٔ جداگانه برای کار از طریق فهرست سفید (اینترنت موبایل، «حالت بدون نظارت»):

- کاندیداها از فایل‌های **1–29** و منابع تکمیلی فهرست **`30_urls.json`** (اشتراک‌های دور زدن آماده) جمع‌آوری می‌شوند؛
- کانفیگ‌هایی که از **فهرست سفید CIDR/SNI** عبور نمی‌کنند کنار گذاشته می‌شوند (`cidrwhitelist.txt`، `sni_domains.json`)؛
- هر کانفیگ **اعتبارسنجی ساختاری** را پاس می‌کند: لینک‌های چسبیده `&amp;` → `&` ترمیم می‌شوند و آدرس‌های خراب (UUID نامعتبر، reality بدون `pbk`، Base64 خراب و غیره) حذف می‌شوند؛
- **healthcheck** (بررسی سلامت) انجام می‌شود — یک اتصال TCP/TLS برای هر کانفیگ؛
- ادغام با **`storage.json`** — کانفیگ‌های شخصی و تست‌شده.

> اگر کانفیگ‌های فایل‌های معمولی (1–29) از فهرست سفید عبور نمی‌کنند، حتماً از همان **30.txt** استفاده کنید.

### 🪞 آینه‌های روسی / راه‌های دور زدن برای اشتراک شماره 30 (حالت بدون نظارت)

اگر خود لینک `raw.githubusercontent.com` باز نمی‌شود (حالت فهرست سفید / حالت بدون نظارت) — از **لینک‌های پروکسی مترجم یاندکس** برای به‌روزرسانی اشتراک شماره 30 در کلاینت استفاده کنید:

1. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fraw.githack.com%2Fpie-with-jam%2FPulseProxy%2Frefs%2Fheads%2Fmain%2Fgithubmirror%2F30.txt&lang=de-de`
2. `https://translate.yandex.ru/translate?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpie-with-jam%2FPulseProxy%40main%2Fgithubmirror%2F30.txt&lang=de-de`

> ✦ این لینک‌ها دقیقاً محتوای `30.txt` را بازتولید می‌کنند و همراه با آن به‌روز می‌شوند — یکی از آن‌ها را به‌جای لینک معمولی در فیلد URL اشتراک قرار دهید.
>
> ✦ در واقع این ترکیبِ مشخص **Yandex +** (`raw.githack.com` / `cdn.jsdelivr.net`) است که کار می‌کند؛ ترکیب‌های دیگر با یاندکس ممکن است کانفیگ‌ها را خراب کنند.
>
> ✦ اگر لینک اول باز نشد، لینک دوم را امتحان کنید (و بالعکس). پس از به‌روزرسانی در کلاینت، دوباره متصل شوید.

---

## 🇨🇳🇮🇷 فایل‌های شماره 31 و 32 — برای چین و ایران

**[31.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)** و **[32.txt](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — اشتراک‌های کشوری برای کاربران پشت فایروال‌های ملی (چین، ایران):

- کاندیداها از فایل‌های **1–29** و `storage.json` جمع‌آوری می‌شوند (حذف تکراری‌ها و اعتبارسنجی ساختاری)؛
- **سرورهای داخل کشور حذف می‌شوند**: کانفیگ‌هایی که IP آن‌ها در `cn_cidr.txt` / `ir_cidr.txt` (8 802 / 1 901 زیرشبکه) است به‌صورت ایستا کنار گذاشته می‌شوند و دامنه‌ها هنگام healthcheck بر اساس IP واقعی اتصال بررسی می‌شوند — وصل‌شدن به سروری در همان کشور برای دور زدن محدودیت‌های همان کشور بی‌فایده است؛ **هنگ کنگ، ماکائو و تایوان** (`hk_cidr.txt` / `mo_cidr.txt` / `tw_cidr.txt`) از این حذف مستثنی هستند: بیرون از GFW قرار دارند و خروجی‌های نزدیک و مفید باقی می‌مانند؛
- **healthcheck** (بررسی سلامت) با دست‌دادن TCP/TLS و نمونه‌گیری یکنواخت تا 4 000 کاندیدا برای هر فایل انجام می‌شود (کل مجموعهٔ 1–29 برای بررسی کامل بزرگ است؛ سقف با `COUNTRY_PROBE_LIMIT` قابل تنظیم است).

> ⚠️ **مهم:** بررسی سلامت **از سرورهای GitHub Actions انجام می‌شود، نه از چین/ایران** — دیوار بزرگ (GFW) یا فیلتر ایران ممکن است بخشی از کانفیگ‌هایی را که همه‌جا کار می‌کنند مسدود کند. فایل، کاندیدای فیلترشده است، نه تضمین دسترسی‌پذیری داخل کشور؛ اگر در دسترس نبود، سرورهای بعدی فهرست را امتحان کنید.

> 🔒 **DoH (DNS over HTTPS) را فراموش نکنید:** دیوار بزرگ و فیلتر ایران DNS معمولی را آلوده می‌کنند. Remote DNS را روی `https://dns.google/dns-query` (گوگل) یا `https://cloudflare-dns.com/dns-query` (کلادفلر) بگذارید — در غیر این صورت دامنه‌ها پیش از اتصال به پروکسی جعل می‌شوند.

> 💡 این فایل‌ها همچنین برای کاربران این کشورها در بخش مسیریابی v2rayNG در پایین توصیه شده‌اند.

---

## ⚙️ چگونه کار می‌کند
1. **GitHub Actions** (`.github/workflows/auto_update.yml`) ساخت را **طبق برنامه هر ~30 دقیقه** (دقیقه‌های `:07` و `:37` هر ساعت به وقت UTC) اجرا می‌کند؛ علاوه بر آن، تریگر خارجی از سرور، workflow را در دقیقه‌های `:25` و `:55` فراخوانی می‌کند. اجرای دستی هم وجود دارد (`manual_update.yml`).
2. اسکریپت کانفیگ‌ها را به‌صورت موازی از **29 منبع عمومی** (`urls.json`) دانلود می‌کند و از ETag/If-Modified-Since استفاده می‌کند (دانلودهای مجدد بدون تغییر، ترافیک را هدر نمی‌دهند).
3. هر کانفیگ فیلتر می‌شود: Base64 رمزگشایی می‌شود، وجود پروتکل‌ها بررسی می‌شود (`vmess://`، `vless://`، `trojan://`، `ss://`، `hysteria2://`، `tuic://` و غیره)، کانفیگ‌های ناامن (`allowInsecure=1`) حذف می‌شوند، تکراری‌ها زدوده می‌شوند.
4. **فایل شماره 30** جداگانه ساخته می‌شود: جمع‌آوری کاندیداها از 1–29 + `30_urls.json` → فیلتر بر اساس فهرست‌های سفید CIDR/SNI → اعتبارسنجی ساختاری → healthcheck → ادغام با `storage.json`.
5. **فایل‌های شماره 31 (چین) و شماره 32 (ایران)** از 1–29 + `storage.json` ساخته می‌شوند → حذف سرورهای داخل کشور بر اساس CIDR (`cn_cidr.txt` / `ir_cidr.txt`) → اعتبارسنجی → healthcheck (نمونه‌گیری تا 4 000 کاندیدا).
6. **کدهای QR** (`qr-codes/1.png` … `32.png`) تولید می‌شوند — URL اشتراک را کد می‌کنند.
7. همهٔ تغییرات کامیت و پوش می‌شوند — لینک‌های README همیشه به‌روزند.

## 🗂 ساختار مخزن
```text
.github/workflows/   — CI/CD با GitHub Actions
 ├─ auto_update.yml     — به‌روزرسانی خودکار هر ~30 دقیقه طبق برنامه (+ workflow_dispatch)
 └─ manual_update.yml   — اجرای دستی ساخت
githubmirror/        — اشتراک‌های .txt تولیدشده (32 فایل)
qr-codes/            — کدهای QR اشتراک‌ها برای واردکردن (32 PNG)
source/              — کد منبع و پیکربندی‌های تولیدکننده
 ├─ main.py             — اسکریپت اصلی تولید
 ├─ requirements.txt    — وابستگی‌های Python
 ├─ config/
 │   ├─ urls.json           — 29 منبع عمومی (فایل‌های 1–29)
 │   ├─ 30_urls.json        — منابع فهرست سفید برای فایل ویژهٔ شماره 30
 │   ├─ storage.json        — کانفیگ‌های شخصی تست‌شده (در 30.txt ادغام می‌شوند)
 │   ├─ cidrwhitelist.txt   — فهرست سفید CIDR (برای دور زدن محدودیت‌ها)
 │   ├─ cn_cidr.txt         — شبکه‌های CIDR چین (برای فایل شماره 31)
 │   ├─ hk_cidr.txt         — شبکه‌های CIDR هنگ کنگ (مستثنی از شماره 31)
 │   ├─ mo_cidr.txt         — شبکه‌های CIDR ماکائو (مستثنی از شماره 31)
 │   ├─ tw_cidr.txt         — شبکه‌های CIDR تایوان (مستثنی از شماره 31)
 │   ├─ ir_cidr.txt         — شبکه‌های CIDR ایران (برای فایل شماره 32)
 │   └─ sni_domains.json    — فهرست سفید دامنه‌های SNI
 └─ src/
     ├─ __init__.py
     ├─ config.py           — مسیرها و بارگذاری پیکربندی
     ├─ file_manager.py     — دانلود، فیلترکردن، فهرست‌های سفید، ساخت فایل‌ها
     ├─ validator.py        — اعتبارسنجی ساختاری کانفیگ‌ها
     ├─ healthcheck.py      — بررسی سلامت (TCP/TLS)
     ├─ cidr.py             — کار با فهرست‌های CIDR
     ├─ parser.py           — فیلترکردن کانفیگ‌های ناامن
     ├─ network.py          — نشست HTTP با retry/ETag
     ├─ qr_generator.py     — تولید کدهای QR
     ├─ git_ops.py          — کامیت و پوش تغییرات
     ├─ github_api.py       — GitHub API
     ├─ readme_updater.py   — به‌روزرسانی خودکار README
     ├─ release_fetcher.py  — لینک‌های به‌روز دانلود کلاینت‌ها
     ├─ logger.py           — لاگ‌گیری
     └─ github_api.py       — آمار مخزن
 LICENSE               — مجوز GPL-3.0
 README.md             — همین فایل (روسی)
 README.en.md          — ترجمه انگلیسی
 README.zh.md          — ترجمه چینی ساده‌شده
 README.fa.md          — ترجمه فارسی (فارسی)
```

---

## 🔧 اجرای محلی ژنراتور

```bash
git clone https://github.com/pie-with-jam/PulseProxy.git
cd PulseProxy/source
python -m pip install -r requirements.txt
export MY_TOKEN=<GITHUB_TOKEN>   # توکن PAT با دسترسی contents:write برای پوش تغییرات
python main.py                   # کانفیگ‌ها در ../githubmirror ظاهر می‌شوند
```

> **مهم!** بدون `MY_TOKEN` هم تولید انجام می‌شود، اما کامیت/پوش تغییرات انجام نخواهد شد.

---

# 📋 فهرست کلیه کانفیگ‌های همیشه به‌روز

> فهرست‌های پیشنهادی: **[1](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/1.txt)**، **[6](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/6.txt)**، **[22](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/22.txt)**، **[23](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/23.txt)**، **[24](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/24.txt)** و **[25](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/25.txt)**.

> دور زدن فهرست سفید SNI/CIDR: **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)**.

> برای چین: **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**، برای ایران: **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** — بدون سرورهای داخل این کشورها.

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

> 🔗 [لینک کدهای QR کانفیگ‌های همیشه به‌روز](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes)

---

# 📷 کدهای QR

کدهای QR همهٔ اشتراک‌ها در پوشه [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) قرار دارند — `1.png` … `32.png`. QR **لینک اشتراک** را کد می‌کند، بنابراین برای واردکردن در کلاینت‌های موبایل و Android TV مناسب است (جایی که جای‌گذاری متنی لینک راحت نیست).

---

# 🗂️ راهنماهای کلاینت‌ها

<details>

<summary>📱 راهنمای اندروید (v2rayNG)</summary>

**1.** **«v2rayNG»** را دانلود می‌کنیم — [آخرین انتشار](https://github.com/2dust/v2rayNG/releases) (APK `arm64-v8a`).

**2.** لینک دلخواه را از بخش **«📋 فهرست کلیه کانفیگ‌های همیشه به‌روز»** کپی می‌کنیم.

**3.** وارد برنامه **«v2rayNG»** می‌شویم و در گوشهٔ بالا سمت راست روی ➕ می‌زنیم، سپس **«واردکردن از کلیپ‌بورد»** را انتخاب می‌کنیم.

**4.** روی **«سه نقطه»** در بالا سمت راست می‌زنیم → **«بررسی تأخیر پروفایل‌ها»**؛ پس از پایان، در همان منو **«مرتب‌سازی بر اساس نتایج تست»** را بزنید.

**5.** سرور دلخواه را انتخاب می‌کنیم و روی دکمهٔ ▶️ در گوشهٔ پایین سمت راست می‌زنیم.

**به‌روزرسانی کانفیگ‌ها:** منوی «سه خط» در بالا سمت چپ → **«گروه‌ها»** → آیکون «دایرهٔ فلش‌دار» در بالا سمت راست → صبر تا پایان به‌روزرسانی.

> 🧭 **نکته:** **مسیریابی** را تنظیم کنید (ترافیک ایران/چین/روسیه → مستقیم، بقیه → از طریق پراکسی) و **mux** و **فرگمنت** را غیرفعال کنید — بخش [«📱 مسیریابی v2rayNG برای اندروید»](#-مسیریابی-v2rayng-برای-اندروید) را ببینید.

</details>

<details>

<summary>📺 راهنمای Android TV</summary>

**1.** **«v2rayNG»** را دانلود می‌کنیم — [آخرین انتشار](https://github.com/2dust/v2rayNG/releases) (APK `armeabi-v7a`).

**2.** **کد QR** دلخواه را از پوشه [`qr-codes/`](https://github.com/pie-with-jam/PulseProxy/tree/main/qr-codes) دانلود می‌کنیم.

**3.** وارد **«v2rayNG»** می‌شویم → ➕ → **«واردکردن از کد QR»** → تصویر را انتخاب می‌کنیم (آیکون عکس در بالا سمت راست).

**4.** «سه نقطه» → **«بررسی تأخیر پروفایل‌ها»** → **«مرتب‌سازی بر اساس نتایج تست»**.

**5.** سرور را انتخاب می‌کنیم و ▶️ را می‌زنیم.

</details>

<details>

<summary>🖥 راهنمای ویندوز و لینوکس (Throne)</summary>

**1.** **«Throne»** را دانلود می‌کنیم — [آخرین انتشار](https://github.com/throneproj/Throne/releases) (`windows64` / `windowslegacy64` / `linux-amd64`).

**2.** لینک دلخواه را از بخش **«📋 فهرست کلیه...»** کپی می‌کنیم.

**3.** **«پروفایل‌ها»** → **«افزودن پروفایل از کلیپ‌بورد»**.

**4.** همهٔ کانفیگ‌ها را با **Ctrl+A** انتخاب می‌کنیم، سپس **«پروفایل‌ها»** → **«تست تأخیر (پینگ) پروفایل انتخاب‌شده»** و تا پایان صبر می‌کنیم (در «لاگ‌ها» پیام «تست تأخیر (پینگ) پایان یافت!» ظاهر می‌شود).

**5.** روی ستون **«تأخیر (پینگ)»** کلیک می‌کنیم — مرتب‌سازی انجام می‌شود.

**6.** در بالای پنجره گزینهٔ **«حالت TUN»** را روشن می‌کنیم (تیک‌خورده).

**7.** کانفیگی با کمترین پینگ را انتخاب می‌کنیم → **کلیک چپ** → **«اجرا»**.

**به‌روزرسانی کانفیگ‌ها:** «تنظیمات» → «گروه‌ها» → **«به‌روزرسانی همهٔ اشتراک‌ها»**.

</details>

<details>

<summary>☎ راهنمای iOS و iPadOS (V2Box)</summary>

**1.** **«V2Box - V2ray Client»** را دانلود می‌کنیم — [App Store](https://apps.apple.com/ru/app/v2box-v2ray-client/id6446814690).

**2.** لینک دلخواه را از بخش **«📋 فهرست کلیه...»** کپی می‌کنیم.

**3.** در برنامه به سربرگ **«Config»** می‌رویم → علامت + در بالا سمت راست → **«افزودن اشتراک»** → نام را وارد می‌کنیم و لینک را در فیلد **«URL»** می‌چسبانیم.

**4.** تا پایان بررسی صبر می‌کنیم، کانفیگ را با زدن روی نام انتخاب می‌کنیم.

**5.** در نوار پایین **«اتصال»** را می‌زنیم.

**به‌روزرسانی کانفیگ‌ها:** سربرگ «Config» → آیکون به‌روزرسانی سمت چپ نام گروه.

</details>

<details>

<summary>💻 راهنمای مک‌اواس (Hiddify)</summary>

**1.** **«Hiddify»** را دانلود می‌کنیم — [آخرین انتشار](https://github.com/hiddify/hiddify-app/releases) (`Hiddify-MacOS.dmg`).

**2.** **«پروفایل جدید»** را می‌زنیم → **«افزودن از کلیپ‌بورد»** (لینک را از بخش **«📋 فهرست کلیه...»** کپی می‌کنیم).

**3.** **«تنظیمات»** → **«گزینهٔ مسیریابی»** → منطقهٔ مناسب را انتخاب می‌کنیم.

**4.** آیکون تنظیمات در بالا سمت چپ → **«سرویس VPN»** → **«VPN»** را روشن می‌کنیم (آیکون وسطی).

**5.** برای عوض‌کردن سرور: سربرگ **«پراکسی»**.

**به‌روزرسانی کانفیگ‌ها:** پروفایل را انتخاب کنید → آیکون به‌روزرسانی سمت چپ نام.

</details>

---

# 📱 مسیریابی v2rayNG برای اندروید

برای اندروید **[v2rayNG](https://github.com/2dust/v2rayNG/releases)** را همراه با **قواعد مسیریابی** توصیه می‌کنیم: ترافیک محلی (ایرانی، چینی، روسی) و «خودی» **مستقیم** می‌رود و فقط آنچه واقعاً به دورزدن نیاز دارد از پراکسی عبور می‌کند. این‌طوری پایدارتر و سریع‌تر است و فشار روی پراکسی کمتر می‌شود.

### 🧭 فایل مسیریابی آماده

**[`routing/v2rayng-routing.json`](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/routing/v2rayng-routing.json)** — قواعدی برای واردکردن در v2rayNG (اولین تطبیق برنده است):

- **مستقیم (direct):**
  - شبکهٔ محلی (LAN)؛
  - **ایران** (`geoip:ir` + پسوند `domain:ir`)، **چین** (`geoip:cn` / `geosite:cn`)، **روسیه** (`geoip:ru` + پسوندهای `domain:ru` / `domain:su`)؛
  - DNSهای عمومی چین و روسیه (AliDNS، DNSPod، یاندکس، SafeDNS)؛
  - سرویس‌های تشخیص IP و نشت DNS — **ipify.org, 2ip.io, icanhazip.com, ifconfig.me, ipleak.net, dnsleaktest.com** و غیره (تا IP **واقعی** را ببینید)؛
  - فروشگاه‌های برنامه — **F-Droid, Huawei, Xiaomi**, Samsung, Amazon (دانلودهای سنگین از پراکسی عبور داده نمی‌شوند).
- **مسدودسازی:** QUIC (`UDP 443`) — ترافیک به‌زور به TCP فرستاده می‌شود که به دورزدن DPI کمک می‌کند (اغلب در ایران/روسیه).
- **بقیهٔ موارد → از طریق پراکسی** (رفتار پیش‌فرض — چیز اضافه‌ای لازم نیست تنظیم کنید).

**واردکردن:** محتوای JSON را کپی کنید → در v2rayNG «سه خط» سمت چپ → **«تنظیمات»** → **«Routing»** → **«⋮»** → **«واردکردن از کلیپ‌بورد»**. ترتیب قواعد مهم است — آن‌ها را جابه‌جا نکنید و بلوک `geoip:private` را حذف نکنید.

> ✅ **پایداری در نسخه‌های پایدار v2rayNG:** این فایل فقط از دسته‌هایی استفاده می‌کند که واقعاً در `geosite.dat` استاندارد وجود دارند (`geosite:private`، `geosite:cn`) به‌علاوهٔ پسوندهای TLD یعنی `domain:ir` / `domain:ru`. دسته‌های `geosite:ir` و `geosite:ru` در `geosite.dat` استاندارد **وجود ندارند** — هر قانونی که به آن‌ها اشاره کند کانفیگ را با خطا می‌شکند: `code not found in geosite.dat: IR`. اگر پس از واردکردن قواعد شخصی یا قدیمی این خطا را دیدید — قواعد `geosite:ir` / `geosite:ru` را حذف کنید یا فایل ما را دوباره وارد کنید (به‌روزرسانی Geo-فایل‌ها کمکی نمی‌کند — این دسته‌ها در هیچ‌یک از بیلدهای استاندارد نیستند).

> ⚠️ **مهم: همهٔ قواعد مسیریابی را فعال کنید (`enabled: true`)، فارغ از اینکه کجا زندگی می‌کنید.** قواعد «مربوط به کشورهای دیگر» را غیرفعال نکنید — آن‌ها مزاحمتی ایجاد نمی‌کنند و فقط ترافیک لازم را از کنار پراکسی عبور می‌دهند (مثلاً می‌توانید در روسیه زندگی کنید ولی قواعد ایران/چین را فعال نگه دارید).

### ⚙️ تنظیمات پیشنهادی کلاینت

- **اشتراک:** از **چین** — فایل **[31](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/31.txt)**، از **ایران** — فایل **[32](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/32.txt)** (بدون سرورهای داخل این کشورها)؛ از روسیه با فایل **[30](https://github.com/pie-with-jam/PulseProxy/raw/refs/heads/main/githubmirror/30.txt)** شروع کنید.
- **Mux** — **خاموش** (تنظیمات → Mux → disable). Mux اغلب TLS و سایت‌ها را خراب می‌کند.
- **فرگمنت (fragment)** — **خاموش**. فقط وقتی سایتی خاص بر اساس SNI بریده می‌شود، به‌صورت هدفمند روشن کنید.
- **Remote DNS:** برای فهرست سفید (فایل **30**) — DNS ارائه‌دهنده یا یاندکس؛ برای حالت معمولی — DoH: `https://dns.google/dns-query` (گوگل) یا `https://cloudflare-dns.com/dns-query` (کلادفلر).
- **استراتژی دامنه** («تنظیمات» → «Routing» → «Domain Strategy») — **`IPIfNonMatch`**: قواعد دامنه فوراً برخورد می‌کنند و قواعد `geoip` فقط برای دامنه‌هایی بررسی می‌شوند که به هیچ قانونی نخورده‌اند. `AsIs` (پیش‌فرض) را نگذارید — با آن `geoip:ir` / `geoip:cn` / `geoip:ru` دامنه‌ها را نمی‌گیرند و ترافیک محلی از پراکسی می‌رود؛ `IPOnDemand` هم بی‌جهت هر اتصال را resolve می‌کند. توجه: `IPIfNonMatch` دامنه‌های بدون تطبیق را resolve می‌کند، پس Remote DNS باید DoH باشد (بالا را ببینید).

---

# ⚠️ رفع مشکلات رایج

<details>

<summary>⚠ گیرکردن «بررسی تأخیر پروفایل‌ها» در v2rayNG (بررسی تا N رسید و «گیر کرد»)</summary>

کانفیگ‌های عمومی زیادند (گاهی هزاران عدد) و تست واقعی اتصال برای هرکدام خیلی طول می‌کشد.

**1.** **v2rayNG** را به آخرین نسخه به‌روز کنید — [انتشارها](https://github.com/2dust/v2rayNG/releases).

**2.** در منوی بررسی، نوع تست را از **REALITY/HTTP** به **TCP ping** تغییر دهید — TCP پینگ آنی بررسی می‌شود و کانفیگ «آویزان» نمی‌ماند.

**3.** یا منتظر بررسی کامل نمانید: اشتراک را وارد کنید، تا ظاهرشدن کانفیگ‌ها صبر کنید و به مورد دلخواه وصل شوید — بررسی ضروری نیست.

</details>

<details>

<summary>⚠ ظاهرنشدن کانفیگ‌ها هنگام افزودن اشتراک در v2rayNG</summary>

**1.** روی **«سه خط»** در گوشهٔ بالا سمت چپ بزنید.

**2.** **«گروه‌ها»** را باز می‌کنیم.

**3.** روی **«دایرهٔ فلش‌دار»** در بالا سمت راست می‌زنیم و تا پایان به‌روزرسانی صبر می‌کنیم.

</details>

<details>

<summary>⚠ نبود اینترنت هنگام اتصال به VPN</summary>

**1.** کانفیگ دیگری از اشتراک را امتحان کنید (VPN را خاموش و روشن کنید یا سروری با پینگ کمتر انتخاب کنید).

**2.** اگر پینگ موفق است ولی ترافیکی نیست — **Remote DNS** را در کلاینت به DoH تغییر دهید، مثلاً `https://dns.google/dns-query` (گوگل) یا `https://cloudflare-dns.com/dns-query` (کلادفلر) (در v2rayNG: «تنظیمات» → «تنظیمات DNS» → «Basic DNS Settings»).

**3.** برای فهرست سفید (فایل 30) از DNS ارائه‌دهنده (یا یاندکس) استفاده کنید — DNSهای خارجی در حالت فهرست سفید کار نمی‌کنند.

</details>

<details>

<summary>⚠ خطاهای «net/http: 12x handshake timeout» و «io: read/write closed pipe»</summary>

**1.** در دسکتاپ، روی آیکون **«v2rayNG»** کلیک طولانی کنید → **«درباره برنامه»**.

**2.** **«توقف»** را بزنید و برنامه را دوباره اجرا کنید.

**3.** اشتراک را به‌روز کنید (گروه‌ها → ⟳) و دوباره متصل شوید.

</details>

<details>

<summary>⚠ خطای MSVCP/VCRUNTIME در Throne روی ویندوز</summary>

**1.** **Win+R** → `control` → **«برنامه‌ها و ویژگی‌ها»**.

**2.** در جستجوی سمت راست **«Visual»** را بنویسید و همهٔ مؤلفه‌های **«Microsoft Visual C++»** را حذف کنید.

**3.** بستهٔ **Visual C++ Runtimes All-in-One** را دانلود و استخراج کنید.

**4.** `install_bat.all` را **با دسترسی مدیر** اجرا کنید و تا پایان نصب صبر کنید.

</details>

---

# ⚠️ سلب مسئولیت

**با استفاده از این مخزن و پیکربندی‌های آن، کلیهٔ مسئولیت استفاده از آن‌ها را بر عهده می‌گیرید.**

- نویسنده در قبال هیچ پیامدی از استفاده از پیکربندی‌های منتشرشده **مسئولیتی ندارد**: این شامل کارکرد، امنیت و احتمال محدودیت‌های از سوی ارائه‌دهندهٔ اینترنت یا سایر سازمان‌ها می‌شود.
- همهٔ پیکربندی‌ها جزئیاً **عمومی** هستند — اشخاص ثالث آن‌ها را قرار می‌دهند و به‌روز می‌کنند؛ نویسندهٔ پروژه فقط آن‌ها را جمع‌آوری، فیلتر و به شکلی راحت منتشر می‌کند و نسبت به محتوا، در دسترس‌بودن و کارکرد پیوستهٔ آن‌ها تضمینی نمی‌دهد.
- پروژه **غیرتجاری و به‌صورت «as is» (بدون تضمین)** ساخته شده: هیچ ضمانتی داده نمی‌شود و هیچ مسئولیتی در قبال زیان‌ها، اختلال‌ها، مسدودسازی‌ها یا پیامدهای دیگر پذیرفته نمی‌شود.
- شما موظفید خودتان ریسک‌ها را ارزیابی کنید و قوانین کشور خود را رعایت کنید.

---

# 🙏 قدردانی

ایدهٔ پایه، ساختار و کد منبع این پروژه از **[AvenCores / goida-vpn-configs](https://gitlab.com/avencores/goida-vpn-configs)** گرفته شده است — **از AvenCores، نویسندهٔ آن، بابت زحماتش صمیمانه سپاسگزارم!** ❤️

همچنین از نگهدارندهٔ [LalatinaHub/Mineral](https://github.com/LalatinaHub/Mineral) (منبع شماره 14 در جدول) سپاسگزاریم: به [issue #6](https://github.com/LalatinaHub/Mineral/issues/6) ما دربارهٔ از کار افتادن workflow زمان‌بندی‌شده فردای همان روز پاسخ دادند و پوش به main را درست کردند. در میان 29 منبع بیگانه، تعداد انگشت‌شماری پاسخ می‌دهند.

PulseProxy فورکی با بهبودهاست: healthcheck، اعتبارسنجی ساختاری کانفیگ‌ها، فایل ویژهٔ شماره 30 با فهرست‌های سفید SNI/CIDR، کانفیگ‌های اختصاصی (`storage.json`) و به‌روزرسانی هر ~30 دقیقه از طریق GitHub Actions به آن افزوده شده است.

---

# 📜 مجوز

پروژه تحت مجوز **GPL-3.0** توزیع می‌شود. متن کامل مجوز در فایل [`LICENSE`](LICENSE) آمده است.

---

<!-- 💰 حمایت از نویسنده -->

اگر پروژه برایتان مفید بود، می‌توانید از توسعهٔ آن حمایت کنید:

| شبکه / رمزارز | آدرس انتقال | کد QR |
| :--- | :--- | :---: |
| **GRAM (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="GRAM TON QR"> |
| **USDT (TON)** | `UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=UQBcrOMKtoHYBhg0UtzoLCQobvO15Av-c8ICnLeHIwBV75ie" width="130" height="130" alt="USDT TON QR"> |
| **BTC (BitCoin network)** | `bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=bc1q656qrnfhe0f7wcwzdmk8zsva34s9fwhhsledwz" width="130" height="130" alt="BTC QR"> |
| **ETH (Etherium)** | `0xF162fb13798A7B177d9d7fB0C923779c1bFD0258` | <img src="https://api.qrserver.com/v1/create-qr-code/?size=130x130&data=0xF162fb13798A7B177d9d7fB0C923779c1bFD0258" width="130" height="130" alt="ETH QR"> |

> ⚠️ **توجه:** رمزارزها را **فقط در شبکه‌های مشخص‌شده** بفرستید — GRAM/USDT در شبکهٔ **TON**، BTC در شبکهٔ **BitCoin**، ETH در شبکهٔ **Etherium**.
