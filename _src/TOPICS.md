# SEO content plan — Văn Phú Đà Lạt (https://vanphudalat.com/)

Owner: Phú (vanphudl@gmail.com). Report language: Vietnamese.

## How a new article is added
1. Pick the first unchecked topic in "Backlog". The backlog is a dated daily calendar (one article per day); follow its order. If a day was missed, just take the next unchecked one. Topics marked (publish ~date) wait until that date.
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
- Electric-scooter range: only as the owner-approved figure "one battery lasts about 35–40 km" (battery swap at the shop 20,000 VND). Never any other number, never "per charge" wording.
- Electric scooters: max 2 riders with combined weight under 100 kg; avoid long steep passes (Prenn, Mimosa, Lang Biang) — suggest the Air Blade 125cc for long trips.
- Prices: 150,000 VND/day for every bike (Honda Vision 110cc, Honda Air Blade 125cc, electric scooter). No cash deposit — guest leaves passport or ID card. Free helmet. Phone holder on every bike; gas scooters come with 1 liter of fuel. Free hotel delivery in central Da Lat for 2+ days. Rental day = pickup until 21:00. Test ride + video of bike condition before rental.
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
- 2026-10-12 waterfalls — Waterfalls near Da Lat by motorbike (Datanla, Prenn, Elephant Falls, Pongour)
- 2026-10-14 evrules — Electric scooter rental rules (owner's official rules; link to it from electric-scooter articles)
- 2026-10-14 caudat — Cau Dat tea hills: complete sunrise guide

## Backlog (top = next) — daily calendar from 2026-10-14
- [ ] 15/10 cloudhunt — Cloud hunting (săn mây) around Da Lat: where, what time, riding there before dawn
- [ ] 16/10 nightmarket — Da Lat night market guide: what to eat and buy
- [ ] 17/10 langbiang — Lang Biang Mountain guide by motorbike
- [ ] 18/10 electric — Electric scooter rental in Da Lat: why it's great for the city (no licence talk; link to the evrules article)
- [ ] 19/10 coffee — Coffee with a view: Da Lat cafés reachable by bike (types/areas, only very famous names)
- [ ] 20/10 rainyday — What to do in Da Lat on a rainy day
- [ ] 21/10 tuyenlam — Tuyen Lam Lake & Truc Lam Monastery guide
- [ ] 22/10 photospots — Best photo spots in Da Lat by motorbike
- [ ] 23/10 flowers — Flower villages and farms around Da Lat (Van Thanh etc.)
- [ ] 24/10 thingstodo — Things to do in central Da Lat: Xuan Huong Lake, Da Lat Station, Crazy House, Domaine de Marie
- [ ] 25/10 oneday — Da Lat in 1 day by motorbike: a full loop
- [ ] 26/10 strawberries — Strawberry farms and local produce
- [ ] 27/10 where-to-stay — Where to stay in Da Lat: areas compared (no specific hotel claims)
- [ ] 28/10 budget — Planning a Da Lat trip budget (only own rental price exact; others qualitative)
- [ ] 29/10 passes — Scenic mountain roads around Da Lat (Prenn, Mimosa) — safety focus
- [ ] 30/10 kids — Da Lat with kids
- [ ] 31/10 pinkgrass — Pink grass (cỏ hồng) season around Da Lat: where to see it by bike
- [ ] 01/11 november — Da Lat in November: weather, what's in season, what to pack
- [ ] 02/11 days2 — Da Lat in 2 days 1 night by motorbike
- [ ] 03/11 sunrise-sunset — Best sunrise and sunset spots around Da Lat
- [ ] 04/11 station — Da Lat Railway Station and the train to Trai Mat & Linh Phuoc (Ve Chai) pagoda
- [ ] 05/11 phrases — Useful Vietnamese phrases for renting a bike, eating and shopping in Da Lat
- [ ] 06/11 parking-fuel — Practical riding in Da Lat: parking, fuel stations, charging, helmets, rain gear
- [ ] 07/11 pagodas — Temples and pagodas of Da Lat worth a ride
- [ ] 08/11 danhia — Dankia Lake & Golden Stream (Suoi Vang) by motorbike
- [ ] 09/11 solo — Da Lat for solo travellers
- [ ] 10/11 vegetarian — Vegetarian and vegan food in Da Lat
- [ ] 11/11 souvenirs — What to buy in Da Lat: local souvenirs and specialties
- [ ] 12/11 december — Da Lat in December & the Flower Festival (tell readers to check official festival dates; never invent dates)
- [ ] christmas — Da Lat in December: Christmas, cool weather, early cherry blossom (publish ~early Dec)
- [ ] tet — Tết (Lunar New Year) in Da Lat: tips for travellers (publish ~early Jan)
