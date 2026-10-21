# SEO content plan — Văn Phú Đà Lạt (https://vanphudalat.com/)

Owner: Phú. Report language: Vietnamese.

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
- Electric-scooter range: only as the owner-approved figures "one battery lasts about 35–40 km; each scooter comes with 2 batteries, about 60–70 km in total" (battery swap at the shop 20,000 VND). Never any other number, never "per charge" wording.
- Electric scooters: max 2 riders with combined weight under 140 kg (owner changed from 100 kg on 2026-10-18); avoid long steep passes (Prenn, Mimosa, Lang Biang) — suggest the Air Blade 125cc for long trips.
- Prices: 150,000 VND/day for every bike, fixed, no discounts (never advertise a lower or "from" price — the owner always charges 150,000 VND). Always write the currency as "VND" in every language — never đ, ₫, донг, ดอง, 동, ドン, 越南盾, דונג. Bikes: Honda Vision 110cc, Honda Air Blade 125cc, electric scooter. No cash deposit — guest leaves passport or ID card. Free helmet. Phone holder on every bike; gas scooters come with 1 liter of fuel. Free hotel delivery in central Da Lat for 2+ days. Rental day = pickup until 21:00. Test ride + video of bike condition before rental.
- Contacts: WhatsApp +84 944 081 101 / +84 834 622 149, Zalo 0944 081 101, Telegram @vanphudalat, WeChat vanphudalat, Russian Telegram channel t.me/dalat_life_vietnam. Shop: 1/15/5 Thông Thiên Học, Đà Lạt.
- Rules to mention where natural: no alcohol/beer when riding; strictly follow Vietnamese traffic law.
- Facts about places: only well-established ones; distances/times as approximate ("about", "около", "约"). No invented prices of tickets/hotels, no invented opening hours, no fake reviews or quotes, no claims about competitors.
- Write each language natively (not word-for-word); keep the article genuinely useful to a traveller (≈450–700 words in en). Avoid keyword stuffing.
- Hebrew (he) is right-to-left; write natural Israeli Hebrew, plural address (אתם), avoid recommending pork dishes. German/French/Spanish: natural, informal-friendly tone (du / vous / tú).
- Malay: avoid pork dishes as recommendations; mention halal where food is discussed. Thai/Malay/Indonesian readers drive on the left at home — remind "Vietnam drives on the right" if riding is discussed.

- Photo-spot map page (/photo-map/, all 13 languages) is built from `content/photomap.py`; the pagoda map (/pagoda-map/, 7 pagodas) from `content/pagodamap.py`, the church map (/church-map/, 6 churches) from `content/churchmap.py`, the wild-sunflower map (/wild-sunflower-map/, 9 dã quỳ spots, season late Oct–Dec) from `content/sunflowermap.py`, the cloud-hunting map (/cloud-hunting-map/, 8 sunrise spots) from `content/cloudmap.py`, the café map (/cafe-view-map/, 12 view cafés) from `content/cafemap.py`, all 13 languages. Their PDFs live in `/files/` (VanPhu-Dalat-Photo-Map-XX.pdf, VanPhu-Dalat-Pagoda-Map-XX.pdf, VanPhu-Dalat-Church-Map-XX.pdf, VanPhu-Dalat-Wild-Sunflower-Map-XX.pdf, VanPhu-Dalat-Cloud-Hunting-Map-XX.pdf, VanPhu-Dalat-Cafe-View-Map-XX.pdf); the BBQ map (/bbq-map/, 9 grill restaurants) from `content/bbqmap.py`, all 13 languages (files/VanPhu-Dalat-BBQ-Map-XX.pdf); the 5-star hotels map (/5-star-hotels-map/, 8 hotels/resorts listed as 5-star by 2+ sources; Terracotta, Dalat Wonder left out as not consistently 5-star) from `content/hotelmap.py` (files/VanPhu-Dalat-5-Star-Hotels-Map-XX.pdf); the 4-star hotels map (/4-star-hotels-map/, 10 hotels listed as 4-star by 2+ sources with 800+ reviews) from `content/fourstarmap.py` (files/VanPhu-Dalat-4-Star-Hotels-Map-XX.pdf); the 3-star hotels map (/3-star-hotels-map/, 8 hotels listed as 3-star by 2+ sources with 250+ reviews) from `content/threestarmap.py` (files/VanPhu-Dalat-3-Star-Hotels-Map-XX.pdf); the Saigon bus map (/saigon-bus-map/, Da Lat bus station + 12 bus company offices, no fares/timetables) from `content/busmap.py` (files/VanPhu-Dalat-Saigon-Bus-Map-XX.pdf); the Da Nang bus map (/da-nang-bus-map/, Da Lat bus station + 6 company offices on the Da Nang / Hoi An route, kept only when 2+ sources agree and the office matches Google Maps; no fares/timetables) from `content/danangbusmap.py` (files/VanPhu-Dalat-Da-Nang-Bus-Map-XX.pdf); the Flower Festival 2026 page (/flower-festival-2026/, 11th edition, planned 19–31 Dec 2026 per the 8 Oct 2026 press briefing — all dates marked as planned; update when the official schedule is out) from `content/festivalmap.py` (files/VanPhu-Dalat-Flower-Festival-2026-XX.pdf), its banner on the home page sits below the map section (owner asked: not at the top). Do not delete them. Articles about sights or pagodas may link to them with a relative link to `photo-map/` or `pagoda-map/` in their language.

