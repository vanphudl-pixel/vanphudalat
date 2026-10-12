"""Build the whole multilingual site (home, routes, blog + 5 articles per language)
from content/<lang>.py. Output: /home/claude/site"""
import importlib, json, re, shutil, sys
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
BASE = "https://vanphudalat.com/"
OUT = HERE.parent  # repo root = published site
LANGS = ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he"]
LABEL = {"en": "EN", "ru": "RU", "zh": "中文", "ko": "한국어", "ja": "日本語", "th": "ไทย", "id": "ID", "ms": "MY", "vi": "VI", "de": "DE", "fr": "FR", "es": "ES", "he": "עב"}
LOCALE = {"en": "en_US", "ru": "ru_RU", "zh": "zh_CN", "ko": "ko_KR", "ja": "ja_JP", "th": "th_TH", "id": "id_ID", "ms": "ms_MY", "vi": "vi_VN", "de": "de_DE", "fr": "fr_FR", "es": "es_ES", "he": "he_IL"}
LAT, LON = 11.9510676, 108.4384077
GMAPS = "https://maps.app.goo.gl/ULvgaZFh4Q1kjTCe6"
YA_LINK = f"https://yandex.ru/maps/?pt={LON},{LAT}&z=17&l=map"
AMAP = f"https://uri.amap.com/marker?position={LON},{LAT}&name=Van%20Phu%20%E5%A4%A7%E5%8F%BB%E6%91%A9%E6%89%98%E8%BD%A6%E7%A7%9F%E8%B5%81&src=vanphudalat&coordinate=wgs84&callnative=1"
YA_WIDGET = f"https://yandex.ru/map-widget/v1/?ll={LON}%2C{LAT}&z=16&pt={LON}%2C{LAT}%2Cpm2rdm"
TG = "https://t.me/vanphudalat"
TG_CHANNEL = "https://t.me/dalat_life_vietnam"
ZALO = "https://zalo.me/0944081101"
WA2 = "https://wa.me/84834662149"

C = {l: importlib.import_module(f"content.{l}").C for l in LANGS}

TPL = (HERE / "template.html").read_text(encoding="utf-8")
# article order = order in content/en.py (oldest first); every language must have every key
ARTICLES = list(C["en"]["articles"].keys())
DATES = C["en"].get("dates", {})
def adate(k): return DATES.get(k, "2026-10-10")
CSS = re.search(r"<style>(.*?)</style>", TPL, re.S).group(1) + """
.lead{font-size:17px}
.langs a{border:1px solid rgba(255,255,255,.5);color:#fff;border-radius:6px;padding:4px 8px;font-size:13px;text-decoration:none}
.langs a.on{background:#fff;color:var(--brand)}
table.price{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.price th,table.price td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line)}
table.price th{background:var(--brand2);font-size:14px}
table.price tr:last-child td{border-bottom:0}
.note{color:var(--muted);font-size:14px;margin-top:8px}
.checks{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.checks li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px 12px 40px;position:relative}
.checks li:before{content:"✓";position:absolute;left:14px;top:11px;color:var(--brand);font-weight:700}
.prose p{margin:0 0 12px}
.prose ul{padding-left:20px}
.prose li{margin-bottom:6px}
.crumbs{font-size:13px;opacity:.9;margin-bottom:8px}
.crumbs a{color:#fff}
.route{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:12px}
.route h3{margin:0 0 6px;font-size:18px}
.route .meta{font-size:13px;color:var(--muted);margin-bottom:8px}
.route p{margin:0 0 8px}
.cta-box{background:var(--brand);color:#fff;border-radius:14px;padding:20px;margin-top:8px}
.cta-box h2{color:#fff}
.cta-box p{margin:0 0 14px}
.rules{display:grid;gap:10px}
.rule{display:flex;align-items:center;gap:12px;background:#fff4e5;border:1px solid #f2c98a;border-radius:12px;padding:14px 16px}
.rule .ic{font-size:24px;flex:none}
.box{background:#e8f5fc;border:1px solid #9fd4ef;border-radius:14px;padding:18px;margin:8px 0 18px}
.box h2{font-size:19px;margin:0 0 6px}
.box p{margin:0 0 12px}
.posts{display:grid;gap:12px}
.post{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;text-decoration:none;color:var(--ink)}
.post b{display:block;font-size:17px;margin-bottom:4px;color:var(--brand)}
.post span{color:var(--muted);font-size:14px}
.tg{background:#229ED9;color:#fff}
.zalo{background:#0068FF;color:#fff}
.wechat{background:#07C160;color:#fff}
.float.f2{bottom:74px}
.float.tgf{background:#229ED9}
.float.zf{background:#0068FF}
html:lang(ko) h1,html:lang(ko) h2{word-break:keep-all}
html[dir=rtl] .checks li{padding:12px 40px 12px 14px}
html[dir=rtl] .checks li:before{left:auto;right:14px}
html[dir=rtl] ol{padding-left:0;padding-right:20px}
html[dir=rtl] .prose ul{padding-left:0;padding-right:20px}
html[dir=rtl] .langs,html[dir=rtl] .price,html[dir=rtl] table.price th,html[dir=rtl] table.price td{text-align:right}
"""

