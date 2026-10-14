"""Da Lat 3-star hotels map — shared data for the website page (/3-star-hotels-map/) and the printable PDF.
Hotels listed as 3-star by at least two travel sources (mia.vn, vietnambooking.com, agotourist.com, tourdalattravel.com,
Oct 2026), with 250+ Google Maps reviews; coordinates and place links (cid) taken from Google Maps on 2026-10-14."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (reception)
SPOTS = [
    ("ngocphat",   11.9376231, 108.4439463, "10108612022680929948", True, "24h"),
    ("iris",       11.9410146, 108.4336734, "17595584161299827193", True, "24h"),
    ("dulys",      11.9407917, 108.4346003, "2788549472951622892",  True, "24h"),
    ("roydala",    11.9406411, 108.4355364, "12718554076507123743", True, "24h"),
    ("marguerite", 11.9412421, 108.4364376, "15508391104840311404", True, "24h"),
    ("maivang",    11.9420054, 108.4316465, "5025561373797321540",  True, "24h"),
    ("kyhoa",      11.9683652, 108.4438086, "15643657310000291558", True, "24h"),
    ("decharme",   11.9325602, 108.4645702, "12454287519585639178", True, "24h"),
]
CENTER = _PM.CENTER
SLUG = "3-star-hotels-map"
PDF = "VanPhu-Dalat-3-Star-Hotels-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 8
LEGW = 280
MAPH = 560
H1PT = 22
MAXKM = 4.0
RINGS = (1, 2, 3)
SIDE = {}
JITTER = {"maivang": (-14, -16), "iris": (-22, 12), "dulys": (-4, 26), "roydala": (18, 20), "marguerite": (20, -10), "kyhoa": (34, 8)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("3-Star Hotels in Da Lat: Map of 8 Popular Hotels | Van Phu", "Da Lat 3-Star Hotels Map",
 "Map of 8 popular 3-star hotels in Da Lat — most a short walk from the night market and Xuan Huong Lake — with directions, distances and a free PDF.",
 "Here are 8 hotels listed as 3-star in Da Lat, each with 250+ Google Maps reviews — six in the centre near the night market and two quieter ones a short ride out — with one-tap directions.",
 "In town (1–8)", "Good to know",
 [("Delivery", "we bring the scooter to your hotel in the city centre for rentals of 2 days or more"), ("Centre (1–6)", "all within walking distance of the night market and Xuan Huong Lake"), ("Deposit", "passport or ID card, no cash deposit"), ("Return", "bring the scooter back by 21:00")],
 "Tips",
 ["Ask reception where to park the scooter safely.", "Many 3-star hotels have no air-conditioning — Da Lat is cool, but ask for a fan if needed.", "Rooms on the street side can be noisy — ask for a higher floor.", "Star ratings and prices change — check with the hotel when you book."],
 [("Ngoc Phat Dalat Hotel", "Any time", "Hotel across from Lam Vien Square, some rooms with lake views."),
  ("Iris Dalat Hotel", "Any time", "Hotel on Phan Nhu Thach Street, a short walk from the night market."),
  ("Hotel Du Lys", "Any time", "Hotel on Nam Ky Khoi Nghia Street, minutes from the market and restaurants."),
  ("Hotel Roy Dala", "Any time", "Hotel with a marble lobby and large rooms, walking distance to the market and lake."),
  ("Marguerite Hotel", "Any time", "Spacious rooms on Nguyen Chi Thanh Street, across from the night market."),
  ("Mai Vang Hotel", "Any time", "Simple hotel on Hai Thuong Street, about 5 minutes to the night market."),
  ("Ky Hoa Garden Villages Hotel", "Any time", "French-style villas with gardens, north of the centre."),
  ("Dalat De Charme Village", "Sunset", "Themed rooms and a terraced garden, east of the centre.")])
T["vi"] = _mk("Khách sạn 3 sao Đà Lạt: bản đồ 8 khách sạn đông khách | Văn Phú", "Bản đồ khách sạn 3 sao Đà Lạt",
 "Bản đồ 8 khách sạn 3 sao đông khách ở Đà Lạt — phần lớn đi bộ ra chợ đêm và hồ Xuân Hương — có chỉ đường, khoảng cách và PDF miễn phí.",
 "Đây là 8 khách sạn được xếp hạng 3 sao ở Đà Lạt, nơi nào cũng có trên 250 đánh giá Google Maps — 6 nơi ở trung tâm gần chợ đêm và 2 nơi yên tĩnh hơn, đi xe một đoạn ngắn — có nút chỉ đường.",
 "Trong thành phố (1–8)", "Nên biết",
 [("Giao xe", "giao xe tận khách sạn trong trung tâm khi thuê từ 2 ngày"), ("Trung tâm (1–6)", "đều đi bộ được ra chợ đêm và hồ Xuân Hương"), ("Đặt cọc", "giữ hộ chiếu hoặc CCCD, không cọc tiền"), ("Trả xe", "trả xe trước 21:00")],
 "Lưu ý",
 ["Hỏi lễ tân chỗ để xe an toàn.", "Nhiều khách sạn 3 sao không có máy lạnh — Đà Lạt mát, cần thì xin thêm quạt.", "Phòng mặt đường có thể ồn — nên xin tầng cao.", "Hạng sao và giá phòng có thể thay đổi — hỏi khách sạn khi đặt phòng."],
 [("Khách sạn Ngọc Phát", "Cả ngày", "Khách sạn đối diện quảng trường Lâm Viên, có phòng view hồ."),
  ("Iris Dalat Hotel", "Cả ngày", "Khách sạn trên đường Phan Như Thạch, đi bộ vài phút ra chợ đêm."),
  ("Hotel Du Lys", "Cả ngày", "Khách sạn trên đường Nam Kỳ Khởi Nghĩa, gần chợ và quán ăn."),
  ("Hotel Roy Dala", "Cả ngày", "Sảnh lát đá cẩm thạch, phòng rộng, đi bộ ra chợ và hồ."),
  ("Khách sạn Marguerite", "Cả ngày", "Phòng rộng trên đường Nguyễn Chí Thanh, đối diện chợ đêm."),
  ("Khách sạn Mai Vàng", "Cả ngày", "Khách sạn đơn giản trên đường Hải Thượng, khoảng 5 phút ra chợ đêm."),
  ("Kỳ Hòa Garden Villages", "Cả ngày", "Biệt thự kiểu Pháp có sân vườn, phía bắc trung tâm."),
  ("Dalat De Charme Village", "Hoàng hôn", "Phòng thiết kế theo chủ đề, vườn bậc thang, phía đông trung tâm.")])
T["ru"] = _mk("Отели 3 звезды в Далате: карта 8 популярных отелей | Van Phu", "Карта отелей 3 звезды Далата",
 "Карта 8 популярных отелей Далата категории 3 звезды — большинство в нескольких минутах от ночного рынка и озера Суанхыонг — с маршрутом, расстоянием и бесплатным PDF.",
 "Здесь 8 отелей Далата категории 3 звезды, у каждого более 250 отзывов в Google Maps — шесть в центре у ночного рынка и два потише, недалеко от центра — с маршрутом в одно касание.",
 "В городе (1–8)", "Полезно знать",
 [("Доставка", "привезём байк к вашему отелю в центре при аренде от 2 дней"), ("Центр (1–6)", "все в пешей доступности от ночного рынка и озера Суанхыонг"), ("Залог", "паспорт или ID-карта, без денежного залога"), ("Возврат", "верните байк до 21:00")],
 "Советы",
 ["Спросите на ресепшене, где безопасно оставить байк.", "Во многих отелях 3 звезды нет кондиционера — в Далате прохладно, при необходимости попросите вентилятор.", "Номера с окнами на улицу бывают шумными — просите этаж повыше.", "Категория и цены меняются — уточняйте в отеле при бронировании."],
 [("Ngoc Phat Dalat Hotel", "В любое время", "Отель напротив площади Ламвьен, в части номеров вид на озеро."),
  ("Iris Dalat Hotel", "В любое время", "Отель на улице Фаннятхать, пара минут пешком до ночного рынка."),
  ("Hotel Du Lys", "В любое время", "Отель на улице Намкикхоингиа, рядом с рынком и кафе."),
  ("Hotel Roy Dala", "В любое время", "Мраморное лобби и большие номера, пешком до рынка и озера."),
  ("Marguerite Hotel", "В любое время", "Просторные номера на улице Нгуенчитхань, напротив ночного рынка."),
  ("Mai Vang Hotel", "В любое время", "Простой отель на улице Хайтхыонг, около 5 минут до ночного рынка."),
  ("Ky Hoa Garden Villages Hotel", "В любое время", "Виллы во французском стиле с садами, к северу от центра."),
  ("Dalat De Charme Village", "Закат", "Тематические номера и сад на террасах, к востоку от центра.")])
T["zh"] = _mk("大叻三星级酒店：8 家热门酒店地图 | Van Phu", "大叻三星级酒店地图",
 "大叻 8 家热门三星级酒店地图——大多步行即到夜市和春香湖——附导航、距离和免费 PDF。",
 "这里是大叻 8 家三星级酒店，每家在 Google 地图上都有 250 条以上评价——6 家在市中心夜市附近，2 家稍远一点、更安静——一键导航。",
 "市区（1–8）", "须知",
 [("送车", "租 2 天及以上，可把车送到市中心酒店"), ("市中心（1–6）", "步行即可到夜市和春香湖"), ("押金", "押护照或身份证，不收现金押金"), ("还车", "21:00 前还车")],
 "提示",
 ["向前台询问安全的停车位置。", "很多三星级酒店没有空调——大叻天气凉爽，需要时可以要风扇。", "临街房间可能较吵——可要求高楼层。", "星级和房价可能变化——订房时请向酒店确认。"],
 [("Ngoc Phat Dalat Hotel", "全天", "林园广场对面的酒店，部分房间可看湖景。"),
  ("Iris Dalat Hotel", "全天", "范如石路上的酒店，步行几分钟到夜市。"),
  ("Hotel Du Lys", "全天", "南圻起义路上的酒店，靠近市场和餐馆。"),
  ("Hotel Roy Dala", "全天", "大理石大堂、房间宽敞，步行可到市场和湖边。"),
  ("Marguerite Hotel", "全天", "阮志清路上的宽敞客房，就在夜市对面。"),
  ("Mai Vang Hotel", "全天", "海上路上的简单酒店，到夜市约 5 分钟。"),
  ("Ky Hoa Garden Villages Hotel", "全天", "带花园的法式别墅，位于市中心北边。"),
  ("Dalat De Charme Village", "日落", "主题客房和梯田花园，位于市中心东边。")])
T["ko"] = _mk("달랏 3성급 호텔: 인기 호텔 8곳 지도 | Van Phu", "달랏 3성급 호텔 지도",
 "달랏의 인기 3성급 호텔 8곳 지도 — 대부분 야시장과 쑤언흐엉 호수까지 걸어갈 수 있는 곳 — 길찾기, 거리, 무료 PDF.",
 "달랏의 3성급 호텔 8곳으로, 모두 구글 지도 리뷰가 250개 이상입니다. 6곳은 야시장 근처 시내, 2곳은 조금 떨어진 조용한 곳 — 원터치 길찾기.",
 "시내 (1–8)", "알아두세요",
 [("배달", "2일 이상 대여 시 시내 중심 호텔로 오토바이를 가져다 드립니다"), ("시내 중심 (1–6)", "모두 야시장과 쑤언흐엉 호수까지 걸어갈 수 있습니다"), ("보증", "여권 또는 신분증, 현금 보증금 없음"), ("반납", "21:00까지 반납")],
 "팁",
 ["오토바이를 안전하게 세울 곳을 리셉션에 물어보세요.", "3성급 호텔은 에어컨이 없는 곳이 많아요 — 달랏은 시원하지만 필요하면 선풍기를 요청하세요.", "길가 쪽 방은 시끄러울 수 있으니 높은 층을 요청하세요.", "등급과 요금은 바뀔 수 있으니 예약 시 호텔에 확인하세요."],
 [("Ngoc Phat Dalat Hotel", "언제든", "럼비엔 광장 맞은편 호텔, 일부 객실 호수 전망."),
  ("Iris Dalat Hotel", "언제든", "판뉴탁 거리의 호텔, 야시장까지 걸어서 몇 분."),
  ("Hotel Du Lys", "언제든", "남끼커이응이아 거리의 호텔, 시장과 식당 근처."),
  ("Hotel Roy Dala", "언제든", "대리석 로비와 넓은 객실, 시장과 호수까지 도보."),
  ("Marguerite Hotel", "언제든", "응우옌찌타인 거리의 넓은 객실, 야시장 맞은편."),
  ("Mai Vang Hotel", "언제든", "하이트엉 거리의 소박한 호텔, 야시장까지 약 5분."),
  ("Ky Hoa Garden Villages Hotel", "언제든", "정원이 있는 프랑스풍 빌라, 시내 북쪽."),
  ("Dalat De Charme Village", "해 질 녘", "테마 객실과 계단식 정원, 시내 동쪽.")])
T["ja"] = _mk("ダラットの3つ星ホテル：人気ホテル8軒の地図 | Van Phu", "ダラット3つ星ホテルマップ",
 "ダラットの人気3つ星ホテル8軒の地図。ほとんどがナイトマーケットやスアンフーン湖まで徒歩圏。ルート案内・距離・無料PDF付き。",
 "ダラットの3つ星ホテル8軒で、どこもGoogleマップの口コミが250件以上。6軒はナイトマーケット近くの中心部、2軒は少し離れた静かな場所です。ワンタップでルート案内。",
 "市内（1–8）", "知っておきたいこと",
 [("配達", "2日以上のレンタルなら市中心部のホテルまでバイクをお届け"), ("中心部（1–6）", "どこもナイトマーケットとスアンフーン湖まで徒歩圏"), ("デポジット", "パスポートまたはIDカード、現金デポジットなし"), ("返却", "21:00までに返却")],
 "ヒント",
 ["バイクを安全に停められる場所をフロントで聞きましょう。", "3つ星ホテルはエアコンがないことも多いです — ダラットは涼しいですが、必要なら扇風機を頼みましょう。", "通り側の部屋はうるさいことがあるので、高層階を頼みましょう。", "星の等級や料金は変わることがあります — 予約時にホテルへ確認を。"],
 [("Ngoc Phat Dalat Hotel", "いつでも", "ラムヴィエン広場の向かいのホテル、湖が見える部屋も。"),
  ("Iris Dalat Hotel", "いつでも", "ファンニュータック通りのホテル、ナイトマーケットまで徒歩数分。"),
  ("Hotel Du Lys", "いつでも", "ナムキーコイギア通りのホテル、市場や食堂の近く。"),
  ("Hotel Roy Dala", "いつでも", "大理石のロビーと広い客室、市場と湖まで徒歩圏。"),
  ("Marguerite Hotel", "いつでも", "グエンチータン通りの広い客室、ナイトマーケットの向かい。"),
  ("Mai Vang Hotel", "いつでも", "ハイトゥオン通りのシンプルなホテル、ナイトマーケットまで約5分。"),
  ("Ky Hoa Garden Villages Hotel", "いつでも", "庭のあるフランス風ヴィラ、中心部の北。"),
  ("Dalat De Charme Village", "夕暮れ", "テーマ別の客室と段々の庭園、中心部の東。")])
T["th"] = _mk("โรงแรม 3 ดาวในดาลัด: แผนที่โรงแรมยอดนิยม 8 แห่ง | Van Phu", "แผนที่โรงแรม 3 ดาวดาลัด",
 "แผนที่โรงแรม 3 ดาวยอดนิยม 8 แห่งในดาลัด ส่วนใหญ่เดินไปไนท์มาร์เก็ตและทะเลสาบซวนเฮืองได้ พร้อมเส้นทาง ระยะทาง และ PDF ฟรี",
 "นี่คือโรงแรม 3 ดาว 8 แห่งในดาลัด ทุกแห่งมีรีวิวบน Google Maps มากกว่า 250 รีวิว ในใจกลางเมืองใกล้ไนท์มาร์เก็ต 6 แห่ง และอีก 2 แห่งที่เงียบกว่า ขี่รถไม่ไกล กดนำทางได้ทันที",
 "ในเมือง (1–8)", "ควรรู้",
 [("ส่งรถ", "เช่าตั้งแต่ 2 วัน ส่งรถถึงโรงแรมในตัวเมือง"), ("ใจกลางเมือง (1–6)", "ทุกแห่งเดินไปไนท์มาร์เก็ตและทะเลสาบซวนเฮืองได้"), ("มัดจำ", "ฝากพาสปอร์ตหรือบัตรประชาชน ไม่มีมัดจำเงินสด"), ("คืนรถ", "คืนรถก่อน 21:00")],
 "เคล็ดลับ",
 ["ถามแผนกต้อนรับว่าจอดรถตรงไหนปลอดภัย", "โรงแรม 3 ดาวหลายแห่งไม่มีแอร์ — ดาลัดอากาศเย็น แต่ขอพัดลมได้ถ้าต้องการ", "ห้องติดถนนอาจเสียงดัง — ขอชั้นสูง", "ระดับดาวและราคาอาจเปลี่ยน — สอบถามโรงแรมตอนจอง"],
 [("Ngoc Phat Dalat Hotel", "ทั้งวัน", "โรงแรมตรงข้ามจัตุรัสลัมเวียน บางห้องเห็นวิวทะเลสาบ"),
  ("Iris Dalat Hotel", "ทั้งวัน", "โรงแรมบนถนนฟานนูทัค เดินไม่กี่นาทีถึงไนท์มาร์เก็ต"),
  ("Hotel Du Lys", "ทั้งวัน", "โรงแรมบนถนนนามกีคอยเงีย ใกล้ตลาดและร้านอาหาร"),
  ("Hotel Roy Dala", "ทั้งวัน", "ล็อบบี้หินอ่อน ห้องกว้าง เดินไปตลาดและทะเลสาบได้"),
  ("Marguerite Hotel", "ทั้งวัน", "ห้องกว้างบนถนนเหงียนชีทาน ตรงข้ามไนท์มาร์เก็ต"),
  ("Mai Vang Hotel", "ทั้งวัน", "โรงแรมเรียบง่ายบนถนนไห่เทือง ราว 5 นาทีถึงไนท์มาร์เก็ต"),
  ("Ky Hoa Garden Villages Hotel", "ทั้งวัน", "วิลล่าสไตล์ฝรั่งเศสมีสวน ทางเหนือของตัวเมือง"),
  ("Dalat De Charme Village", "พระอาทิตย์ตก", "ห้องพักตามธีมและสวนขั้นบันได ทางตะวันออกของตัวเมือง")])
T["id"] = _mk("Hotel Bintang 3 di Da Lat: Peta 8 Hotel Populer | Van Phu", "Peta Hotel Bintang 3 Da Lat",
 "Peta 8 hotel bintang 3 populer di Da Lat — kebanyakan dekat jalan kaki ke pasar malam dan Danau Xuan Huong — dengan petunjuk arah, jarak, dan PDF gratis.",
 "Inilah 8 hotel bintang 3 di Da Lat, masing-masing dengan lebih dari 250 ulasan Google Maps — enam di pusat dekat pasar malam dan dua yang lebih tenang tak jauh dari pusat — dengan petunjuk arah sekali ketuk.",
 "Di kota (1–8)", "Perlu diketahui",
 [("Antar motor", "kami antar motor ke hotel Anda di pusat kota untuk sewa 2 hari atau lebih"), ("Pusat kota (1–6)", "semuanya dekat jalan kaki ke pasar malam dan Danau Xuan Huong"), ("Jaminan", "paspor atau kartu identitas, tanpa deposit uang"), ("Pengembalian", "kembalikan motor sebelum 21:00")],
 "Tips",
 ["Tanyakan resepsionis tempat parkir motor yang aman.", "Banyak hotel bintang 3 tanpa AC — Da Lat sejuk, tapi mintalah kipas jika perlu.", "Kamar menghadap jalan bisa bising — mintalah lantai atas.", "Peringkat bintang dan harga bisa berubah — tanyakan hotel saat memesan."],
 [("Ngoc Phat Dalat Hotel", "Kapan saja", "Hotel di seberang Lapangan Lam Vien, sebagian kamar menghadap danau."),
  ("Iris Dalat Hotel", "Kapan saja", "Hotel di Jalan Phan Nhu Thach, beberapa menit jalan kaki ke pasar malam."),
  ("Hotel Du Lys", "Kapan saja", "Hotel di Jalan Nam Ky Khoi Nghia, dekat pasar dan tempat makan."),
  ("Hotel Roy Dala", "Kapan saja", "Lobi marmer dan kamar luas, jalan kaki ke pasar dan danau."),
  ("Marguerite Hotel", "Kapan saja", "Kamar luas di Jalan Nguyen Chi Thanh, di seberang pasar malam."),
  ("Mai Vang Hotel", "Kapan saja", "Hotel sederhana di Jalan Hai Thuong, sekitar 5 menit ke pasar malam."),
  ("Ky Hoa Garden Villages Hotel", "Kapan saja", "Vila bergaya Prancis dengan taman, di utara pusat kota."),
  ("Dalat De Charme Village", "Matahari terbenam", "Kamar bertema dan taman berteras, di timur pusat kota.")])
T["ms"] = _mk("Hotel 3 Bintang di Da Lat: Peta 8 Hotel Popular | Van Phu", "Peta Hotel 3 Bintang Da Lat",
 "Peta 8 hotel 3 bintang popular di Da Lat — kebanyakannya dekat berjalan kaki ke pasar malam dan Tasik Xuan Huong — dengan arah, jarak dan PDF percuma.",
 "Inilah 8 hotel 3 bintang di Da Lat, setiap satu dengan lebih 250 ulasan Google Maps — enam di pusat bandar dekat pasar malam dan dua yang lebih tenang tidak jauh dari pusat — dengan arah satu ketikan.",
 "Dalam bandar (1–8)", "Perlu tahu",
 [("Hantar motosikal", "kami hantar motosikal ke hotel anda di pusat bandar untuk sewa 2 hari atau lebih"), ("Pusat bandar (1–6)", "semuanya dekat berjalan kaki ke pasar malam dan Tasik Xuan Huong"), ("Cagaran", "pasport atau kad pengenalan, tiada deposit wang"), ("Pulangkan", "pulangkan motosikal sebelum 21:00")],
 "Tip",
 ["Tanya kaunter penyambut tetamu tempat letak motosikal yang selamat.", "Banyak hotel 3 bintang tiada penghawa dingin — Da Lat sejuk, tetapi minta kipas jika perlu.", "Bilik menghadap jalan boleh bising — minta tingkat atas.", "Penarafan bintang dan harga boleh berubah — semak dengan hotel semasa menempah."],
 [("Ngoc Phat Dalat Hotel", "Bila-bila masa", "Hotel bertentangan Dataran Lam Vien, sesetengah bilik menghadap tasik."),
  ("Iris Dalat Hotel", "Bila-bila masa", "Hotel di Jalan Phan Nhu Thach, beberapa minit berjalan kaki ke pasar malam."),
  ("Hotel Du Lys", "Bila-bila masa", "Hotel di Jalan Nam Ky Khoi Nghia, dekat pasar dan kedai makan."),
  ("Hotel Roy Dala", "Bila-bila masa", "Lobi marmar dan bilik luas, berjalan kaki ke pasar dan tasik."),
  ("Marguerite Hotel", "Bila-bila masa", "Bilik luas di Jalan Nguyen Chi Thanh, bertentangan pasar malam."),
  ("Mai Vang Hotel", "Bila-bila masa", "Hotel ringkas di Jalan Hai Thuong, kira-kira 5 minit ke pasar malam."),
  ("Ky Hoa Garden Villages Hotel", "Bila-bila masa", "Vila gaya Perancis dengan taman, di utara pusat bandar."),
  ("Dalat De Charme Village", "Matahari terbenam", "Bilik bertema dan taman bertingkat, di timur pusat bandar.")])
T["de"] = _mk("3-Sterne-Hotels in Da Lat: Karte mit 8 beliebten Hotels | Van Phu", "Karte der 3-Sterne-Hotels in Da Lat",
 "Karte von 8 beliebten 3-Sterne-Hotels in Da Lat — die meisten zu Fuß vom Nachtmarkt und vom Xuan-Huong-See — mit Route, Entfernung und kostenlosem PDF.",
 "Hier sind 8 Hotels mit 3 Sternen in Da Lat, jedes mit über 250 Google-Maps-Bewertungen — sechs im Zentrum nahe dem Nachtmarkt und zwei ruhigere etwas außerhalb — mit Route per Fingertipp.",
 "In der Stadt (1–8)", "Gut zu wissen",
 [("Lieferung", "ab 2 Miettagen bringen wir den Roller zu Ihrem Hotel im Zentrum"), ("Zentrum (1–6)", "alle zu Fuß vom Nachtmarkt und vom Xuan-Huong-See erreichbar"), ("Kaution", "Reisepass oder Ausweis, keine Geldkaution"), ("Rückgabe", "Roller bis 21:00 zurückbringen")],
 "Tipps",
 ["Fragen Sie an der Rezeption nach einem sicheren Parkplatz für den Roller.", "Viele 3-Sterne-Hotels haben keine Klimaanlage — Da Lat ist kühl, bei Bedarf nach einem Ventilator fragen.", "Zimmer zur Straße können laut sein — nach einem höheren Stockwerk fragen.", "Sterne und Preise können sich ändern — bei der Buchung beim Hotel nachfragen."],
 [("Ngoc Phat Dalat Hotel", "Jederzeit", "Hotel gegenüber dem Lam-Vien-Platz, manche Zimmer mit Seeblick."),
  ("Iris Dalat Hotel", "Jederzeit", "Hotel an der Phan-Nhu-Thach-Straße, wenige Gehminuten zum Nachtmarkt."),
  ("Hotel Du Lys", "Jederzeit", "Hotel an der Nam-Ky-Khoi-Nghia-Straße, nahe Markt und Restaurants."),
  ("Hotel Roy Dala", "Jederzeit", "Marmorlobby und große Zimmer, zu Fuß zum Markt und zum See."),
  ("Marguerite Hotel", "Jederzeit", "Geräumige Zimmer an der Nguyen-Chi-Thanh-Straße, gegenüber dem Nachtmarkt."),
  ("Mai Vang Hotel", "Jederzeit", "Einfaches Hotel an der Hai-Thuong-Straße, etwa 5 Minuten zum Nachtmarkt."),
  ("Ky Hoa Garden Villages Hotel", "Jederzeit", "Villen im französischen Stil mit Gärten, nördlich des Zentrums."),
  ("Dalat De Charme Village", "Sonnenuntergang", "Themenzimmer und Terrassengarten, östlich des Zentrums.")])
T["fr"] = _mk("Hôtels 3 étoiles à Da Lat : carte de 8 hôtels populaires | Van Phu", "Carte des hôtels 3 étoiles de Da Lat",
 "Carte de 8 hôtels 3 étoiles populaires à Da Lat — la plupart à pied du marché de nuit et du lac Xuan Huong — avec itinéraire, distances et PDF gratuit.",
 "Voici 8 hôtels classés 3 étoiles à Da Lat, chacun avec plus de 250 avis Google Maps — six au centre près du marché de nuit et deux plus calmes un peu à l'écart — avec itinéraire en un clic.",
 "En ville (1–8)", "Bon à savoir",
 [("Livraison", "nous livrons le scooter à votre hôtel du centre-ville pour 2 jours de location ou plus"), ("Centre (1–6)", "tous à pied du marché de nuit et du lac Xuan Huong"), ("Caution", "passeport ou carte d'identité, pas de caution en argent"), ("Retour", "rendez le scooter avant 21 h")],
 "Conseils",
 ["Demandez à la réception où garer le scooter en sécurité.", "Beaucoup d'hôtels 3 étoiles n'ont pas de climatisation — Da Lat est frais, demandez un ventilateur si besoin.", "Les chambres côté rue peuvent être bruyantes — demandez un étage élevé.", "Les étoiles et les prix peuvent changer — vérifiez auprès de l'hôtel à la réservation."],
 [("Ngoc Phat Dalat Hotel", "À tout moment", "Hôtel face à la place Lam Vien, certaines chambres avec vue sur le lac."),
  ("Iris Dalat Hotel", "À tout moment", "Hôtel rue Phan Nhu Thach, à quelques minutes à pied du marché de nuit."),
  ("Hotel Du Lys", "À tout moment", "Hôtel rue Nam Ky Khoi Nghia, près du marché et des restaurants."),
  ("Hotel Roy Dala", "À tout moment", "Hall en marbre et grandes chambres, à pied du marché et du lac."),
  ("Marguerite Hotel", "À tout moment", "Chambres spacieuses rue Nguyen Chi Thanh, face au marché de nuit."),
  ("Mai Vang Hotel", "À tout moment", "Hôtel simple rue Hai Thuong, à environ 5 minutes du marché de nuit."),
  ("Ky Hoa Garden Villages Hotel", "À tout moment", "Villas de style français avec jardins, au nord du centre."),
  ("Dalat De Charme Village", "Coucher du soleil", "Chambres à thème et jardin en terrasses, à l'est du centre.")])
T["es"] = _mk("Hoteles de 3 estrellas en Da Lat: mapa de 8 hoteles populares | Van Phu", "Mapa de hoteles 3 estrellas de Da Lat",
 "Mapa de 8 hoteles de 3 estrellas populares en Da Lat — la mayoría a pie del mercado nocturno y del lago Xuan Huong — con cómo llegar, distancias y PDF gratis.",
 "Aquí tienes 8 hoteles de 3 estrellas en Da Lat, cada uno con más de 250 reseñas en Google Maps — seis en el centro cerca del mercado nocturno y dos más tranquilos a poca distancia — con ruta en un toque.",
 "En la ciudad (1–8)", "Bueno saber",
 [("Entrega", "llevamos la moto a tu hotel del centro en alquileres de 2 días o más"), ("Centro (1–6)", "todos a pie del mercado nocturno y del lago Xuan Huong"), ("Garantía", "pasaporte o documento de identidad, sin depósito en efectivo"), ("Devolución", "devuelve la moto antes de las 21:00")],
 "Consejos",
 ["Pregunta en recepción dónde aparcar la moto con seguridad.", "Muchos hoteles de 3 estrellas no tienen aire acondicionado — Da Lat es fresco, pide un ventilador si lo necesitas.", "Las habitaciones a la calle pueden ser ruidosas — pide un piso alto.", "Las estrellas y los precios pueden cambiar — confírmalo con el hotel al reservar."],
 [("Ngoc Phat Dalat Hotel", "Cualquier hora", "Hotel frente a la plaza Lam Vien, algunas habitaciones con vista al lago."),
  ("Iris Dalat Hotel", "Cualquier hora", "Hotel en la calle Phan Nhu Thach, a pocos minutos a pie del mercado nocturno."),
  ("Hotel Du Lys", "Cualquier hora", "Hotel en la calle Nam Ky Khoi Nghia, cerca del mercado y de restaurantes."),
  ("Hotel Roy Dala", "Cualquier hora", "Vestíbulo de mármol y habitaciones grandes, a pie del mercado y del lago."),
  ("Marguerite Hotel", "Cualquier hora", "Habitaciones amplias en la calle Nguyen Chi Thanh, frente al mercado nocturno."),
  ("Mai Vang Hotel", "Cualquier hora", "Hotel sencillo en la calle Hai Thuong, a unos 5 minutos del mercado nocturno."),
  ("Ky Hoa Garden Villages Hotel", "Cualquier hora", "Villas de estilo francés con jardines, al norte del centro."),
  ("Dalat De Charme Village", "Atardecer", "Habitaciones temáticas y jardín en terrazas, al este del centro.")])
T["he"] = _mk("מלונות 3 כוכבים בדלאט: מפה של 8 מלונות פופולריים | Van Phu", "מפת מלונות 3 כוכבים בדלאט",
 "מפה של 8 מלונות פופולריים בדירוג 3 כוכבים בדלאט — רובם במרחק הליכה משוק הלילה ומאגם שואן הואנג — עם ניווט, מרחקים ו-PDF בחינם.",
 "הנה 8 מלונות בדירוג 3 כוכבים בדלאט, לכל אחד יותר מ-250 ביקורות ב-Google Maps — שישה במרכז ליד שוק הלילה ושניים שקטים יותר במרחק נסיעה קצרה — עם ניווט בלחיצה אחת.",
 "בעיר (1–8)", "כדאי לדעת",
 [("משלוח", "בהשכרה של יומיים ומעלה נביא את הקטנוע למלון שלכם במרכז העיר"), ("מרכז (1–6)", "כולם במרחק הליכה משוק הלילה ומאגם שואן הואנג"), ("ערבון", "דרכון או תעודת זהות, בלי פיקדון כספי"), ("החזרה", "מחזירים את הקטנוע עד 21:00")],
 "טיפים",
 ["שאלו בקבלה איפה לחנות את הקטנוע בבטחה.", "בהרבה מלונות 3 כוכבים אין מזגן — בדלאט קריר, אבל אפשר לבקש מאוורר.", "חדרים לכיוון הרחוב עלולים להיות רועשים — בקשו קומה גבוהה.", "דירוג הכוכבים והמחירים משתנים — בדקו מול המלון בהזמנה."],
 [("Ngoc Phat Dalat Hotel", "בכל שעה", "מלון מול כיכר לאם וייאן, בחלק מהחדרים נוף לאגם."),
  ("Iris Dalat Hotel", "בכל שעה", "מלון ברחוב פאן נו טאך, כמה דקות הליכה משוק הלילה."),
  ("Hotel Du Lys", "בכל שעה", "מלון ברחוב נאם קי חוי נגיה, ליד השוק והמסעדות."),
  ("Hotel Roy Dala", "בכל שעה", "לובי שיש וחדרים גדולים, במרחק הליכה מהשוק והאגם."),
  ("Marguerite Hotel", "בכל שעה", "חדרים מרווחים ברחוב נגוין צ'י טאן, מול שוק הלילה."),
  ("Mai Vang Hotel", "בכל שעה", "מלון פשוט ברחוב האי טואנג, כ-5 דקות משוק הלילה."),
  ("Ky Hoa Garden Villages Hotel", "בכל שעה", "וילות בסגנון צרפתי עם גינות, צפונית למרכז."),
  ("Dalat De Charme Village", "שקיעה", "חדרים בעיצוב נושאי וגינה מדורגת, מזרחית למרכז.")])

from content._langs import inject as _inject
_inject(T, __name__)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"ngocphat": "Khách sạn Ngọc Phát", "iris": "Iris Dalat Hotel", "dulys": "Hotel Du Lys", "roydala": "Hotel Roy Dala",
      "marguerite": "Marguerite Hotel", "maivang": "Khách sạn Mai Vàng", "kyhoa": "Khách sạn Kỳ Hòa Garden Villages",
      "decharme": "Dalat De Charme Village"}
def img_link(sid):
    """Temporary photo link: Google Images search for the hotel name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
