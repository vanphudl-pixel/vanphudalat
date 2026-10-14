"""Da Lat church map — shared data for the website page (/church-map/) and the printable PDF.
Coordinates, Google Maps place links (cid) and opening hours were taken from Google Maps on 2026-10-14.
Shared labels (directions, hours, legend, CTA, address…) are reused from the photo-spot map."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours (same codes as photomap)
SPOTS = [
    ("cathedral", 11.9360895, 108.4377113, "4046450182113774666",  True, "outside"),
    ("thanhtam",  11.9373552, 108.4305046, "9068647737476597169",  True, "8:00–20:00"),
    ("pink",      11.9496557, 108.4302407, "10570931153699557351", True, "7:30–11:30, 13:30–17:30"),
    ("camly",     11.9437965, 108.4220433, "10664212045593619792", True, "day"),
    ("dusinh",    11.9335067, 108.4184166, "13290532011272112981", True, "outside"),
    ("thanhmau",  11.9748047, 108.4327525, "7166832731603150520",  True, "outside"),
]
CENTER = _PM.CENTER
SLUG = "church-map"
PDF = "VanPhu-Dalat-Church-Map"
GUIDES = {"pink": "domainedemarie"}
LANGS = list(_PM.LANGS)
NCENTER = 6
SHOP_DY = -30
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Da Lat Church Map: 6 Beautiful Churches to Visit | Van Phu", "Da Lat Church Map",
 "Map of the 6 most-visited churches in Da Lat — the Rooster Church, the Pink Church and more — with opening hours, best time to go and directions, plus a free PDF.",
 "The 6 churches travellers visit most in Da Lat, from the Rooster Church to the Pink Church — with opening hours, the best time to go and one-tap directions. All within 4 km of the lake.",
 "Da Lat churches (1–6)", "Church etiquette",
 [("Dress", "cover shoulders and knees"), ("During Mass", "stay quiet; no photos or flash inside"), ("Opening", "many churches open their doors only for Mass — you can still visit the grounds"), ("Domaine de Marie", "closed at lunch, 11:30–13:30")],
 "Route ideas",
 ["Centre: the Cathedral and Thanh Tam Church, both on Tran Phu Street.", "West: Domaine de Marie → Cam Ly → Du Sinh (a hilltop view at the end).", "North: Thanh Mau Church on its hill, near the strawberry farms.", "Christmas Eve: churches are lit up and very busy — park early."],
 [("Da Lat Cathedral (Rooster Church)", "Late afternoon", "French-era cathedral with a rooster on its tower; doors open for Mass."),
  ("Thanh Tam Church", "Evening", "Large church on Tran Phu Street, lit up at night; guests mention a Sunday evening Mass in English — check with the parish."),
  ("Domaine de Marie (Pink Church)", "Morning", "Pink church and convent with a flower garden on a hill; free entry."),
  ("Cam Ly Church", "Morning", "Built in the style of a Central Highlands stilt house, among pine trees."),
  ("Du Sinh Church", "Early morning", "Looks like a pagoda from outside; hilltop view, clouds below on misty mornings."),
  ("Thanh Mau Church", "Early morning", "Tall church on a hill north of town with a wide view; many steps.")])
T["vi"] = _mk("Bản đồ nhà thờ Đà Lạt: 6 nhà thờ đẹp nên ghé | Văn Phú", "Bản đồ nhà thờ Đà Lạt",
 "Bản đồ 6 nhà thờ được khách ghé nhiều nhất Đà Lạt — nhà thờ Con Gà, nhà thờ Domaine de Marie… — giờ mở cửa, giờ đẹp, chỉ đường và PDF miễn phí.",
 "6 nhà thờ khách hay ghé nhất Đà Lạt, từ nhà thờ Con Gà đến nhà thờ Domaine de Marie, có giờ mở cửa, giờ đẹp và nút chỉ đường. Tất cả đều cách hồ Xuân Hương dưới 4 km.",
 "Nhà thờ Đà Lạt (1–6)", "Lưu ý khi vào nhà thờ",
 [("Trang phục", "che vai và gối"), ("Trong giờ lễ", "giữ yên lặng; không chụp ảnh, không dùng đèn flash bên trong"), ("Giờ mở cửa", "nhiều nhà thờ chỉ mở cửa vào giờ lễ — vẫn tham quan khuôn viên được"), ("Domaine de Marie", "nghỉ trưa 11:30–13:30")],
 "Gợi ý lộ trình",
 ["Trung tâm: nhà thờ Chánh tòa và nhà thờ Thánh Tâm, cùng trên đường Trần Phú.", "Phía tây: Domaine de Marie → Cam Ly → Du Sinh (cuối lộ trình có view đồi).", "Phía bắc: nhà thờ Thánh Mẫu trên đồi, gần các vườn dâu.", "Đêm Giáng sinh: nhà thờ trang trí đèn, rất đông — nên đến sớm gửi xe."],
 [("Nhà thờ Chánh tòa (nhà thờ Con Gà)", "Chiều muộn", "Nhà thờ thời Pháp, trên tháp có tượng con gà; mở cửa vào giờ lễ."),
  ("Nhà thờ Thánh Tâm", "Buổi tối", "Nhà thờ lớn trên đường Trần Phú, lên đèn buổi tối; khách cho biết có lễ tiếng Anh tối Chủ nhật — nên hỏi giáo xứ."),
  ("Nhà thờ Domaine de Marie", "Buổi sáng", "Nhà thờ màu hồng và tu viện, vườn hoa trên đồi; vào cửa miễn phí."),
  ("Nhà thờ Cam Ly", "Buổi sáng", "Kiến trúc mô phỏng nhà rông Tây Nguyên, giữa rừng thông."),
  ("Nhà thờ Du Sinh", "Sáng sớm", "Bên ngoài trông như ngôi chùa; trên đồi, sáng sương mù thấy mây phía dưới."),
  ("Nhà thờ Thánh Mẫu", "Sáng sớm", "Nhà thờ cao trên đồi phía bắc thành phố, view rộng; nhiều bậc thang.")])
T["ru"] = _mk("Карта церквей Далата: 6 красивых храмов | Van Phu", "Карта церквей Далата",
 "Карта 6 самых посещаемых церквей Далата — «Петушиная церковь», розовая церковь и другие — часы работы, лучшее время, маршрут и бесплатный PDF.",
 "6 церквей, которые туристы посещают в Далате чаще всего, от «Петушиной» до розовой, — с часами работы, лучшим временем и маршрутом в одно касание. Все — в пределах 4 км от озера.",
 "Церкви Далата (1–6)", "Как вести себя в церкви",
 [("Одежда", "закрытые плечи и колени"), ("Во время мессы", "тишина; внутри без фото и вспышки"), ("Время работы", "многие церкви открывают двери только к мессе — двор можно осмотреть"), ("Домен де Мари", "перерыв на обед 11:30–13:30")],
 "Идеи маршрутов",
 ["Центр: кафедральный собор и церковь Тхань Там — обе на улице Чан Фу.", "Запад: Домен де Мари → Камли → Зусинь (в конце — вид с холма).", "Север: церковь Тхань Мау на холме, рядом клубничные фермы.", "Сочельник: церкви в огнях и очень многолюдны — приезжайте заранее."],
 [("Кафедральный собор («Петушиная церковь»)", "Ближе к вечеру", "Собор французской эпохи с петухом на шпиле; двери открыты во время мессы."),
  ("Церковь Тхань Там", "Вечер", "Большая церковь на улице Чан Фу, вечером с подсветкой; гости пишут о воскресной вечерней мессе на английском — уточняйте в приходе."),
  ("Домен де Мари (розовая церковь)", "Утро", "Розовая церковь и монастырь с садом на холме; вход бесплатный."),
  ("Церковь Камли", "Утро", "Построена в стиле дома на сваях народов Тэйнгуен, среди сосен."),
  ("Церковь Зусинь", "Раннее утро", "Снаружи похожа на пагоду; на холме, туманным утром облака внизу."),
  ("Церковь Тхань Мау", "Раннее утро", "Высокая церковь на холме к северу от города, широкий вид; много ступеней.")])
T["zh"] = _mk("大叻教堂地图：6座值得一去的教堂 | Van Phu", "大叻教堂地图",
 "大叻游客最常去的6座教堂地图——公鸡教堂、粉红教堂等——附开放时间、最佳时段、导航和免费 PDF。",
 "大叻游客最常去的6座教堂，从公鸡教堂到粉红教堂，附开放时间、最佳时段和一键导航。全部距春香湖4公里以内。",
 "大叻教堂（1–6）", "参观教堂礼仪",
 [("着装", "遮住肩膀和膝盖"), ("弥撒期间", "保持安静；室内不拍照、不开闪光灯"), ("开放时间", "很多教堂只在弥撒时开门——院子仍可参观"), ("粉红教堂", "午休 11:30–13:30")],
 "路线建议",
 ["市中心：大教堂和圣心堂，都在陈富路上。", "西线：粉红教堂 → 甘里教堂 → 游生教堂（终点可看山景）。", "北线：圣母堂在山上，靠近草莓园。", "平安夜：教堂张灯结彩，人非常多——请提早停车。"],
 [("大叻主教座堂（公鸡教堂）", "傍晚", "法国时期的主教座堂，塔顶有公鸡；弥撒时开门。"),
  ("圣心堂 Thanh Tam", "晚上", "陈富路上的大教堂，晚上亮灯；有游客提到周日晚上有英语弥撒——请向堂区确认。"),
  ("玛丽修道院（粉红教堂）", "上午", "山坡上的粉色教堂和修道院，有花园；免费入场。"),
  ("甘里教堂 Cam Ly", "上午", "模仿西原高脚屋建筑，位于松林中。"),
  ("游生教堂 Du Sinh", "清晨", "外观像寺庙；在山顶，雾天清晨可见云海。"),
  ("圣母堂 Thanh Mau", "清晨", "城北山上的高大教堂，视野开阔；台阶很多。")])
T["ko"] = _mk("달랏 성당 지도: 꼭 가볼 만한 성당 6곳 | Van Phu", "달랏 성당 지도",
 "여행자가 가장 많이 찾는 달랏 성당 6곳 지도 — 닭 성당, 핑크 성당 등 — 운영 시간, 추천 시간대, 길찾기와 무료 PDF.",
 "닭 성당부터 핑크 성당까지, 여행자가 가장 많이 찾는 달랏 성당 6곳. 운영 시간, 추천 시간대, 원터치 길찾기까지. 모두 호수에서 4km 이내입니다.",
 "달랏 성당 (1–6)", "성당 방문 예절",
 [("복장", "어깨와 무릎 가리기"), ("미사 중", "조용히; 실내 촬영·플래시 금지"), ("개방", "많은 성당이 미사 때만 문을 엶 — 마당은 둘러볼 수 있음"), ("도멘 드 마리", "점심시간 11:30–13:30 휴무")],
 "추천 코스",
 ["시내: 대성당과 타잉땀 성당, 모두 쩐푸 거리.", "서쪽: 도멘 드 마리 → 깜리 → 주신 (마지막에 언덕 전망).", "북쪽: 딸기 농장 근처 언덕 위 타잉머우 성당.", "크리스마스이브: 조명이 켜지고 매우 붐빔 — 일찍 주차하세요."],
 [("달랏 대성당 (닭 성당)", "늦은 오후", "프랑스 시대 대성당, 탑 위에 닭; 미사 때 문을 엶."),
  ("타잉땀 성당", "저녁", "쩐푸 거리의 큰 성당, 밤에 조명; 일요일 저녁 영어 미사가 있다는 후기 — 본당에 확인하세요."),
  ("도멘 드 마리 (핑크 성당)", "오전", "언덕 위 분홍색 성당과 수도원, 꽃 정원; 무료입장."),
  ("깜리 성당", "오전", "소나무 숲 속, 떠이응우옌 고상가옥 양식으로 지은 성당."),
  ("주신 성당", "이른 아침", "밖에서 보면 사찰 같은 모습; 언덕 위, 안개 낀 아침엔 발아래 구름."),
  ("타잉머우 성당", "이른 아침", "시내 북쪽 언덕 위 높은 성당, 넓은 전망; 계단이 많음.")])
T["ja"] = _mk("ダラット教会マップ：訪れたい美しい教会6選 | Van Phu", "ダラット教会マップ",
 "ダラットで旅行者がよく訪れる6つの教会のマップ — 鶏の教会、ピンク教会など — 開門時間、おすすめの時間帯、道案内、無料PDF付き。",
 "鶏の教会からピンク教会まで、ダラットで旅行者が最も訪れる6つの教会。開門時間、おすすめの時間帯、ワンタップ道案内付き。どれも湖から4km以内です。",
 "ダラットの教会（1–6）", "教会でのマナー",
 [("服装", "肩と膝を隠す"), ("ミサの間", "静かに。堂内での撮影・フラッシュは控える"), ("開門", "ミサの時だけ扉を開く教会が多い — 敷地は見学できます"), ("ドメーヌ・ド・マリー", "昼休み 11:30–13:30")],
 "おすすめルート",
 ["中心部：大聖堂とタインタム教会（どちらもチャンフー通り）。", "西ルート：ドメーヌ・ド・マリー → カムリー → ズーシン（最後に丘の眺め）。", "北ルート：イチゴ農園近くの丘に建つタインマウ教会。", "クリスマスイブ：ライトアップされ大混雑 — 早めに駐車を。"],
 [("ダラット大聖堂（鶏の教会）", "夕方", "フランス時代の大聖堂。塔の上に鶏。ミサの時に開門。"),
  ("タインタム教会", "夜", "チャンフー通りの大きな教会で夜はライトアップ。日曜夜に英語ミサがあるという口コミあり — 教会に確認を。"),
  ("ドメーヌ・ド・マリー（ピンク教会）", "午前", "丘の上のピンクの教会と修道院、花の庭。入場無料。"),
  ("カムリー教会", "午前", "松林の中、中部高原の高床式住居を模した建築。"),
  ("ズーシン教会", "早朝", "外から見るとお寺のよう。丘の上で、霧の朝は眼下に雲。"),
  ("タインマウ教会", "早朝", "市の北の丘に建つ背の高い教会。眺めが広く、階段が多い。")])
T["th"] = _mk("แผนที่โบสถ์ดาลัด: 6 โบสถ์สวยที่ควรไป | Van Phu", "แผนที่โบสถ์ดาลัด",
 "แผนที่ 6 โบสถ์ที่นักท่องเที่ยวไปมากที่สุดในดาลัด — โบสถ์ไก่ โบสถ์สีชมพู และอื่น ๆ — พร้อมเวลาเปิด ช่วงเวลาที่ดีที่สุด เส้นทาง และ PDF ฟรี",
 "6 โบสถ์ที่นักท่องเที่ยวไปมากที่สุดในดาลัด ตั้งแต่โบสถ์ไก่ถึงโบสถ์สีชมพู พร้อมเวลาเปิด ช่วงเวลาที่ดีที่สุด และนำทางแตะเดียว ทั้งหมดอยู่ห่างทะเลสาบไม่เกิน 4 กม.",
 "โบสถ์ในดาลัด (1–6)", "มารยาทในโบสถ์",
 [("การแต่งกาย", "ปิดไหล่และเข่า"), ("ระหว่างมิสซา", "เงียบ ห้ามถ่ายรูปหรือใช้แฟลชด้านใน"), ("เวลาเปิด", "หลายโบสถ์เปิดประตูเฉพาะเวลามิสซา — เดินชมบริเวณได้"), ("โบสถ์สีชมพู", "พักเที่ยง 11:30–13:30")],
 "ไอเดียเส้นทาง",
 ["ใจกลางเมือง: อาสนวิหารและโบสถ์ถั่นห์ต๋ามบนถนน Tran Phu", "ฝั่งตะวันตก: Domaine de Marie → กัมลี → ซูซินห์ (จบด้วยวิวบนเนิน)", "ฝั่งเหนือ: โบสถ์ถั่นห์เหมาบนเนิน ใกล้ไร่สตรอว์เบอร์รี", "คืนคริสต์มาสอีฟ: โบสถ์ประดับไฟและคนเยอะมาก — ไปจอดรถแต่เนิ่น ๆ"],
 [("อาสนวิหารดาลัด (โบสถ์ไก่)", "ช่วงบ่ายแก่ ๆ", "อาสนวิหารยุคฝรั่งเศส มีรูปไก่บนยอดหอ เปิดประตูช่วงมิสซา"),
  ("โบสถ์ถั่นห์ต๋าม", "ช่วงค่ำ", "โบสถ์ใหญ่บนถนน Tran Phu เปิดไฟสวยตอนกลางคืน มีรีวิวว่ามีมิสซาภาษาอังกฤษคืนวันอาทิตย์ — ควรสอบถามวัด"),
  ("Domaine de Marie (โบสถ์สีชมพู)", "ช่วงเช้า", "โบสถ์และอารามสีชมพูบนเนิน มีสวนดอกไม้ เข้าฟรี"),
  ("โบสถ์กัมลี", "ช่วงเช้า", "สร้างแบบบ้านใต้ถุนสูงของชาวที่ราบสูงตอนกลาง ท่ามกลางป่าสน"),
  ("โบสถ์ซูซินห์", "เช้าตรู่", "ภายนอกดูเหมือนวัด อยู่บนเนิน เช้าที่มีหมอกจะเห็นทะเลหมอกด้านล่าง"),
  ("โบสถ์ถั่นห์เหมา", "เช้าตรู่", "โบสถ์สูงบนเนินทางเหนือของเมือง วิวกว้าง บันไดเยอะ")])
T["id"] = _mk("Peta Gereja Da Lat: 6 Gereja Cantik untuk Dikunjungi | Van Phu", "Peta Gereja Da Lat",
 "Peta 6 gereja yang paling sering dikunjungi di Da Lat — Gereja Ayam, Gereja Merah Muda dan lainnya — jam buka, waktu terbaik, petunjuk arah dan PDF gratis.",
 "6 gereja yang paling sering dikunjungi wisatawan di Da Lat, dari Gereja Ayam sampai Gereja Merah Muda — dengan jam buka, waktu terbaik dan petunjuk arah sekali ketuk. Semuanya dalam 4 km dari danau.",
 "Gereja di Da Lat (1–6)", "Etika di gereja",
 [("Pakaian", "tutup bahu dan lutut"), ("Saat Misa", "tenang; jangan memotret atau memakai flash di dalam"), ("Jam buka", "banyak gereja hanya membuka pintu saat Misa — halaman tetap bisa dikunjungi"), ("Domaine de Marie", "tutup saat makan siang, 11:30–13:30")],
 "Ide rute",
 ["Pusat: Katedral dan Gereja Thanh Tam, sama-sama di Jalan Tran Phu.", "Barat: Domaine de Marie → Cam Ly → Du Sinh (berakhir dengan pemandangan bukit).", "Utara: Gereja Thanh Mau di atas bukit, dekat kebun stroberi.", "Malam Natal: gereja penuh lampu dan sangat ramai — parkir lebih awal."],
 [("Katedral Da Lat (Gereja Ayam)", "Sore", "Katedral era Prancis dengan patung ayam di menaranya; pintu dibuka saat Misa."),
  ("Gereja Thanh Tam", "Malam", "Gereja besar di Jalan Tran Phu, terang di malam hari; tamu menyebut ada Misa berbahasa Inggris Minggu malam — tanyakan ke paroki."),
  ("Domaine de Marie (Gereja Merah Muda)", "Pagi", "Gereja dan biara merah muda dengan taman bunga di bukit; gratis masuk."),
  ("Gereja Cam Ly", "Pagi", "Dibangun bergaya rumah panggung Dataran Tinggi Tengah, di antara pinus."),
  ("Gereja Du Sinh", "Pagi-pagi", "Dari luar mirip pagoda; di atas bukit, saat berkabut tampak awan di bawah."),
  ("Gereja Thanh Mau", "Pagi-pagi", "Gereja tinggi di bukit utara kota dengan pemandangan luas; banyak anak tangga.")])
T["ms"] = _mk("Peta Gereja Da Lat: 6 Gereja Cantik untuk Dilawati | Van Phu", "Peta Gereja Da Lat",
 "Peta 6 gereja paling popular di Da Lat — Gereja Ayam, Gereja Merah Jambu dan lain-lain — waktu buka, masa terbaik, arah dan PDF percuma.",
 "6 gereja yang paling kerap dilawati pelancong di Da Lat, dari Gereja Ayam hingga Gereja Merah Jambu — dengan waktu buka, masa terbaik dan arah sekali sentuh. Semuanya dalam 4 km dari tasik.",
 "Gereja di Da Lat (1–6)", "Adab di gereja",
 [("Pakaian", "tutup bahu dan lutut"), ("Semasa Misa", "senyap; jangan ambil gambar atau guna flash di dalam"), ("Waktu buka", "banyak gereja hanya buka pintu semasa Misa — kawasan luar boleh dilawati"), ("Domaine de Marie", "tutup waktu makan tengah hari, 11:30–13:30")],
 "Cadangan laluan",
 ["Pusat: Katedral dan Gereja Thanh Tam, kedua-duanya di Jalan Tran Phu.", "Barat: Domaine de Marie → Cam Ly → Du Sinh (berakhir dengan pemandangan bukit).", "Utara: Gereja Thanh Mau di atas bukit, dekat ladang strawberi.", "Malam Krismas: gereja bercahaya dan sangat sesak — letak motor awal."],
 [("Katedral Da Lat (Gereja Ayam)", "Lewat petang", "Katedral era Perancis dengan ayam di atas menaranya; pintu dibuka semasa Misa."),
  ("Gereja Thanh Tam", "Malam", "Gereja besar di Jalan Tran Phu, bercahaya waktu malam; pelawat menyebut Misa bahasa Inggeris malam Ahad — tanya pihak paroki."),
  ("Domaine de Marie (Gereja Merah Jambu)", "Pagi", "Gereja dan biara merah jambu dengan taman bunga di bukit; masuk percuma."),
  ("Gereja Cam Ly", "Pagi", "Dibina gaya rumah panggung Tanah Tinggi Tengah, di antara pokok pain."),
  ("Gereja Du Sinh", "Awal pagi", "Dari luar seperti pagoda; di atas bukit, pagi berkabus nampak awan di bawah."),
  ("Gereja Thanh Mau", "Awal pagi", "Gereja tinggi di bukit utara bandar dengan pemandangan luas; banyak anak tangga.")])
T["de"] = _mk("Kirchen-Karte Da Lat: 6 schöne Kirchen | Van Phu", "Kirchen-Karte Da Lat",
 "Karte der 6 meistbesuchten Kirchen in Da Lat – Hahnenkirche, rosa Kirche und mehr – mit Öffnungszeiten, bester Zeit, Route und kostenlosem PDF.",
 "Die 6 Kirchen, die Reisende in Da Lat am häufigsten besuchen, von der Hahnenkirche bis zur rosa Kirche – mit Öffnungszeiten, bester Zeit und Route per Fingertipp. Alle höchstens 4 km vom See entfernt.",
 "Kirchen in Da Lat (1–6)", "Verhalten in der Kirche",
 [("Kleidung", "Schultern und Knie bedecken"), ("Während der Messe", "ruhig bleiben; innen keine Fotos, kein Blitz"), ("Öffnung", "viele Kirchen öffnen nur zur Messe – das Gelände ist trotzdem zugänglich"), ("Domaine de Marie", "Mittagspause 11:30–13:30")],
 "Routen-Ideen",
 ["Zentrum: Kathedrale und Thanh-Tam-Kirche, beide an der Tran-Phu-Straße.", "Westen: Domaine de Marie → Cam Ly → Du Sinh (am Ende Blick vom Hügel).", "Norden: Thanh-Mau-Kirche auf dem Hügel, nahe den Erdbeerfarmen.", "Heiligabend: Kirchen beleuchtet und sehr voll – früh parken."],
 [("Kathedrale von Da Lat (Hahnenkirche)", "Später Nachmittag", "Kathedrale aus der Kolonialzeit mit Hahn auf dem Turm; Türen zur Messe offen."),
  ("Thanh-Tam-Kirche", "Abend", "Große Kirche an der Tran-Phu-Straße, abends beleuchtet; Gäste erwähnen eine englische Messe am Sonntagabend – bitte in der Gemeinde nachfragen."),
  ("Domaine de Marie (rosa Kirche)", "Vormittag", "Rosa Kirche und Kloster mit Blumengarten auf einem Hügel; Eintritt frei."),
  ("Cam-Ly-Kirche", "Vormittag", "Im Stil eines Pfahlhauses des Zentralen Hochlands gebaut, zwischen Kiefern."),
  ("Du-Sinh-Kirche", "Früher Morgen", "Sieht von außen wie eine Pagode aus; auf einem Hügel, an nebligen Morgen Wolken darunter."),
  ("Thanh-Mau-Kirche", "Früher Morgen", "Hohe Kirche auf einem Hügel im Norden mit weitem Blick; viele Stufen.")])
T["fr"] = _mk("Carte des églises de Da Lat : 6 belles églises à voir | Van Phu", "Carte des églises de Da Lat",
 "Carte des 6 églises les plus visitées de Da Lat — l'église du Coq, l'église rose et d'autres — avec horaires, meilleur moment, itinéraire et PDF gratuit.",
 "Les 6 églises que les voyageurs visitent le plus à Da Lat, de l'église du Coq à l'église rose — avec horaires, meilleur moment et itinéraire en un clic. Toutes à moins de 4 km du lac.",
 "Églises de Da Lat (1–6)", "Savoir-vivre à l'église",
 [("Tenue", "épaules et genoux couverts"), ("Pendant la messe", "silence ; ni photo ni flash à l'intérieur"), ("Ouverture", "beaucoup d'églises n'ouvrent que pour la messe — on peut visiter l'extérieur"), ("Domaine de Marie", "fermé le midi, 11 h 30–13 h 30")],
 "Idées d'itinéraires",
 ["Centre : la cathédrale et l'église Thanh Tam, toutes deux rue Tran Phu.", "Ouest : Domaine de Marie → Cam Ly → Du Sinh (vue sur les collines à la fin).", "Nord : l'église Thanh Mau sur sa colline, près des fermes de fraises.", "Veille de Noël : églises illuminées et bondées — garez-vous tôt."],
 [("Cathédrale de Da Lat (église du Coq)", "Fin d'après-midi", "Cathédrale de l'époque française avec un coq sur la tour ; portes ouvertes pour la messe."),
  ("Église Thanh Tam", "Soir", "Grande église rue Tran Phu, illuminée le soir ; des visiteurs signalent une messe en anglais le dimanche soir — à vérifier auprès de la paroisse."),
  ("Domaine de Marie (église rose)", "Matin", "Église et couvent roses avec un jardin fleuri sur une colline ; entrée gratuite."),
  ("Église de Cam Ly", "Matin", "Construite comme une maison sur pilotis des Hauts Plateaux, parmi les pins."),
  ("Église de Du Sinh", "Tôt le matin", "On dirait une pagode de l'extérieur ; sur une colline, nuages en contrebas les matins de brume."),
  ("Église Thanh Mau", "Tôt le matin", "Haute église sur une colline au nord de la ville, large vue ; beaucoup de marches.")])
T["es"] = _mk("Mapa de iglesias de Da Lat: 6 iglesias bonitas | Van Phu", "Mapa de iglesias de Da Lat",
 "Mapa de las 6 iglesias más visitadas de Da Lat — la iglesia del Gallo, la iglesia rosa y más — con horarios, mejor momento, ruta y PDF gratis.",
 "Las 6 iglesias que más visitan los viajeros en Da Lat, de la iglesia del Gallo a la iglesia rosa, con horarios, mejor momento y ruta con un toque. Todas a menos de 4 km del lago.",
 "Iglesias de Da Lat (1–6)", "Normas en la iglesia",
 [("Ropa", "hombros y rodillas cubiertos"), ("Durante la misa", "silencio; sin fotos ni flash dentro"), ("Apertura", "muchas iglesias solo abren para la misa; el recinto se puede visitar"), ("Domaine de Marie", "cierra a mediodía, 11:30–13:30")],
 "Ideas de ruta",
 ["Centro: la catedral y la iglesia Thanh Tam, ambas en la calle Tran Phu.", "Oeste: Domaine de Marie → Cam Ly → Du Sinh (vistas desde la colina al final).", "Norte: la iglesia Thanh Mau en su colina, cerca de las granjas de fresas.", "Nochebuena: iglesias iluminadas y abarrotadas; aparca pronto."],
 [("Catedral de Da Lat (iglesia del Gallo)", "Última hora de la tarde", "Catedral de la época francesa con un gallo en la torre; abre en horario de misa."),
  ("Iglesia Thanh Tam", "Noche", "Gran iglesia en la calle Tran Phu, iluminada de noche; los visitantes mencionan una misa en inglés el domingo por la noche: confírmalo en la parroquia."),
  ("Domaine de Marie (iglesia rosa)", "Mañana", "Iglesia y convento rosas con jardín de flores en una colina; entrada gratuita."),
  ("Iglesia de Cam Ly", "Mañana", "Construida como una casa sobre pilotes de las Tierras Altas Centrales, entre pinos."),
  ("Iglesia de Du Sinh", "A primera hora", "Por fuera parece una pagoda; en lo alto de una colina, con nubes debajo las mañanas de niebla."),
  ("Iglesia Thanh Mau", "A primera hora", "Iglesia alta en una colina al norte de la ciudad, con amplias vistas; muchos escalones.")])
T["he"] = _mk("מפת הכנסיות של דלאט: 6 כנסיות יפות לביקור | Van Phu", "מפת הכנסיות של דלאט",
 "מפה של 6 הכנסיות המתויירות ביותר בדלאט — כנסיית התרנגול, הכנסייה הוורודה ועוד — שעות פתיחה, הזמן הכי טוב, ניווט ו-PDF בחינם.",
 "6 הכנסיות שמטיילים מבקרים בהן הכי הרבה בדלאט, מכנסיית התרנגול ועד הכנסייה הוורודה — עם שעות פתיחה, הזמן הכי טוב וניווט בלחיצה אחת. כולן במרחק של עד 4 ק\"מ מהאגם.",
 "כנסיות דלאט (1–6)", "כללי התנהגות בכנסייה",
 [("לבוש", "כתפיים וברכיים מכוסות"), ("בזמן המיסה", "שקט; בלי צילום ובלי פלאש בפנים"), ("פתיחה", "כנסיות רבות פותחות דלתות רק למיסה — אפשר לבקר בחצר"), ("דומיין דה מרי", "סגור בצהריים, 11:30–13:30")],
 "רעיונות למסלול",
 ["מרכז: הקתדרלה וכנסיית טאן טאם, שתיהן ברחוב טראן פו.", "מערב: דומיין דה מרי → קאם לי → זו סין (בסוף תצפית מהגבעה).", "צפון: כנסיית טאן מאו על הגבעה, ליד חוות התותים.", "ערב חג המולד: הכנסיות מוארות ועמוסות מאוד — חנו מוקדם."],
 [("הקתדרלה של דלאט (כנסיית התרנגול)", "אחר הצהריים המאוחרים", "קתדרלה מהתקופה הצרפתית עם תרנגול על המגדל; הדלתות פתוחות בזמן המיסה."),
  ("כנסיית טאן טאם", "ערב", "כנסייה גדולה ברחוב טראן פו, מוארת בערב; מבקרים מזכירים מיסה באנגלית ביום ראשון בערב — כדאי לבדוק עם הקהילה."),
  ("דומיין דה מרי (הכנסייה הוורודה)", "בוקר", "כנסייה ומנזר ורודים עם גן פרחים על גבעה; כניסה חינם."),
  ("כנסיית קאם לי", "בוקר", "בנויה בסגנון בית על כלונסאות של הרמה המרכזית, בין עצי אורן."),
  ("כנסיית זו סין", "מוקדם בבוקר", "מבחוץ נראית כמו פגודה; על גבעה, ובבקרים ערפיליים העננים מתחת."),
  ("כנסיית טאן מאו", "מוקדם בבוקר", "כנסייה גבוהה על גבעה בצפון העיר עם נוף רחב; הרבה מדרגות.")])

from content._langs import inject as _inject
_inject(T, __name__)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_VI = {"cathedral": "Nhà thờ Chánh tòa Con Gà", "thanhtam": "Nhà thờ Thánh Tâm", "pink": "Nhà thờ Domaine de Marie",
       "camly": "Nhà thờ Cam Ly", "dusinh": "Nhà thờ Du Sinh", "thanhmau": "Nhà thờ Thánh Mẫu"}
def img_link(sid):
    """Temporary photo link: Google Images search for the Vietnamese place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_VI[sid] + " Đà Lạt")
MAXKM = 5.0
RINGS = (1, 2, 4)