# ------------------------------------------------------------------ URLs
def home_path(l): return "" if l == "en" else f"{l}/"
def routes_path(l): return home_path(l) + C[l]["routes"]["slug"] + "/"
def blog_path(l): return home_path(l) + "blog/"
def art_path(l, k): return blog_path(l) + C[l]["articles"][k][0] + "/"

def path_of(l, kind, key=None):
    return {"home": home_path, "routes": routes_path, "blog": blog_path}[kind](l) if kind != "art" else art_path(l, key)

def rel(frm, to):
    """relative link from page path `frm` to page path `to` (both like 'ru/blog/x/')."""
    depth = frm.count("/")
    r = "../" * depth + to
    return r or "./"

# ------------------------------------------------------------------ pieces
def wa_link(l):
    return "https://wa.me/84944081101?text=" + quote(C[l]["ui"]["wa_text"])

def btn(kind, l, cls_extra=""):
    u = C[l]["ui"]
    if kind == "wa": return f'<a class="btn wa" href="{wa_link(l)}" target="_blank" rel="noopener">{u["book_wa"]}</a>'
    if kind == "tg": return f'<a class="btn tg" href="{TG}" target="_blank" rel="noopener">{u["tg_btn"]}</a>'
    if kind == "zalo": return f'<a class="btn zalo" href="{ZALO}" target="_blank" rel="noopener">{u["zalo_btn"]}</a>'
    if kind == "wc": return '<button class="btn wechat wcbtn" type="button">WeChat: vanphudalat</button>'
    if kind == "gmap": return f'<a class="btn alt" href="{GMAPS}" target="_blank" rel="noopener">{u["open_map"]}</a>'
    if kind == "amap": return f'<a class="btn alt" href="{AMAP}" target="_blank" rel="noopener">在高德地图中打开</a>'
    if kind == "yamap": return f'<a class="btn alt" href="{YA_LINK}" target="_blank" rel="noopener">Открыть в Яндекс Картах</a>'
    raise KeyError(kind)

HERO = {"ru": ["tg", "wa", "yamap", "wc"], "zh": ["wc", "wa", "amap", "gmap"], "vi": ["zalo", "wa", "gmap"]}
def hero_btns(l): return "\n".join(btn(k, l) for k in HERO.get(l, ["wa", "gmap"]))

def floats(l):
    if l == "ru":
        return f'<a class="float f2 tgf" href="{TG}" target="_blank" rel="noopener">Telegram</a>\n<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'
    if l == "vi":
        return f'<a class="float f2 zf" href="{ZALO}" target="_blank" rel="noopener">Zalo</a>\n<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'
    return f'<a class="float" href="{wa_link(l)}" target="_blank" rel="noopener">WhatsApp</a>'

