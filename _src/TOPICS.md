# SEO content plan — Văn Phú Đà Lạt (vanphudl-pixel.github.io)

Owner: Phú (vanphudl@gmail.com). Report language: Vietnamese.

## How a new article is added
1. Pick the first unchecked topic in "Backlog" (season-aware: skip ahead if a seasonal topic is due within ~4 weeks).
2. Add the article to **every** file in `content/` (en, ru, zh, ko, ja, th, id, ms, vi, de, fr, es, he) under the **same key**, appended at the END of `C["articles"]` (order = publish order).
   Tuple: `(slug, title_tag, h1, meta_description, lead, image_name, html_body)`
   - slug: en/zh/ko/ja/th/id/ms/de/fr/es/he → same English kebab slug; ru → transliterated Russian slug; vi → Vietnamese kebab slug without diacritics.
   - image_name: one of the files in `/img` without `.jpg`: electric-row, electric-helmets, airblade, fleet-gas, vision-white (do NOT use guest-1/guest-2 as article images).
   - html_body: `<h2>`, `<p>`, `<ul><li>` only. Link to the routes page with `<a href="{ROUTES}">…</a>` when relevant.
3. In `content/en.py` add the publish date: `C["dates"]["<key>"] = "YYYY-MM-DD"` (create `C["dates"] = {}` if missing).
4. `python3 _src/build_site.py && python3 _src/check.py` — must print ALL CHECKS PASSED.
5. Move the topic to "Published" with date and key. Commit + push to `main`.

## Hard rules (business owner's decisions — never break)
- NEVER mention driving licences/permits in any language (no "license", "права", "驾照", "bằng lái", etc.).
- NEVER state an electric-scooter range in km.
- Prices: 150,000 VND/day for every bike (Honda Vision 110, Honda Air Blade 125, electric scooter). No cash deposit — guest leaves passport or ID card. Free helmet. Phone holder on every bike; gas scooters come with 1 liter of fuel. Free hotel delivery in central Da Lat for 2+ days. Rental day = pickup until 21:00. Test ride + video of bike condition before rental.
- Contacts: WhatsApp +84 944 081 101 / +84 834 622 149, Zalo 0944 081 101, Telegram @vanphudalat, WeChat vanphudalat, Russian Telegram channel t.me/dalat_life_vietnam. Shop: 1/15/5 Thông Thiên Học, Đà Lạt.
- Rules to mention where natural: no alcohol/beer when riding; strictly follow Vietnamese traffic law.
- Facts about places: only well-established ones; distances/times as approximate ("about", "около", "约"). No invented prices of tickets/hotels, no invented opening hours, no fake reviews or quotes, no claims about competitors.
- Write each language natively (not word-for-word); keep the article genuinely useful to a traveller (≈450–700 words in en). Avoid keyword stuffing.
- Hebrew (he) is right-to-left; write natural Israeli Hebrew, plural address (אתם), avoid recommending pork dishes. German/French/Spanish: natural, informal-friendly tone (du / vous / tú).
- Malay: avoid pork dishes as recommendations; mention halal where food is discussed. Thai/Malay/Indonesian readers drive on the left at home — remind "Vietnam drives on the right" if riding is discussed.

## Published
- 2026-10-10 weather — Da Lat weather by month
- 2026-10-10 getting — How to get to Da Lat (Nha Trang, HCMC, Mui Ne)
- 2026-10-10 days3 — Da Lat in 3 days by motorbike
- 2026-10-10 food — What to eat in Da Lat
- 2026-10-10 riding — Riding a motorbike in Vietnam: tips
- 2026-10-11 wildsunflower — Wild sunflower (dã quỳ) season around Da Lat by motorbike

## Backlog (top = next)
- [ ] waterfalls — Waterfalls near Da Lat by motorbike (Datanla, Pongour, Elephant Falls)
- [ ] caudat — Cau Dat tea hills: complete sunrise guide
- [ ] electric — Electric scooter rental in Da Lat: why it's great for the city (no range, no licence talk)
- [ ] nightmarket — Da Lat night market guide: what to eat and buy
- [ ] coffee — Coffee with a view: Da Lat cafés reachable by bike (describe types/areas, avoid naming specific businesses unless very famous)
- [ ] christmas — Da Lat in December: Christmas, cool weather, early cherry blossom (publish early Dec)
- [ ] rainyday — What to do in Da Lat on a rainy day
- [ ] photospots — Best photo spots in Da Lat by motorbike
- [ ] flowers — Flower villages and farms around Da Lat (Van Thanh etc.)
- [ ] tet — Tết (Lunar New Year) in Da Lat: tips for travellers (publish early Jan)
- [ ] langbiang — Lang Biang Mountain guide
- [ ] tuyenlam — Tuyen Lam Lake & Truc Lam Monastery guide
- [ ] kids — Da Lat with kids
- [ ] where-to-stay — Where to stay in Da Lat: areas compared (no specific hotel claims)
- [ ] strawberries — Strawberry farms and local produce
- [ ] budget — Planning a Da Lat trip budget (only own rental price is exact; others described qualitatively)
- [ ] passes — Scenic mountain roads around Da Lat (Prenn, Mimosa) — safety focus