- `/go/` is the QR landing page printed on bike stickers (hand-written HTML, not built by build_site.py). Never delete it; community links are in the COMMUNITY block at the top of its script.

## Published
- 2026-10-10 weather — Da Lat weather by month
- 2026-10-10 getting — How to get to Da Lat (Nha Trang, HCMC, Mui Ne)
- 2026-10-10 days3 — Da Lat in 3 days by motorbike
- 2026-10-10 food — What to eat in Da Lat
- 2026-10-10 riding — Riding a motorbike in Vietnam: tips
- 2026-10-11 wildsunflower — Wild sunflower (dã quỳ) season around Da Lat by motorbike
- 2026-10-12 waterfalls — Waterfalls near Da Lat by motorbike (Datanla, Prenn, Elephant Falls, Pongour)
- 2026-10-14 domainedemarie — Domaine de Marie pink church guide (owner's photos)
- 2026-10-14 evrules — Electric scooter rental rules (owner's official rules; link to it from electric-scooter articles)
- 2026-10-14 caudat — Cau Dat tea hills: complete sunrise guide
- 2026-10-15 cloudhunt — Cloud hunting (săn mây) around Da Lat: where, when, riding there before dawn (links to cloud-hunting-map and caudat)
- 2026-10-15 lt-nodeposit — Long-tail: motorbike rental in Da Lat with no cash deposit (passport/ID card; links to price article)
- 2026-10-16 nightmarket — Da Lat night market guide: what to eat and buy (18 languages)
- 2026-10-16 lt-procedure — Long-tail: how to rent a motorbike in Da Lat step by step (18 languages)
- 2026-10-16 lt-ev-foreigners — EV long-tail: electric scooter rental in Da Lat for foreigners (18 languages; first article of the daily EV series)
- 2026-10-17 langbiang — Lang Biang Mountain guide by motorbike (Radar Peak by jeep/on foot, summit trail; 18 languages; photos group-rental-air-blade-van-phu-morning + van-phu-guest-air-blade-thumbs-up)
- 2026-10-17 lt-documents — Long-tail: what you need to rent a motorbike in Da Lat (passport/CCCD only; vi "thuê xe máy Đà Lạt cần giấy tờ gì"; 18 languages)
- 2026-10-17 lt-ev-experience — EV long-tail: practical tips for renting an electric scooter in Da Lat (vi "kinh nghiệm thuê xe điện ở Đà Lạt"; 18 languages)
- 2026-10-18 coffee — Coffee with a view: Da Lat cafés by area by motorbike (links cafe-view-map + night-view-cafe-map, nightmarket; photos white-honda-vision-sidewalk-dalat + honda-vision-cafe-garden-dalat + couple-air-blade-dalat-center-street; 18 languages)
- 2026-10-18 lt-early — Long-tail: early-opening motorbike rental, shop opens 4:30 am (vi "thuê xe máy Đà Lạt mở cửa sớm"; links cloudhunt, caudat, cloud-hunting-map; photos van-phu-shop-early-pickup-air-blade + evening-pickup-van-phu-1-15-5-thong-thien-hoc; 18 languages)
- 2026-10-18 lt-ev-city — EV long-tail: exploring the city by electric scooter (vi "xe điện đi dạo thành phố Đà Lạt"; links evrules, lt-ev-experience; photos electric-scooters-van-phu-shop + guest-white-electric-scooter-dalat; 18 languages)
- 2026-10-19 days2 — Da Lat 2 days 1 night by motorbike (en "Dalat 2 day itinerary by motorbike"; links waterfalls, nightmarket, caudat, days3; photos friends-air-blade-van-phu-gate + honda-vision-bui-thi-xuan-street-dalat + air-blade-handover-dalat-homestay; 18 languages) — add a link to lt-2days when it is published
- 2026-10-19 lt-busstation — Long-tail: motorbike rental near Da Lat bus station (vi "thuê xe máy gần bến xe đà lạt", en "motorbike rental near Dalat bus station"; links saigon-bus-map, lt-procedure; photos honda-air-blade-vision-fleet-van-phu + honda-vision-hotel-delivery-dalat; 18 languages)
- 2026-10-19 lt-ev-price — EV long-tail: electric scooter rental price (vi "giá thuê xe máy điện đà lạt"; links price, evrules; photos electric-scooters-helmets-van-phu + electric-scooters-van-phu-shop; 18 languages)
- 2026-10-22 getaround — How to get around Dalat without a car (en "how to get around Dalat without a car", vi "cách di chuyển ở Đà Lạt không cần ô tô"; links days2, riding, routes; photos honda-vision-girls-helmets-dalat + couple-air-blade-dalat-center-street; 18 languages)
- 2026-10-22 lt-automatic — Long-tail: automatic scooter rental (vi "thuê xe tay ga Đà Lạt", en "automatic scooter rental Dalat"; links lt-procedure; photos van-phu-shop-busy-morning-vision-air-blade + guest-white-honda-vision-van-phu-shop; 18 languages)
- 2026-10-22 lt-ev-battery — EV long-tail: how far the battery goes, when to swap (vi "thuê xe máy điện Đà Lạt đi được bao xa"; links lt-ev-city, evrules; photos electric-scooters-van-phu-shop + guest-white-electric-scooter-dalat; 18 languages)

- Spot guide pages (one per photo-map spot, long-tail: opening hours, entrance fee, how to get there by scooter, history, photo spots, FAQ) use the owner's own photos in `img/spots/<id>-*.webp`; first done: 2026-10-14 domainedemarie. Write the next ones only when the owner sends photos.

## Long-tail backlog — rental keywords (ONE per day, in addition to the daily travel article)
Purpose: rank for longer, less competitive rental searches in every language. Rules for these articles:
- Each article answers ONE specific search intent with practical, honest info (≈450–650 words in en). Never a near-copy of the main rental page or of existing articles `price` (rental prices) and `evgas` (electric vs gas) — link to them instead.
- Title/H1/meta built around the natural local phrase for that intent in EACH language (research how people really search it in that language, e.g. vi "thuê xe máy Đà Lạt không cần cọc", ru "аренда байка в Далате без залога", zh "大叻租摩托车 不用押金", th "เช่ามอเตอร์ไซค์ดาลัด ไม่ต้องมัดจำ"). Use the phrase naturally 2–4 times; no stuffing.
- Link to the main rental page with <a href="{HOME}">…</a> and, for electric topics, to <a href="{EV}">…</a>.
- All Hard rules apply (no licence wording in any language, no invented facts, no competitor claims). Hotel delivery only exactly as the owner's rule: free delivery to hotels in central Da Lat for rentals of 2+ days (never promise it for 1-day rentals — say "message us").
- OWNER'S KEYWORD PLAN (16/10/2026): focus on 4 niche groups — (1) no cash deposit & quick paperwork, (2) early opening / cloud hunting / sunrise, (3) electric scooters (EV backlog), (4) delivery & location. Each topic below lists its exact Vietnamese target keyword → the vi title_tag, H1 and meta must contain it verbatim (natural capitalisation); other languages use their own natural equivalent.
- OWNER'S KEYWORD PLAN 2 (17/10/2026, English-search priorities): each topic below marked [KW2] lists an exact English target phrase → the en title_tag, H1 and meta must contain it (natural capitalisation); vi and other languages use their natural equivalent. Already covered, do NOT write new articles for: "Dalat motorbike rental price" / "How much does it cost to rent a scooter in Dalat" (existing `price`), "Dalat motorbike rental requirements" (lt-documents), "Best places to visit around Dalat by scooter" (routes page + photospots), "What to know before riding a scooter in Dalat" (riding + lt-first-time). Never write "international driving permit" / "can foreigners legally ride" topics — they break the no-licence hard rule.
- Internal links: add every new key to its cluster in `content/cluster.py` ("Read also" then shows cluster siblings first), and link 1–2 sibling articles in the body with <a href="{ART:<key>}">…</a>.
- "Documents" topics: the ONLY documents are passport (foreigners) or CCCD/ID card (Vietnamese guests). Never mention any other document, licence or permit.
- [ ] lt-2days — [KW2] Renting a scooter in Da Lat for 2 days: how the 2 days are counted (pick-up until 21:00), free hotel delivery in central Da Lat from 2 days, a simple 2-day plan linking days2 — en: "rent a scooter in Dalat for 2 days" — vi: "thuê xe máy đà lạt 2 ngày"
- [ ] lt-foreigners — [KW2] Can foreigners rent a motorbike in Da Lat? Yes — passport only, no cash deposit, booking in English, all bike types; never discuss legality/licences; don't repeat lt-ev-foreigners (EV only), link it — en: "can foreigners rent a motorbike in Dalat" — vi: "khách nước ngoài thuê xe máy ở đà lạt"
- [ ] lt-delivery — [Group 4] Motorbike rental with delivery to your hotel in Da Lat: free in central Da Lat for 2+ days, what to send (hotel name, time), check the bike together at handover — vi: "thuê xe máy giao tận khách sạn đà lạt"
- [ ] lt-center — [Group 4] Motorbike rental near central Da Lat: shop at 1/15/5 Thông Thiên Học, getting there on foot/Grab from the market and Xuan Huong Lake (approximate only), riding to the night market and where to park — vi: "thuê xe máy gần trung tâm đà lạt" — [KW2] en: "motorbike rental near Dalat night market" as secondary phrase (also in en title/meta); link nightmarket
- [ ] lt-caudat-early — [Group 2] Renting a motorbike for a dawn ride to the Cau Dat tea hills: which bike (Air Blade), pick-up time, fuel, warm clothes — rental angle only, link the caudat guide instead of repeating it — vi: "thuê xe máy đi đồi chè cầu đất sáng sớm"
- [ ] lt-airblade — Renting a Honda Air Blade 125cc in Da Lat (for passes, two riders, longer day trips)
- [ ] lt-vision — Renting a Honda Vision 110cc in Da Lat (light, easy automatic for beginners and city riding)
- [ ] lt-multiday — Renting a motorbike in Da Lat for a week or longer (2-day intent is lt-2days — don't repeat it) (150,000 VND/day, how days are counted, tips)
- [ ] lt-two — Motorbike rental in Da Lat for two people / couples (which bike, comfort, safety)
- [ ] lt-checklist — 10 things to check before renting a motorbike in Da Lat (brakes, tyres, lights, helmet, video) — no claims about other shops
- [ ] lt-rainy — Renting a motorbike in Da Lat in the rainy season (raincoat, slippery hills, what to avoid) — [KW2] en secondary: "Dalat in the rain: transport tips"; link rainyday
- [ ] lt-backpacker — Motorbike rental in Da Lat for backpackers and budget travellers
- [ ] lt-booking — How to book a motorbike in Da Lat online (WhatsApp, Zalo, WeChat, Telegram — what to send)
- [ ] lt-reliable — How to choose a reliable motorbike rental in Da Lat (transparent price, no hidden fees, written rules) — generic advice, no competitor claims
- [ ] lt-first-time — [KW2] en: "is it easy to ride a scooter in Dalat" — First time riding a scooter in Da Lat: is it hard? (practice, quiet streets, traffic on the right)
- [ ] lt-tet — Motorbike rental in Da Lat during Tết and holidays: book early (publish ~early Jan)
- [ ] lt-christmas — Motorbike rental in Da Lat over Christmas and New Year (publish ~early Dec)

## Photos — owner's real photos (use them in every new article)
- Library: `img/<name>.jpg` (EXIF/GPS stripped, ≤1200 px, ~150–240 KB; the build serves WebP copies of ~20–75 KB automatically). Alt texts in all languages: `content/photos.py` ALT[lang][name].
- Landscape 1200x675 (can be the article hero = image_name): van-phu-shop-early-pickup-air-blade, honda-vision-girls-helmets-dalat, van-phu-shop-busy-morning-vision-air-blade, friends-air-blade-van-phu-gate, group-rental-air-blade-van-phu-morning, honda-air-blade-vision-fleet-van-phu, vision-air-blade-villa-delivery-dalat, white-honda-vision-sidewalk-dalat, electric-scooters-van-phu-shop, electric-scooters-helmets-van-phu.
- Portrait (inline only): van-phu-guest-air-blade-thumbs-up, air-blade-handover-dalat-homestay, guest-white-honda-vision-van-phu-shop, honda-vision-cafe-garden-dalat, couple-air-blade-dalat-center-street, honda-vision-hotel-delivery-dalat, evening-pickup-van-phu-1-15-5-thong-thien-hoc, honda-vision-bui-thi-xuan-street-dalat, guest-white-electric-scooter-dalat.
- In an article body put `{PHOTO:<name>}` on its own line between blocks (1–2 per article, matching the topic: electric photos for EV articles). Link another article with `<a href="{ART:<key>}">`. Older articles get photos via HERO/INLINE in photos.py.
- New photos from the owner: save as `img/<descriptive-english-kebab-name>.jpg` (landscape cropped to 1200x675, portrait max 900x1200, quality ~78, no EXIF) and add ALT for all 18 languages.

## EV backlog — electric-scooter rental long-tail (ONE per day, third daily article)
Same rules as the long-tail backlog; link <a href="{EV}">…</a>, <a href="{HOME}">…</a> and the rules article <a href="{ART:evrules}">…</a>; never duplicate `evgas` (electric vs gas) or `evrules`. Battery only with the approved figures above. Max 2 riders under 140 kg combined; no long steep passes (Prenn, Mimosa, Lang Biang) — suggest the Air Blade for those.
- [ ] lt-ev-couples — Electric scooter for two in Da Lat (combined under 140 kg, comfort, when to pick the Air Blade instead)
- [ ] lt-ev-beginners — Electric scooter for beginners in Da Lat (no gears, quiet, first ride tips, Vietnam drives on the right)
- [ ] lt-ev-cafes — Café hopping in Da Lat by electric scooter (areas, parking, short hops)
- [ ] lt-ev-night — Riding an electric scooter in Da Lat in the evening (lights, cold, night market, return before 21:00)
- [ ] lt-ev-rain — Electric scooter in Da Lat in the rain (slippery hills, no deep water, raincoat)
- [ ] lt-ev-vs-grab — Electric scooter rental vs Grab/taxi for getting around Da Lat (honest comparison, no invented fares)
- [ ] lt-ev-eco — Eco-friendly travel in Da Lat: quiet electric scooter, no fuel, cleaner air
- [ ] lt-ev-parking — Parking an electric scooter in Da Lat (guarded lots, gửi xe tickets, locking)
- [ ] lt-ev-halfday — Half-day city loop in Da Lat by electric scooter (central sights only)
- [ ] lt-ev-checklist — What to check when picking up an electric scooter in Da Lat (battery level, brakes, lights, video)
- [ ] lt-ev-families — Electric scooter in Da Lat for families and older travellers (gentle, quiet; safety)
- [ ] lt-ev-faq — Electric scooter rental in Da Lat: 10 common questions answered

## Backlog (top = next) — daily calendar from 2026-10-14
- [ ] 22/10 selfguided — [KW2] Exploring Da Lat on your own without a tour: planning a self-guided motorbike day (offline maps, fuel/battery, timing, weather, safety), linking routes page; not an itinerary (that's oneday/days2) — en: "Dalat self guided motorbike route" (also "how to explore Dalat without a tour")
- [ ] 20/10 rainyday — What to do in Da Lat on a rainy day
- [ ] 21/10 tuyenlam — Tuyen Lam Lake & Truc Lam Monastery guide
- [ ] 22/10 photospots — Best photo spots in Da Lat by motorbike
- [ ] 23/10 flowers — Flower villages and farms around Da Lat (Van Thanh etc.)
- [ ] 24/10 thingstodo — Things to do in central Da Lat: Xuan Huong Lake, Da Lat Station, Crazy House, Domaine de Marie
- [ ] 25/10 oneday — Da Lat in 1 day by motorbike: a full loop
- [ ] 26/10 strawberries — Strawberry farms and local produce
- [ ] 27/10 where-to-stay — Where to stay in Da Lat: areas compared (no specific hotel claims)
- [ ] 28/10 budget — Planning a Da Lat trip budget (only own rental price exact; others qualitative)
- [ ] 29/10 passes — [KW2] Scenic roads and viewpoints around Da Lat (Prenn, Mimosa) — safety focus — en: "Dalat scenic roads and viewpoints"
- [ ] 30/10 kids — Da Lat with kids
- [ ] 31/10 pinkgrass — Pink grass (cỏ hồng) season around Da Lat: where to see it by bike
- [ ] 01/11 november — Da Lat in November: weather, what's in season, what to pack
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

- Languages: 13 original + it, nl, km, lo, my via `content/_langs.py` (NEW/META); each new language needs `<l>.py`, `<l>_art.py`, `<l>_maps.py` (one MAPS entry per map module). Khmer, Lao and Myanmar texts await a native-speaker check.
- PDFs: built with Chromium, then shrunk with ghostscript + qpdf (font subsets merged); CJK PDFs use fontsource Noto Sans SC/JP/KR (TrueType) instead of the system .ttc fonts, which Chromium embedded as large Type 3 fonts.

- Day-trip set (route maps routenew/routecheckin, day hub, hub reference prices) in 16 more languages: one file per language _src/content/dt_<l>.py, loaded by content/daytr.py. Route PDFs: MAPMOD=routenew|routecheckin pdf.py for all 18.
- Waterfalls map (waterfallmap.py + waterfallmap_tr/_tr2, 18 langs): 6 open waterfalls; Hang Cop, Gougah closed (2026), Tam Tham/Ankroet/Bobla left out.
- Night-view café map (nightcafemap.py + _tr/_tr2, 18 langs): 6 cafés on east hills chosen by owner; PDF uses PROJ_CENTER (cluster) and no rings.