def contact_box(l):
    u = C[l]["ui"]
    if l == "ru":
        b = f'<a class="btn tg" href="{TG_CHANNEL}" target="_blank" rel="noopener">{u["box_btn"]}</a>'
    elif l == "zh":
        b = ('<img src="/img/wechat-qr.png" alt="微信二维码 vanphudalat — 大叻租摩托车" width="280" height="375" '
             'style="display:block;max-width:280px;width:100%;height:auto;border-radius:12px;margin:0 0 12px;background:#fff">'
             + btn("wc", l))
    elif l == "vi":
        b = btn("zalo", l)
    else:
        b = f'<a class="btn wa" href="{wa_link(l)}" target="_blank" rel="noopener">{u["box_btn"]}</a>'
    return f'<div class="box"><h2>{u["box_title"]}</h2><p>{u["box_text"]}</p>{b}</div>'

def cta_box(l, frm):
    u = C[l]["ui"]
    first = {"ru": "tg", "vi": "zalo", "zh": "wc"}.get(l)
    btns = (btn(first, l) + "\n" if first else "") + btn("wa", l)
    return f"""<div class="cta-box"><h2>{u["cta_title"]}</h2><p>{u["cta_text"]}</p>
<div class="cta">{btns}
<a class="btn alt" href="{rel(frm, home_path(l))}">{u["cta_prices"]}</a></div></div>"""

def contacts(l):
    h = C[l]["home"]
    rows = [f'<p><b>WhatsApp:</b> <a href="{wa_link(l)}">+84 944 081 101</a> · <a href="{WA2}">+84 834 622 149</a></p>',
            f'<p><b>Zalo:</b> <a href="{ZALO}">0944 081 101</a></p>',
            f'<p><b>Telegram:</b> <a href="{TG}">@vanphudalat</a></p>']
    if l == "ru":
        rows.append(f'<p><b>Telegram-канал:</b> <a href="{TG_CHANNEL}">@dalat_life_vietnam</a></p>')
    rows += ['<p><b>WeChat:</b> vanphudalat</p>',
             '<p><b>Facebook:</b> <a href="https://www.facebook.com/vanphudalat">facebook.com/vanphudalat</a></p>',
             f'<p><b>{h["addr_label"]}</b> {h["address"]}</p>']
    return '<div class="contact">' + "\n".join(rows) + "</div>"

def langbar(l, kind, key, frm):
    out = ""
    for x in LANGS:
        cls = ' class="on" aria-current="page"' if x == l else ""
        out += f'<a href="{rel(frm, path_of(x, kind, key))}" hreflang="{x}" data-l="{x}"{cls}>{LABEL[x]}</a>'
    return f'<div class="top"><div class="logo">Văn Phú Đà Lạt</div><div class="langs">{out}</div></div>'

