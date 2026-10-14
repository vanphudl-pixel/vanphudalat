"""Da Lat pagoda map — shared data for the website page (/pagoda-map/) and the printable PDF.
Coordinates, Google Maps place links (cid) and opening hours were taken from Google Maps on 2026-10-14.
Shared labels (directions, hours, legend, CTA, address…) are reused from the photo-spot map."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (same codes as photomap)
SPOTS = [
    ("linhson",   11.9501694, 108.4369535, "2581877261277069505",  True,  "6:00–20:00"),
    ("linhquang", 11.9570621, 108.4288801, "12634339505252222746", True,  "5:30–17:00"),
    ("tau",       11.9277614, 108.4602955, "2397042529089527415",  True,  "7:00–17:00"),
    ("vanhanh",   11.9637059, 108.4441437, "7233034912285308646",  True,  "7:00–19:00"),
    ("truclam",   11.9036292, 108.4357112, "1492183853484664151",  True,  "7:00–17:00"),
    ("linhphuoc", 11.9446332, 108.4993224, "2344460066184159003",  True,  "day"),
    ("linhan",    11.8244336, 108.3335918, "3417370834740725284",  False, "5:00–17:00"),
]
CENTER = _PM.CENTER
SLUG = "pagoda-map"
PDF = "VanPhu-Dalat-Pagoda-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Da Lat Pagoda Map: 7 Temples Worth Visiting | Van Phu", "Da Lat Pagoda Map",
 "Map of the 7 most-visited pagodas and Zen monasteries in Da Lat with opening hours, best time to go and directions — plus a free printable PDF.",
 "The 7 pagodas and Zen monasteries travellers visit most in and around Da Lat — with opening hours, the best time to go and one-tap directions. Ride there yourself by scooter.",
 "City pagodas (1–6)", "Temple etiquette",
 [("Dress", "cover shoulders and knees; no shorts in the main halls"), ("Shoes", "take them off before entering a hall"), ("Quiet", "speak softly and ask before photographing monks"), ("Entry", "most pagodas are free; a donation box is optional")],
 "Route ideas",
 ["North loop: Linh Son → Linh Quang → Van Hanh (about 1.5 hours).", "South: Chua Tau, then Truc Lam above Tuyen Lam Lake.", "East: Linh Phuoc — or take the old train to Trai Mat.", "Linh An is next to Elephant Falls: go by Honda Air Blade 125cc."],
 [("Linh Son Pagoda", "Early morning", "Old pagoda among pine trees, right in town and calm."),
  ("Linh Quang Pagoda", "Morning", "Small pagoda full of statues and a dragon around a pond; few tourists."),
  ("Chua Tau (Thien Vuong Co Sat)", "Morning", "Chinese-style pagoda with a white Buddha on a pine hill."),
  ("Van Hanh Zen Monastery (Golden Buddha)", "Afternoon", "Large golden Buddha statues and a view over the city."),
  ("Truc Lam Zen Monastery", "Early morning", "Above Tuyen Lam Lake with lovely gardens; cable car from Robin Hill."),
  ("Linh Phuoc Pagoda (Bottle Pagoda)", "Morning", "Dragon and towers covered in pottery and glass mosaic; climb the bell tower."),
  ("Linh An Pagoda (Nam Ban)", "Morning", "Next to Elephant Falls; you can climb inside the tall Buddha statue.")])
T["vi"] = _mk("Bản đồ chùa Đà Lạt: 7 ngôi chùa nên ghé | Văn Phú", "Bản đồ chùa Đà Lạt",
 "Bản đồ 7 ngôi chùa và thiền viện được khách ghé nhiều nhất Đà Lạt: giờ mở cửa, giờ đẹp, chỉ đường Google Maps — tải miễn phí bản PDF.",
 "7 ngôi chùa và thiền viện khách hay ghé nhất trong và quanh Đà Lạt, có giờ mở cửa, giờ đẹp và nút chỉ đường. Tự chạy xe máy đến từng nơi.",
 "Chùa trong thành phố (1–6)", "Lưu ý khi đi chùa",
 [("Trang phục", "che vai và gối; không mặc quần short vào chánh điện"), ("Giày dép", "cởi ra trước khi vào điện thờ"), ("Giữ yên lặng", "nói nhỏ, hỏi trước khi chụp ảnh các thầy"), ("Vé vào", "hầu hết miễn phí; công đức tùy tâm")],
 "Gợi ý lộ trình",
 ["Vòng phía bắc: Linh Sơn → Linh Quang → Vạn Hạnh (khoảng 1,5 giờ).", "Phía nam: Chùa Tàu rồi Thiền viện Trúc Lâm trên hồ Tuyền Lâm.", "Phía đông: Linh Phước — hoặc đi tàu cổ xuống Trại Mát.", "Linh Ẩn nằm cạnh thác Voi: nên đi Honda Air Blade 125cc."],
 [("Chùa Linh Sơn", "Sáng sớm", "Chùa cổ giữa rừng thông, ngay trung tâm, yên tĩnh."),
  ("Chùa Linh Quang", "Buổi sáng", "Chùa nhỏ nhiều tượng, rồng quanh hồ nước; ít khách du lịch."),
  ("Chùa Tàu (Thiên Vương Cổ Sát)", "Buổi sáng", "Kiến trúc kiểu Hoa, tượng Phật trắng trên đồi thông."),
  ("Thiền viện Vạn Hạnh (Phật Vàng)", "Buổi chiều", "Tượng Phật vàng lớn, nhìn xuống thành phố."),
  ("Thiền viện Trúc Lâm", "Sáng sớm", "Trên hồ Tuyền Lâm, vườn hoa đẹp; có cáp treo từ đồi Robin."),
  ("Chùa Linh Phước (chùa Ve Chai)", "Buổi sáng", "Rồng và tháp khảm sành sứ, mảnh chai; leo được tháp chuông."),
  ("Chùa Linh Ẩn (Nam Ban)", "Buổi sáng", "Cạnh thác Voi; có thể leo lên bên trong tượng Phật cao.")])
T["ru"] = _mk("Карта пагод Далата: 7 храмов, которые стоит посетить | Van Phu", "Карта пагод Далата",
 "Карта 7 самых посещаемых пагод и дзен-монастырей Далата: часы работы, лучшее время и маршрут в Google Maps — плюс бесплатная PDF-карта.",
 "7 пагод и дзен-монастырей, куда чаще всего ездят туристы в Далате и окрестностях, — с часами работы, лучшим временем и маршрутом в одно касание. Доезжайте сами на байке.",
 "Пагоды в городе (1–6)", "Как вести себя в храме",
 [("Одежда", "закрытые плечи и колени; в главный зал — без шорт"), ("Обувь", "снимайте перед входом в зал"), ("Тишина", "говорите тихо, спрашивайте, прежде чем фотографировать монахов"), ("Вход", "в большинство пагод бесплатно; пожертвование по желанию")],
 "Идеи маршрутов",
 ["Север: Линьшон → Линькуанг → Ванхань (около 1,5 часа).", "Юг: Чуа Тау, затем Чуклам над озером Туйенлам.", "Восток: Линьфыок — или на старом поезде до Чаймат.", "Линьан рядом с водопадом Слонов: езжайте на Honda Air Blade 125cc."],
 [("Пагода Линьшон", "Раннее утро", "Старая пагода среди сосен, прямо в городе и тихая."),
  ("Пагода Линькуанг", "Утро", "Небольшая пагода со множеством статуй и драконом у пруда; туристов мало."),
  ("Чуа Тау (Тхиен Выонг Ко Сат)", "Утро", "Пагода в китайском стиле с белым Буддой на сосновом холме."),
  ("Дзен-монастырь Ванхань (Золотой Будда)", "После обеда", "Большие золотые статуи Будды и вид на город."),
  ("Дзен-монастырь Чуклам", "Раннее утро", "Над озером Туйенлам, красивые сады; канатная дорога с холма Робин."),
  ("Пагода Линьфыок («бутылочная»)", "Утро", "Дракон и башни из мозаики керамики и стекла; можно подняться на колокольню."),
  ("Пагода Линьан (Намбан)", "Утро", "Рядом с водопадом Слонов; можно подняться внутрь высокой статуи Будды.")])
T["zh"] = _mk("大叻寺庙地图：7座值得一去的寺院 | Van Phu", "大叻寺庙地图",
 "大叻游客最常去的7座寺庙和禅院地图：开放时间、最佳时段和 Google 地图导航——还可免费下载 PDF。",
 "大叻市区及周边游客最常去的7座寺庙和禅院，附开放时间、最佳时段和一键导航。骑摩托车自己去。",
 "市区寺庙（1–6）", "参观寺庙礼仪",
 [("着装", "遮住肩膀和膝盖；不要穿短裤进大殿"), ("鞋子", "进殿前脱鞋"), ("安静", "小声说话，拍僧人前先询问"), ("门票", "大多数寺庙免费；功德箱随意")],
 "路线建议",
 ["北线：灵山寺 → 灵光寺 → 万行禅院（约1.5小时）。", "南线：天王古刹（中国寺），再去竹林禅院，俯瞰宣林湖。", "东线：灵福寺——或坐老火车去 Trai Mat。", "灵隐寺在大象瀑布旁：建议骑 Honda Air Blade 125cc。"],
 [("灵山寺 Linh Son", "清晨", "松林中的老寺，就在市中心，十分安静。"),
  ("灵光寺 Linh Quang", "上午", "小寺庙，佛像众多，池边有龙；游客很少。"),
  ("天王古刹（中国寺）", "上午", "中式建筑，松林山坡上有白色佛像。"),
  ("万行禅院（金佛寺）", "下午", "巨大的金色佛像，可俯瞰城市。"),
  ("竹林禅院 Truc Lam", "清晨", "位于宣林湖上方，花园很美；可从 Robin 山坐缆车。"),
  ("灵福寺（瓶子寺）", "上午", "用陶瓷和玻璃碎片镶嵌的龙和塔；可登钟楼。"),
  ("灵隐寺 Linh An（南班）", "上午", "紧邻大象瀑布；可登上高大佛像内部。")])
T["ko"] = _mk("달랏 사원 지도: 꼭 가볼 만한 사찰 7곳 | Van Phu", "달랏 사원 지도",
 "여행자가 가장 많이 찾는 달랏 사찰·선원 7곳 지도: 운영 시간, 추천 시간대, Google 지도 길찾기 — 무료 PDF도 있습니다.",
 "달랏 시내와 근교에서 여행자가 가장 많이 찾는 사찰과 선원 7곳. 운영 시간, 추천 시간대, 원터치 길찾기까지. 스쿠터로 직접 가 보세요.",
 "시내 사찰 (1–6)", "사찰 방문 예절",
 [("복장", "어깨와 무릎을 가리고, 본당에는 반바지 금지"), ("신발", "법당에 들어가기 전에 벗기"), ("정숙", "조용히 말하고, 스님 촬영 전 먼저 묻기"), ("입장", "대부분 무료, 시주는 자유")],
 "추천 코스",
 ["북쪽: 린선 → 린꽝 → 반하잉 (약 1.5시간).", "남쪽: 쭈아 따우 다음 뚜옌럼 호수 위 쭉럼 선원.", "동쪽: 린프억 — 또는 옛 기차로 짜이맛까지.", "린안 사원은 코끼리 폭포 옆: 혼다 에어블레이드 125cc 추천."],
 [("린선 사원", "이른 아침", "시내 한가운데 소나무 숲 속의 오래되고 조용한 사찰."),
  ("린꽝 사원", "오전", "불상이 많고 연못가에 용이 있는 작은 사찰, 관광객이 적음."),
  ("쭈아 따우 (티엔브엉꼬삿)", "오전", "중국식 건축, 소나무 언덕 위 흰 불상."),
  ("반하잉 선원 (황금 불상)", "오후", "거대한 황금 불상과 도시 전망."),
  ("쭉럼 선원", "이른 아침", "뚜옌럼 호수 위, 아름다운 정원; 로빈 언덕에서 케이블카."),
  ("린프억 사원 (병 사원)", "오전", "도자기와 유리 조각 모자이크로 된 용과 탑; 종탑에 오를 수 있음."),
  ("린안 사원 (남반)", "오전", "코끼리 폭포 바로 옆; 큰 불상 안으로 올라갈 수 있음.")])
T["ja"] = _mk("ダラット寺院マップ：訪れたい7つのお寺 | Van Phu", "ダラット寺院マップ",
 "ダラットで旅行者がよく訪れる7つの寺院・禅院のマップ：開門時間、おすすめの時間帯、Googleマップの道案内 — 無料PDFもあります。",
 "ダラット市内と近郊で旅行者が最も訪れる7つの寺院と禅院。開門時間、おすすめの時間帯、ワンタップ道案内付き。スクーターで自分で行けます。",
 "市内の寺院（1–6）", "お寺でのマナー",
 [("服装", "肩と膝を隠す。本堂に短パンはNG"), ("靴", "お堂に入る前に脱ぐ"), ("静かに", "小声で話し、僧侶の撮影は先に一声かける"), ("拝観", "ほとんど無料。お布施は任意")],
 "おすすめルート",
 ["北ルート：リンソン → リンクアン → ヴァンハイン（約1.5時間）。", "南ルート：チュア・タウからトゥエンラム湖の上の竹林禅院へ。", "東ルート：リンフオック — 古い列車でチャイマットへ行くのも◎。", "リンアン寺は象の滝の隣：ホンダ エアブレード125ccで。"],
 [("リンソン寺", "早朝", "市内の松林にある古いお寺。静かで落ち着きます。"),
  ("リンクアン寺", "午前", "仏像が多く、池のまわりに龍がいる小さなお寺。観光客は少なめ。"),
  ("チュア・タウ（天王古刹）", "午前", "中国風の建築。松の丘に白い仏像。"),
  ("ヴァンハイン禅院（黄金の大仏）", "午後", "大きな金色の仏像と市街の眺め。"),
  ("竹林禅院", "早朝", "トゥエンラム湖を見下ろし、庭園がきれい。ロビンの丘からロープウェイも。"),
  ("リンフオック寺（瓶の寺）", "午前", "陶器とガラスのモザイクの龍と塔。鐘楼に登れます。"),
  ("リンアン寺（ナムバン）", "午前", "象の滝のすぐ隣。大きな仏像の中を登れます。")])
T["th"] = _mk("แผนที่วัดดาลัด: 7 วัดที่ควรไป | Van Phu", "แผนที่วัดดาลัด",
 "แผนที่ 7 วัดและวัดเซนที่นักท่องเที่ยวไปมากที่สุดในดาลัด พร้อมเวลาเปิด ช่วงเวลาที่ดีที่สุด และเส้นทาง Google Maps — ดาวน์โหลด PDF ฟรี",
 "7 วัดและวัดเซนที่นักท่องเที่ยวไปมากที่สุดในและรอบดาลัด พร้อมเวลาเปิด ช่วงเวลาที่ดีที่สุด และนำทางแตะเดียว ขี่สกู๊ตเตอร์ไปเองได้",
 "วัดในเมือง (1–6)", "มารยาทในการไปวัด",
 [("การแต่งกาย", "ปิดไหล่และเข่า ห้ามใส่กางเกงขาสั้นเข้าโบสถ์"), ("รองเท้า", "ถอดก่อนเข้าโบสถ์"), ("ความสงบ", "พูดเบา ๆ และขออนุญาตก่อนถ่ายรูปพระ"), ("ค่าเข้า", "ส่วนใหญ่ฟรี ทำบุญได้ตามศรัทธา")],
 "ไอเดียเส้นทาง",
 ["สายเหนือ: ลินห์เซิน → ลินห์กวาง → วันฮันห์ (ประมาณ 1.5 ชม.)", "สายใต้: วัดจีน (ChuaTau) แล้วต่อวัดจั๊กเลิมเหนือทะเลสาบเตวียนเลิม", "สายตะวันออก: วัดลินห์เฟือก — หรือนั่งรถไฟโบราณไป Trai Mat", "วัดลินห์อานอยู่ติดน้ำตกช้าง: ควรขี่ Honda Air Blade 125cc"],
 [("วัดลินห์เซิน", "เช้าตรู่", "วัดเก่ากลางป่าสน อยู่ใจกลางเมืองและเงียบสงบ"),
  ("วัดลินห์กวาง", "ช่วงเช้า", "วัดเล็ก ๆ มีรูปปั้นมากมายและมังกรรอบสระน้ำ นักท่องเที่ยวน้อย"),
  ("วัดจีน (เทียนเวืองโกซาต)", "ช่วงเช้า", "สถาปัตยกรรมแบบจีน พระพุทธรูปสีขาวบนเนินสน"),
  ("วัดเซนวันฮันห์ (พระพุทธรูปทองคำ)", "ช่วงบ่าย", "พระพุทธรูปทองคำองค์ใหญ่ มองเห็นวิวเมือง"),
  ("วัดเซนจั๊กเลิม", "เช้าตรู่", "อยู่เหนือทะเลสาบเตวียนเลิม สวนสวย ขึ้นกระเช้าจากเนิน Robin ได้"),
  ("วัดลินห์เฟือก (วัดขวด)", "ช่วงเช้า", "มังกรและเจดีย์ประดับโมเสกเซรามิกและแก้ว ขึ้นหอระฆังได้"),
  ("วัดลินห์อาน (นามบาน)", "ช่วงเช้า", "ติดน้ำตกช้าง ขึ้นไปด้านในพระพุทธรูปองค์สูงได้")])
T["id"] = _mk("Peta Pagoda Da Lat: 7 Kuil yang Layak Dikunjungi | Van Phu", "Peta Pagoda Da Lat",
 "Peta 7 pagoda dan biara Zen yang paling sering dikunjungi di Da Lat: jam buka, waktu terbaik dan petunjuk arah Google Maps — plus PDF gratis.",
 "7 pagoda dan biara Zen yang paling sering dikunjungi wisatawan di dalam dan sekitar Da Lat — lengkap dengan jam buka, waktu terbaik dan petunjuk arah sekali ketuk. Datangi sendiri dengan motor.",
 "Pagoda di kota (1–6)", "Etika di pagoda",
 [("Pakaian", "tutup bahu dan lutut; jangan bercelana pendek di aula utama"), ("Alas kaki", "lepas sebelum masuk aula"), ("Tenang", "bicara pelan, minta izin sebelum memotret biksu"), ("Masuk", "sebagian besar gratis; donasi sukarela")],
 "Ide rute",
 ["Utara: Linh Son → Linh Quang → Van Hanh (sekitar 1,5 jam).", "Selatan: Chua Tau, lalu Truc Lam di atas Danau Tuyen Lam.", "Timur: Linh Phuoc — atau naik kereta tua ke Trai Mat.", "Linh An ada di samping Air Terjun Gajah: naik Honda Air Blade 125cc."],
 [("Pagoda Linh Son", "Pagi-pagi", "Pagoda tua di antara pohon pinus, di tengah kota dan tenang."),
  ("Pagoda Linh Quang", "Pagi", "Pagoda kecil penuh patung dan naga di sekeliling kolam; sepi wisatawan."),
  ("Chua Tau (Thien Vuong Co Sat)", "Pagi", "Bergaya Tionghoa dengan Buddha putih di bukit pinus."),
  ("Biara Zen Van Hanh (Buddha Emas)", "Sore", "Patung Buddha emas besar dan pemandangan kota."),
  ("Biara Zen Truc Lam", "Pagi-pagi", "Di atas Danau Tuyen Lam, taman indah; kereta gantung dari Bukit Robin."),
  ("Pagoda Linh Phuoc (Pagoda Botol)", "Pagi", "Naga dan menara bermozaik keramik dan kaca; bisa naik menara lonceng."),
  ("Pagoda Linh An (Nam Ban)", "Pagi", "Di samping Air Terjun Gajah; bisa naik ke dalam patung Buddha tinggi.")])
T["ms"] = _mk("Peta Pagoda Da Lat: 7 Kuil yang Wajar Dilawati | Van Phu", "Peta Pagoda Da Lat",
 "Peta 7 pagoda dan biara Zen paling popular di Da Lat: waktu buka, masa terbaik dan arah Google Maps — serta PDF percuma.",
 "7 pagoda dan biara Zen yang paling kerap dilawati pelancong di dalam dan sekitar Da Lat — dengan waktu buka, masa terbaik dan arah sekali sentuh. Tunggang skuter sendiri ke sana.",
 "Pagoda dalam bandar (1–6)", "Adab di pagoda",
 [("Pakaian", "tutup bahu dan lutut; jangan berseluar pendek di dewan utama"), ("Kasut", "tanggalkan sebelum masuk dewan"), ("Senyap", "bercakap perlahan, minta izin sebelum mengambil gambar sami"), ("Masuk", "kebanyakan percuma; derma ikut kerelaan")],
 "Cadangan laluan",
 ["Utara: Linh Son → Linh Quang → Van Hanh (kira-kira 1.5 jam).", "Selatan: Chua Tau, kemudian Truc Lam di atas Tasik Tuyen Lam.", "Timur: Linh Phuoc — atau naik kereta api lama ke Trai Mat.", "Linh An di sebelah Air Terjun Gajah: tunggang Honda Air Blade 125cc."],
 [("Pagoda Linh Son", "Awal pagi", "Pagoda lama di antara pokok pain, di tengah bandar dan tenang."),
  ("Pagoda Linh Quang", "Pagi", "Pagoda kecil dengan banyak patung dan naga di sekeliling kolam; kurang pelancong."),
  ("Chua Tau (Thien Vuong Co Sat)", "Pagi", "Seni bina gaya Cina dengan Buddha putih di bukit pain."),
  ("Biara Zen Van Hanh (Buddha Emas)", "Petang", "Patung Buddha emas yang besar dan pemandangan bandar."),
  ("Biara Zen Truc Lam", "Awal pagi", "Di atas Tasik Tuyen Lam, taman cantik; kereta kabel dari Bukit Robin."),
  ("Pagoda Linh Phuoc (Pagoda Botol)", "Pagi", "Naga dan menara bermozek seramik dan kaca; boleh naik menara loceng."),
  ("Pagoda Linh An (Nam Ban)", "Pagi", "Di sebelah Air Terjun Gajah; boleh naik ke dalam patung Buddha yang tinggi.")])
T["de"] = _mk("Pagoden-Karte Da Lat: 7 Tempel, die sich lohnen | Van Phu", "Pagoden-Karte Da Lat",
 "Karte der 7 meistbesuchten Pagoden und Zen-Klöster in Da Lat mit Öffnungszeiten, bester Besuchszeit und Google-Maps-Route – plus kostenloses PDF.",
 "Die 7 Pagoden und Zen-Klöster, die Reisende in und um Da Lat am häufigsten besuchen – mit Öffnungszeiten, bester Zeit und Route per Fingertipp. Fahren Sie selbst mit dem Roller hin.",
 "Pagoden in der Stadt (1–6)", "Verhalten im Tempel",
 [("Kleidung", "Schultern und Knie bedecken; keine Shorts in den Haupthallen"), ("Schuhe", "vor dem Betreten einer Halle ausziehen"), ("Ruhe", "leise sprechen, vor Fotos von Mönchen fragen"), ("Eintritt", "meist kostenlos; Spende freiwillig")],
 "Routen-Ideen",
 ["Norden: Linh Son → Linh Quang → Van Hanh (ca. 1,5 Stunden).", "Süden: Chua Tau, dann Truc Lam über dem Tuyen-Lam-See.", "Osten: Linh Phuoc – oder mit dem alten Zug nach Trai Mat.", "Linh An liegt neben dem Elefantenwasserfall: mit der Honda Air Blade 125cc."],
 [("Linh-Son-Pagode", "Früher Morgen", "Alte Pagode zwischen Kiefern, mitten in der Stadt und ruhig."),
  ("Linh-Quang-Pagode", "Vormittag", "Kleine Pagode mit vielen Statuen und einem Drachen am Teich; wenige Touristen."),
  ("Chua Tau (Thien Vuong Co Sat)", "Vormittag", "Pagode im chinesischen Stil mit weißem Buddha auf einem Kiefernhügel."),
  ("Zen-Kloster Van Hanh (Goldener Buddha)", "Nachmittag", "Große goldene Buddhastatuen und Blick über die Stadt."),
  ("Zen-Kloster Truc Lam", "Früher Morgen", "Über dem Tuyen-Lam-See mit schönen Gärten; Seilbahn vom Robin-Hügel."),
  ("Linh-Phuoc-Pagode (Flaschenpagode)", "Vormittag", "Drache und Türme aus Keramik- und Glasmosaik; Glockenturm begehbar."),
  ("Linh-An-Pagode (Nam Ban)", "Vormittag", "Direkt am Elefantenwasserfall; man kann im hohen Buddha hinaufsteigen.")])
T["fr"] = _mk("Carte des pagodes de Da Lat : 7 temples à voir | Van Phu", "Carte des pagodes de Da Lat",
 "Carte des 7 pagodes et monastères zen les plus visités de Da Lat : horaires, meilleur moment et itinéraire Google Maps — plus un PDF gratuit.",
 "Les 7 pagodes et monastères zen que les voyageurs visitent le plus à Da Lat et autour — avec horaires, meilleur moment et itinéraire en un clic. Allez-y vous-même en scooter.",
 "Pagodes en ville (1–6)", "Savoir-vivre au temple",
 [("Tenue", "épaules et genoux couverts ; pas de short dans les salles principales"), ("Chaussures", "à retirer avant d'entrer dans une salle"), ("Calme", "parlez bas et demandez avant de photographier les moines"), ("Entrée", "gratuite la plupart du temps ; don libre")],
 "Idées d'itinéraires",
 ["Nord : Linh Son → Linh Quang → Van Hanh (environ 1 h 30).", "Sud : Chua Tau, puis Truc Lam au-dessus du lac Tuyen Lam.", "Est : Linh Phuoc — ou le vieux train jusqu'à Trai Mat.", "Linh An est à côté des chutes de l'Éléphant : en Honda Air Blade 125cc."],
 [("Pagode Linh Son", "Tôt le matin", "Vieille pagode parmi les pins, en pleine ville et paisible."),
  ("Pagode Linh Quang", "Matin", "Petite pagode pleine de statues avec un dragon autour d'un bassin ; peu de touristes."),
  ("Chua Tau (Thien Vuong Co Sat)", "Matin", "Pagode de style chinois avec un Bouddha blanc sur une colline de pins."),
  ("Monastère zen Van Hanh (Bouddha d'or)", "Après-midi", "Grandes statues de Bouddha dorées et vue sur la ville."),
  ("Monastère zen Truc Lam", "Tôt le matin", "Au-dessus du lac Tuyen Lam, beaux jardins ; téléphérique depuis la colline Robin."),
  ("Pagode Linh Phuoc (pagode des bouteilles)", "Matin", "Dragon et tours en mosaïque de céramique et de verre ; clocher accessible."),
  ("Pagode Linh An (Nam Ban)", "Matin", "Juste à côté des chutes de l'Éléphant ; on peut monter à l'intérieur du grand Bouddha.")])
T["es"] = _mk("Mapa de pagodas de Da Lat: 7 templos que merecen la pena | Van Phu", "Mapa de pagodas de Da Lat",
 "Mapa de las 7 pagodas y monasterios zen más visitados de Da Lat: horarios, mejor momento y ruta en Google Maps, más un PDF gratis.",
 "Las 7 pagodas y monasterios zen que más visitan los viajeros en Da Lat y alrededores, con horarios, mejor momento y ruta con un toque. Ve tú mismo en scooter.",
 "Pagodas en la ciudad (1–6)", "Normas en el templo",
 [("Ropa", "hombros y rodillas cubiertos; sin pantalón corto en las salas principales"), ("Calzado", "quítatelo antes de entrar en una sala"), ("Silencio", "habla bajo y pregunta antes de fotografiar a los monjes"), ("Entrada", "casi siempre gratis; donativo voluntario")],
 "Ideas de ruta",
 ["Norte: Linh Son → Linh Quang → Van Hanh (aprox. 1,5 horas).", "Sur: Chua Tau y después Truc Lam sobre el lago Tuyen Lam.", "Este: Linh Phuoc, o el tren antiguo hasta Trai Mat.", "Linh An está junto a la cascada del Elefante: ve en Honda Air Blade 125cc."],
 [("Pagoda Linh Son", "A primera hora", "Pagoda antigua entre pinos, en plena ciudad y tranquila."),
  ("Pagoda Linh Quang", "Mañana", "Pagoda pequeña llena de estatuas y un dragón alrededor de un estanque; pocos turistas."),
  ("Chua Tau (Thien Vuong Co Sat)", "Mañana", "Pagoda de estilo chino con un Buda blanco en una colina de pinos."),
  ("Monasterio zen Van Hanh (Buda Dorado)", "Tarde", "Grandes estatuas de Buda doradas y vistas de la ciudad."),
  ("Monasterio zen Truc Lam", "A primera hora", "Sobre el lago Tuyen Lam, jardines preciosos; teleférico desde la colina Robin."),
  ("Pagoda Linh Phuoc (pagoda de las botellas)", "Mañana", "Dragón y torres con mosaico de cerámica y vidrio; se puede subir al campanario."),
  ("Pagoda Linh An (Nam Ban)", "Mañana", "Junto a la cascada del Elefante; se puede subir por dentro del gran Buda.")])
T["he"] = _mk("מפת המקדשים של דלאט: 7 פגודות ששווה לבקר | Van Phu", "מפת המקדשים של דלאט",
 "מפה של 7 הפגודות ומנזרי הזן המתויירים ביותר בדלאט: שעות פתיחה, הזמן הכי טוב וניווט ב-Google Maps — ועוד PDF בחינם.",
 "7 הפגודות ומנזרי הזן שמטיילים מבקרים בהם הכי הרבה בדלאט ובסביבה — עם שעות פתיחה, הזמן הכי טוב וניווט בלחיצה אחת. סעו לבד עם קטנוע.",
 "פגודות בעיר (1–6)", "כללי התנהגות במקדש",
 [("לבוש", "כתפיים וברכיים מכוסות; בלי מכנסיים קצרים באולמות המרכזיים"), ("נעליים", "חולצים לפני הכניסה לאולם"), ("שקט", "מדברים בשקט ושואלים לפני שמצלמים נזירים"), ("כניסה", "ברוב המקומות חינם; תרומה לפי רצון")],
 "רעיונות למסלול",
 ["צפון: לין שון → לין קוואנג → ואן האן (כשעה וחצי).", "דרום: צ'ואה טאו, ואחר כך טרוק לאם מעל אגם טויין לאם.", "מזרח: לין פואוק — או ברכבת הישנה ל-Trai Mat.", "לין אן נמצאת ליד מפל הפיל: סעו עם Honda Air Blade 125cc."],
 [("פגודת לין שון", "מוקדם בבוקר", "פגודה עתיקה בין עצי אורן, בלב העיר ושקטה."),
  ("פגודת לין קוואנג", "בוקר", "פגודה קטנה מלאה פסלים ודרקון סביב בריכה; מעט תיירים."),
  ("צ'ואה טאו (טיין וואנג קו סאט)", "בוקר", "פגודה בסגנון סיני עם בודהה לבן על גבעת אורנים."),
  ("מנזר הזן ואן האן (הבודהה הזהוב)", "אחר הצהריים", "פסלי בודהה זהובים גדולים ותצפית על העיר."),
  ("מנזר הזן טרוק לאם", "מוקדם בבוקר", "מעל אגם טויין לאם עם גנים יפים; רכבל מגבעת רובין."),
  ("פגודת לין פואוק (פגודת הבקבוקים)", "בוקר", "דרקון ומגדלים מפסיפס קרמיקה וזכוכית; אפשר לעלות למגדל הפעמון."),
  ("פגודת לין אן (נאם באן)", "בוקר", "צמוד למפל הפיל; אפשר לטפס בתוך פסל הבודהה הגבוה.")])

for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_VI = {"linhson": "Chùa Linh Sơn", "linhquang": "Chùa Linh Quang", "tau": "Chùa Tàu Thiên Vương Cổ Sát", "vanhanh": "Thiền viện Vạn Hạnh",
       "truclam": "Thiền viện Trúc Lâm", "linhphuoc": "Chùa Linh Phước", "linhan": "Chùa Linh Ẩn Nam Ban"}
def img_link(sid):
    """Temporary photo link: Google Images search for the Vietnamese place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_VI[sid] + " Đà Lạt")
NCENTER = 6
SHOP_DY = -30