def ldjson(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>"

def head(l, kind, key, title, desc, ld, img="electric-row"):
    me = path_of(l, kind, key)
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{BASE + path_of(x, kind, key)}">\n' for x in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE + path_of("en", kind, key)}">\n'
    return f"""<!doctype html>
<html lang="{l}"{' dir="rtl"' if l == "he" else ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE + me}">
{alts}<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[l]}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE + me}">
<meta property="og:image" content="{BASE}img/{img}.jpg">
{"".join(ldjson(x) for x in ld)}
<style>{CSS}</style>
</head>
<body>"""

def foot(l, root_redirect=False):
    u = C[l]["ui"]
    redirect = ""
    if root_redirect:
        redirect = ("(function(){if(/bot|crawl|spider|slurp|yandex|google|bing|baidu/i.test(navigator.userAgent))return;let p=null;try{p=localStorage.getItem('lang')}catch(e){}"
                    "const ok=" + json.dumps(LANGS) + ";let t=p;if(!t){const ls=navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'en'];"
                    "for(const x of ls){let n=x.toLowerCase().slice(0,2);if(n==='in')n='id';if(n==='iw')n='he';if(ok.includes(n)){t=n;break}}}"
                    "if(t&&t!=='en'&&ok.includes(t))location.replace(t+'/');})();")
    return f"""<footer>{u["footer"]}</footer>
{floats(l)}
<div class="lb" id="lb"><img alt=""></div>
<script>
document.querySelectorAll('.langs a').forEach(a=>a.addEventListener('click',()=>{{try{{localStorage.setItem('lang',a.dataset.l)}}catch(e){{}}}}));
document.querySelectorAll('.wcbtn').forEach(b=>b.onclick=()=>{{try{{navigator.clipboard.writeText('vanphudalat')}}catch(e){{}};b.textContent={json.dumps(u["copied"], ensure_ascii=False)};setTimeout(()=>b.textContent='WeChat: vanphudalat',2000)}});
const lb=document.getElementById('lb');document.querySelectorAll('.gallery img').forEach(i=>i.onclick=()=>{{lb.querySelector('img').src=i.src;lb.classList.add('on')}});lb.onclick=()=>lb.classList.remove('on');
{redirect}
</script>
</body>
</html>
"""

def business_ld(l, url):
    h, u = C[l]["home"], C[l]["ui"]
    return {"@context": "https://schema.org", "@type": ["LocalBusiness", "AutoRental"], "@id": BASE + "#business",
            "name": "Van Phu Dalat Motorbike Rental", "alternateName": ["Thuê xe máy Đà Lạt Văn Phú", "Văn Phú Đà Lạt", "Dalat Motorbike Rental"],
            "areaServed": {"@type": "City", "name": "Da Lat", "alternateName": ["Đà Lạt", "Dalat"]},
            "currenciesAccepted": "VND",
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "opens": "04:30", "closes": "21:00"}],
            "knowsAbout": ["motorbike rental", "scooter rental", "electric scooter rental", "Da Lat motorbike routes"],
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in
                               ["Free helmet", "Phone holder", "1 liter of fuel (gas scooters)", "Free hotel delivery in central Da Lat (2+ days)", "No cash deposit (passport or ID held)"]],
            "description": h["desc"], "url": url, "image": BASE + "img/electric-row.jpg",
            "telephone": "+84944081101", "priceRange": "150,000 VND",
            "address": {"@type": "PostalAddress", "streetAddress": "1/15/5 Thông Thiên Học", "addressLocality": "Đà Lạt", "addressCountry": "VN"},
            "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON}, "hasMap": GMAPS,
            "sameAs": ["https://www.facebook.com/vanphudalat", "https://www.tiktok.com/@bietthudalat", TG, ZALO],
            "makesOffer": [{"@type": "Offer", "name": n, "price": "150000", "priceCurrency": "VND"}
                           for n in ["Honda Vision 110", "Honda Air Blade 125", h["electric_name"]]]}

def posts(l, frm, keys):
    a = C[l]["articles"]
    return '<div class="posts">' + "".join(
        f'<a class="post" href="{rel(frm, art_path(l, k))}"><b>{a[k][2]}</b><span>{a[k][3]}</span></a>' for k in keys) + "</div>"

# ------------------------------------------------------------------ pages
def page_home(l):
    h, u = C[l]["home"], C[l]["ui"]
    me = home_path(l)
    pre = rel(me, "")
    if pre == "./": pre = ""
    url = BASE + me
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in h["faq"]]}
    alt = u["alt"]
    conds = "".join(f"<li><b>{b}</b> — {t}</li>" for b, t in h["conditions"])
    steps = "".join(f"<li>{s}</li>" for s in h["steps"])
    rules = "".join(f'<div class="rule"><span class="ic">{ic}</span><b>{r}</b></div>' for ic, r in zip(["🚫🍺", "🚦"], h["rules"]))
    why = "".join(f"<p>{p}</p>" for p in h["why"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in h["faq"])
    if l == "ru":
        mp = f'<iframe class="map" src="{YA_WIDGET}" loading="lazy" title="Яндекс Карты" allowfullscreen></iframe><p class="note"><a href="{YA_LINK}" target="_blank" rel="noopener">Яндекс Карты</a> · <a href="{GMAPS}" target="_blank" rel="noopener">Google Maps</a></p>'
    else:
        mp = f'<iframe class="map" src="https://maps.google.com/maps?q={LAT},{LON}&hl={l}&z=17&output=embed" loading="lazy" title="Google Maps"></iframe><p class="note"><a href="{GMAPS}" target="_blank" rel="noopener">Google Maps</a>' + (f' · <a href="{AMAP}" target="_blank" rel="noopener">高德地图</a>' if l == "zh" else "") + '</p>'
    imgs = [("electric-row", 1), ("airblade", 2), ("electric-helmets", 3), ("fleet-gas", 4), ("vision-white", 5), ("guest-1", 6), ("guest-2", 7)]
    gallery = "".join(f'<img src="{pre}img/{n}.jpg" alt="{alt} {i}" loading="lazy">' for n, i in imgs)
    body = f"""
<header><div class="wrap">{langbar(l, "home", None, me)}
<div class="hero">
 <h1>{h["h1"]}</h1>
 <p class="lead">{h["lead"]}</p>
 <div class="price">{h["price_badge"]}</div>
 <div class="cta">{hero_btns(l)}</div>
 <img class="heroimg" src="{pre}img/electric-row.jpg" alt="{alt}" width="1200" height="675">
</div></div></header>
<main class="wrap">
 <section><h2>{h["h_prices"]}</h2>
  <table class="price"><tr><th>{h["th_bike"]}</th><th>{h["th_price"]}</th></tr>
  <tr><td>Honda Vision 110</td><td><b>{h.get("price_cell", "150,000 ₫")}</b></td></tr>
  <tr><td>Honda Air Blade 125</td><td><b>{h.get("price_cell", "150,000 ₫")}</b></td></tr>
  <tr><td>{h["electric_name"]}</td><td><b>{h.get("price_cell", "150,000 ₫")}</b></td></tr></table>
  <p class="note">{h["price_note"]}</p></section>
 <section><h2>{h["h_conditions"]}</h2><ul class="checks">{conds}</ul></section>
 <section><h2>{h["h_fleet"]}</h2><div class="grid">
  <div class="card"><img src="{pre}img/vision-white.jpg" alt="Honda Vision 110 — {alt}" loading="lazy"><b>Honda Vision 110</b><span>{h["vision"]}</span></div>
  <div class="card"><img src="{pre}img/airblade.jpg" alt="Honda Air Blade 125 — {alt}" loading="lazy"><b>Honda Air Blade 125</b><span>{h["airblade"]}</span></div>
  <div class="card"><img src="{pre}img/electric-helmets.jpg" alt="{h["electric_name"]} — {alt}" loading="lazy"><b>{h["electric_name"]}</b><span>{h["electric"]}</span></div>
 </div></section>
 <section><h2>{h["h_how"]}</h2><ol>{steps}</ol></section>
 <section><h2>{h["h_rules"]}</h2><div class="rules">{rules}</div></section>
 <section class="prose"><h2>{h["h_why"]}</h2>{why}
  <p><a class="btn alt" href="{rel(me, routes_path(l))}" style="border:1px solid var(--line)">{h["routes_btn"]}</a></p></section>
 <section><h2>{h["h_photos"]}</h2><div class="gallery">{gallery}</div></section>
 <section class="faq"><h2>{h["h_faq"]}</h2>{faq}</section>
 <section><h2>{u["blog_h"]}</h2>{posts(l, me, ARTICLES[::-1][:6])}</section>
 <section><h2>{h["h_map"]}</h2>{mp}</section>
 <section>{contact_box(l)}</section>
 <section><h2>{h["h_contacts"]}</h2>{contacts(l)}</section>
</main>
"""
    return head(l, "home", None, h["title"], h["desc"], [business_ld(l, url), faq_ld]) + body + foot(l, root_redirect=(l == "en"))

def crumbs(l, me, items):
    u = C[l]["ui"]
    parts = [f'<a href="{rel(me, home_path(l))}">{u["crumbs_home"]}</a>']
    for name, path in items:
        parts.append(f'<a href="{rel(me, path)}">{name}</a>' if path else name)
    return '<div class="crumbs">' + " › ".join(parts) + "</div>"

def crumbs_ld(l, items):
    u = C[l]["ui"]
    el = [{"@type": "ListItem", "position": 1, "name": u["crumbs_home"], "item": BASE + home_path(l)}]
    for i, (n, p) in enumerate(items, 2):
        el.append({"@type": "ListItem", "position": i, "name": n, "item": BASE + p})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}

def page_routes(l):
    r, u = C[l]["routes"], C[l]["ui"]
    me = routes_path(l)
    items = "".join(f'<div class="route"><h3>{i}. {t}</h3><div class="meta">{m}</div><p>{d}</p><p><i>{tip}</i></p></div>'
                    for i, (t, m, d, tip) in enumerate(r["items"], 1))
    tips = "".join(f"<li>{t}</li>" for t in r["tips"])
    art = {"@context": "https://schema.org", "@type": "Article", "headline": r["h1"], "inLanguage": l, "mainEntityOfPage": BASE + me,
           "image": BASE + "img/airblade.jpg", "datePublished": "2026-10-10",
           "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}}
    body = f"""
<header><div class="wrap">{langbar(l, "routes", None, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_routes"], None)])}
 <h1>{r["h1"]}</h1><p class="lead">{r["lead"]}</p>
 <div class="cta">{hero_btns(l)}</div>
</div></div></header>
<main class="wrap">
 <section><h2>{r["h_list"]}</h2>{items}</section>
 <section><h2>{r["h_tips"]}</h2><ul class="checks">{tips}</ul></section>
 <section>{contact_box(l)}{cta_box(l, me)}</section>
 <section><h2>{u["blog_h"]}</h2>{posts(l, me, ARTICLES[::-1][:6])}</section>
</main>
"""
    return head(l, "routes", None, r["title"], r["desc"], [art, crumbs_ld(l, [(u["crumbs_routes"], me)])], "airblade") + body + foot(l)

def page_blog(l):
    b, u = C[l]["blog"], C[l]["ui"]
    me = blog_path(l)
    r = C[l]["routes"]
    extra = f'<a class="post" href="{rel(me, routes_path(l))}"><b>{r["h1"]}</b><span>{r["desc"]}</span></a>'
    body = f"""
<header><div class="wrap">{langbar(l, "blog", None, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_blog"], None)])}
 <h1>{b["h1"]}</h1><p class="lead">{b["lead"]}</p>
</div></div></header>
<main class="wrap">
 <section>{posts(l, me, ARTICLES[::-1]).replace("</div>", extra + "</div>", 1)}</section>
 <section>{contact_box(l)}{cta_box(l, me)}</section>
</main>
"""
    return head(l, "blog", None, b["title"], b["desc"], [crumbs_ld(l, [(u["crumbs_blog"], me)])]) + body + foot(l)

def page_article(l, k):
    slug, title, h1, desc, lead, img, html = C[l]["articles"][k]
    u = C[l]["ui"]
    me = art_path(l, k)
    pre = "../" * me.count("/")
    html = html.replace("{ROUTES}", rel(me, routes_path(l)))
    art = {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "inLanguage": l,
           "mainEntityOfPage": BASE + me, "image": f"{BASE}img/{img}.jpg", "datePublished": adate(k),
           "author": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"},
           "publisher": {"@type": "Organization", "name": "Van Phu Dalat Motorbike Rental"}}
    others = [x for x in ARTICLES[::-1] if x != k][:3]
    body = f"""
<header><div class="wrap">{langbar(l, "art", k, me)}
<div class="hero">{crumbs(l, me, [(u["crumbs_blog"], blog_path(l))])}
 <h1>{h1}</h1><p class="lead">{lead}</p>
 <img class="heroimg" src="{pre}img/{img}.jpg" alt="{h1}" width="1200" height="675">
</div></div></header>
<main class="wrap">
 <section class="prose">{html}</section>
 <section>{contact_box(l)}{cta_box(l, me)}</section>
 <section><h2>{u["read_also"]}</h2>{posts(l, me, others)}</section>
</main>
"""
    return head(l, "art", k, title, desc, [art, crumbs_ld(l, [(u["crumbs_blog"], blog_path(l)), (h1, me)])], img) + body + foot(l)

# ------------------------------------------------------------------ write
def write(path, html):
    p = OUT / path / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")

# images live in <repo>/img and are referenced directly; nothing is deleted here

groups = [("home", None), ("routes", None), ("blog", None)] + [("art", k) for k in ARTICLES]
for l in LANGS:
    write(home_path(l), page_home(l))
    write(routes_path(l), page_routes(l))
    write(blog_path(l), page_blog(l))
    for k in ARTICLES:
        write(art_path(l, k), page_article(l, k))

urls = ""
for kind, key in groups:
    alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{BASE + path_of(x, kind, key)}"/>\n' for x in LANGS)
    alts += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE + path_of("en", kind, key)}"/>\n'
    lm = adate(key) if kind == "art" else max([adate(k) for k in ARTICLES] + ["2026-10-10"])
    for l in LANGS:
        urls += f"  <url>\n    <loc>{BASE + path_of(l, kind, key)}</loc>\n{alts}    <lastmod>{lm}</lastmod>\n  </url>\n"
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n", encoding="utf-8")
LLMS = f"""# Van Phu Dalat Motorbike Rental (Thuê xe máy Đà Lạt Văn Phú)

> Local motorbike and scooter rental in Da Lat (Đà Lạt), Vietnam. Honda Vision 110, Honda Air Blade 125 and electric scooters, all 150,000 VND per day. No cash deposit, free hotel delivery in central Da Lat for rentals of 2+ days.

## Key facts
- Address: 1/15/5 Thông Thiên Học, Đà Lạt, Vietnam ({GMAPS})
- Price: 150,000 VND/day for every bike, fixed, no hidden fees
- Opening hours: every day 4:30 AM – 9:00 PM
- Rental day: from pickup until 9:00 PM the same day
- Deposit: no cash deposit; the guest leaves a passport or ID card; rental fee paid upfront
- Included: free helmet and phone holder with every bike; gas scooters come with 1 liter of fuel
- Delivery: free to hotels in central Da Lat for rentals of 2 days or more
- Before renting: test ride and a video of the bike's condition, filmed together
- Booking: WhatsApp +84 944 081 101 or +84 834 622 149, Zalo 0944 081 101, Telegram @vanphudalat, WeChat vanphudalat
- Languages on the website: {", ".join(LABEL.values())}

## Pages
- [Home (English)]({BASE}): prices, bikes, FAQ, map
- [Motorbike routes around Da Lat]({BASE + routes_path("en")})
- [Travel blog]({BASE + blog_path("en")})
""" + "".join(f"- [{LABEL[x]} home]({BASE + home_path(x)})\n" for x in LANGS if x != "en")
(OUT / "llms.txt").write_text(LLMS, encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
print("pages:", sum(1 for _ in OUT.rglob("index.html")))
