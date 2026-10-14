"""Da Lat BBQ (quán nướng) map — shared data for the website page (/bbq-map/) and the printable PDF.
Places chosen by number of Google Maps reviews; coordinates, place links (cid) and opening hours taken from Google Maps
on 2026-10-14. Shared labels (directions, legend, CTA, address…) are reused from the photo-spot map."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours
SPOTS = [
    ("nn1900",     11.9364905, 108.4333546, "5008804811359840493",  True, "16:00–22:00"),
    ("namnuong",   11.9425409, 108.4306860, "9609338726734180995",  True, "16:00–23:00"),
    ("bbqgarden",  11.9424878, 108.4296355, "14106149137950099292", True, "11:00–23:00"),
    ("didinh",     11.9428701, 108.4287827, "14937801456876662352", True, "13:00–20:30"),
    ("khoithong",  11.9292676, 108.4488825, "5471029174455129725",  True, "10:30–22:00"),
    ("ourmemory",  11.9285088, 108.4302537, "12632435638453586550", True, "16:00–22:00"),
    ("gahanhphuc", 11.9429244, 108.4235302, "14527062552604716745", True, "10:00–21:30"),
    ("hoanghon",   11.9381695, 108.4835734, "3362837821524292832",  True, "14:00–22:00"),
    ("tuimotog",   11.9410479, 108.4837046, "15454092518088732264", True, "10:30–22:00"),
]
CENTER = _PM.CENTER
SLUG = "bbq-map"
PDF = "VanPhu-Dalat-BBQ-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 7
LEGW = 330
MAPH = 560
H1PT = 22
MAXKM = 6.0
RINGS = (1, 2, 5)
SIDE = {"hoanghon": "l", "tuimotog": "l"}
JITTER = {"namnuong": (10, -12), "bbqgarden": (-6, 14), "didinh": (-14, -26), "gahanhphuc": (-16, 4), "hoanghon": (0, 12), "tuimotog": (0, -12)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Best BBQ in Da Lat: Map of 9 Popular Grill Restaurants | Van Phu", "Da Lat BBQ Map",
 "Map of the 9 most-reviewed BBQ and grill restaurants in Da Lat — table grills, bamboo-rice chicken and rice-paper 'pizza' — with opening hours and directions, plus a free PDF.",
 "A cold Da Lat evening is made for barbecue. Here are the 9 grill spots with the most Google Maps reviews — from table-grill restaurants to bamboo-rice chicken and the famous rice-paper 'pizza' — with one-tap directions.",
 "In town (1–7)", "Good to know",
 [("Hours", "most open in the late afternoon; busiest 18:00–20:00"), ("Booking", "at weekends, call ahead or arrive before 18:00"), ("Style", "most are grill-at-your-table, often with hotpot combos"), ("Last rental day", "return the scooter by 21:00 — eat earlier, or come back on foot")],
 "Tips",
 ["Never drink and ride — if you drink, leave the scooter and take a Grab.", "Hoang Diệu Street has three spots next to each other (2–4).", "Hoang Hon and Túi Mơ To are on the east side with sunset views.", "Park only in guarded parking and lock the scooter."],
 [("Nậm Nướng 1900 (Tran Phu)", "Evening", "Very busy table-grill restaurant near the centre; staff help you grill."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Evening", "The original Nậm Nướng: table grill, music and a lively crowd."),
  ("BBQ Garden (buffet)", "Evening", "All-you-can-eat grill and hotpot buffet on Hoang Dieu Street."),
  ("Bánh tráng nướng Dì Đinh", "Afternoon", "Famous grilled rice-paper 'pizza' street snack; expect a short queue."),
  ("Tiệm nướng Khói Thông", "Evening", "Grill restaurant with a pine-hill view; grilled chicken and bamboo rice."),
  ("Tiệm nướng Our Memory", "Evening", "Table-grill and hotpot combos on a slope with a night view; small parking."),
  ("Tiệm Gà Hạnh Phúc", "Lunch or dinner", "Grilled chicken with bamboo rice and chicken hotpot with lá é."),
  ("Tiệm nướng Hoàng Hôn", "Sunset", "Hillside grill east of town, known for its sunset view."),
  ("Túi Mơ To Garden Restaurant", "Sunset", "Garden restaurant with flowers and a hill view; BBQ and hotpot.")])
T["vi"] = _mk("Quán nướng Đà Lạt ngon: bản đồ 9 quán đông khách nhất | Văn Phú", "Bản đồ quán nướng Đà Lạt",
 "Bản đồ 9 quán nướng có nhiều đánh giá nhất Đà Lạt — nướng tại bàn, gà nướng cơm lam, bánh tráng nướng — giờ mở cửa, chỉ đường và PDF miễn phí.",
 "Tối Đà Lạt se lạnh là phải đi ăn nướng. Đây là 9 quán nướng có nhiều đánh giá nhất trên Google Maps — từ nướng tại bàn, gà nướng cơm lam đến bánh tráng nướng — có nút chỉ đường.",
 "Trong thành phố (1–7)", "Nên biết",
 [("Giờ mở", "đa số mở từ chiều; đông nhất 18:00–20:00"), ("Đặt bàn", "cuối tuần nên gọi trước hoặc đến trước 18:00"), ("Kiểu quán", "phần lớn là nướng tại bàn, nhiều quán có combo lẩu"), ("Ngày trả xe", "trả xe trước 21:00 — nên ăn sớm hoặc đi bộ quay lại")],
 "Lưu ý",
 ["Đã uống rượu bia thì không lái xe — để xe lại và gọi Grab.", "Đường Hoàng Diệu có 3 quán sát nhau (số 2–4).", "Hoàng Hôn và Túi Mơ To ở phía đông, có view hoàng hôn.", "Chỉ gửi xe ở bãi có người trông và khóa xe cẩn thận."],
 [("Nậm Nướng 1900 (Trần Phú)", "Buổi tối", "Quán nướng tại bàn rất đông gần trung tâm; nhân viên nướng hộ."),
  ("Nậm Nướng Đà Lạt (Hoàng Diệu)", "Buổi tối", "Quán Nậm Nướng gốc: nướng tại bàn, có nhạc, không khí sôi động."),
  ("BBQ Garden (buffet)", "Buổi tối", "Buffet nướng và lẩu không giới hạn trên đường Hoàng Diệu."),
  ("Bánh tráng nướng Dì Đinh", "Buổi chiều", "Quán bánh tráng nướng nổi tiếng; thường phải xếp hàng một chút."),
  ("Tiệm nướng Khói Thông", "Buổi tối", "Quán nướng view đồi thông; có gà nướng cơm lam."),
  ("Tiệm nướng Our Memory", "Buổi tối", "Combo nướng và lẩu trên sườn dốc, view đêm; chỗ đậu xe ít."),
  ("Tiệm Gà Hạnh Phúc", "Trưa hoặc tối", "Gà nướng cơm lam và lẩu gà lá é."),
  ("Tiệm nướng Hoàng Hôn", "Hoàng hôn", "Quán nướng trên sườn đồi phía đông, nổi tiếng view hoàng hôn."),
  ("Túi Mơ To Garden Restaurant", "Hoàng hôn", "Nhà hàng sân vườn nhiều hoa, view đồi; có nướng và lẩu.")])
T["ru"] = _mk("Лучшее барбекю в Далате: карта 9 популярных гриль-ресторанов | Van Phu", "Карта барбекю Далата",
 "Карта 9 гриль-ресторанов Далата с наибольшим числом отзывов — гриль на столе, курица с рисом в бамбуке и «вьетнамская пицца» — часы работы, маршрут и бесплатный PDF.",
 "Прохладный вечер в Далате создан для барбекю. Вот 9 мест с наибольшим числом отзывов в Google Maps — от гриля на столе до курицы с рисом в бамбуке и знаменитой «пиццы» из рисовой бумаги — с маршрутом в одно касание.",
 "В городе (1–7)", "Полезно знать",
 [("Часы", "большинство открываются ближе к вечеру; больше всего людей в 18:00–20:00"), ("Бронь", "в выходные звоните заранее или приходите до 18:00"), ("Формат", "в основном гриль на столе, часто с комбо из хотпота"), ("Последний день аренды", "верните байк до 21:00 — поужинайте пораньше или вернитесь пешком")],
 "Советы",
 ["Выпили — не садитесь за руль: оставьте байк и вызовите Grab.", "На улице Хоангзьеу три места рядом (2–4).", "Хоанг Хон и Túi Mơ To — на востоке, с видом на закат.", "Ставьте байк только на охраняемую парковку и запирайте."],
 [("Nậm Nướng 1900 (Чан Фу)", "Вечер", "Очень популярный гриль на столе у центра; персонал помогает жарить."),
  ("Nậm Nướng Đà Lạt (Хоангзьеу)", "Вечер", "Первый Nậm Nướng: гриль на столе, музыка, живая атмосфера."),
  ("BBQ Garden (буфет)", "Вечер", "Буфет «гриль и хотпот без ограничений» на улице Хоангзьеу."),
  ("Bánh tráng nướng Dì Đinh", "После обеда", "Знаменитая жареная рисовая бумага — уличная «пицца»; бывает небольшая очередь."),
  ("Tiệm nướng Khói Thông", "Вечер", "Гриль-ресторан с видом на сосновые холмы; курица на гриле и рис в бамбуке."),
  ("Tiệm nướng Our Memory", "Вечер", "Комбо гриль и хотпот на склоне с ночным видом; парковка маленькая."),
  ("Tiệm Gà Hạnh Phúc", "Обед или ужин", "Курица на гриле с рисом в бамбуке и хотпот из курицы с травой лаэ."),
  ("Tiệm nướng Hoàng Hôn", "Закат", "Гриль на склоне к востоку от города, известен видом на закат."),
  ("Túi Mơ To Garden Restaurant", "Закат", "Садовый ресторан с цветами и видом на холмы; барбекю и хотпот.")])
T["zh"] = _mk("大叻烧烤推荐：9家人气烧烤店地图 | Van Phu", "大叻烧烤地图",
 "大叻 Google 地图评价最多的9家烧烤店地图——桌边烤肉、竹筒饭烤鸡和烤米纸“越南披萨”——附营业时间、导航和免费 PDF。",
 "大叻凉爽的夜晚最适合吃烧烤。这里是 Google 地图上评价最多的9家烧烤店——从桌边烤肉到竹筒饭烤鸡和有名的烤米纸——一键导航。",
 "市区（1–7）", "实用信息",
 [("营业时间", "大多下午开始营业；18:00–20:00 最忙"), ("订位", "周末请提前打电话或 18:00 前到"), ("形式", "大多是桌边自助烤，常有火锅套餐"), ("还车日", "最后一天请在 21:00 前还车——早点吃或者走路回来")],
 "提示",
 ["喝酒不骑车——喝了酒就把车留下，打 Grab 回去。", "黄耀路上有三家紧挨着（2–4）。", "Hoàng Hôn 和 Túi Mơ To 在城东，可看日落。", "只停在有人看管的停车场，并锁好车。"],
 [("Nậm Nướng 1900（陈富路）", "晚上", "市中心附近人气很旺的桌边烧烤；店员会帮忙烤。"),
  ("Nậm Nướng Đà Lạt（黄耀路）", "晚上", "最早的 Nậm Nướng：桌边烧烤、有音乐、气氛热闹。"),
  ("BBQ Garden（自助）", "晚上", "黄耀路上的烧烤火锅无限量自助。"),
  ("Dì Đinh 烤米纸", "下午", "有名的烤米纸“越南披萨”小吃；通常要排一下队。"),
  ("Tiệm nướng Khói Thông", "晚上", "可看松林山丘的烧烤店；有烤鸡和竹筒饭。"),
  ("Tiệm nướng Our Memory", "晚上", "山坡上的烧烤火锅套餐，夜景好；停车位少。"),
  ("Tiệm Gà Hạnh Phúc", "午餐或晚餐", "竹筒饭烤鸡和 lá é 鸡肉火锅。"),
  ("Tiệm nướng Hoàng Hôn", "日落", "城东山坡上的烧烤店，以日落景色出名。"),
  ("Túi Mơ To 花园餐厅", "日落", "鲜花环绕的花园餐厅，山景；有烧烤和火锅。")])
T["ko"] = _mk("달랏 BBQ 맛집: 인기 고깃집 9곳 지도 | Van Phu", "달랏 BBQ 지도",
 "달랏에서 Google 지도 리뷰가 가장 많은 바비큐·구이 맛집 9곳 지도 — 테이블 그릴, 대나무밥 닭구이, 라이스페이퍼 '피자' — 영업시간, 길찾기, 무료 PDF.",
 "쌀쌀한 달랏의 저녁엔 바비큐죠. Google 지도 리뷰가 가장 많은 구이집 9곳 — 테이블 그릴부터 대나무밥 닭구이, 유명한 라이스페이퍼 '피자'까지 — 을 원터치 길찾기와 함께 소개합니다.",
 "시내 (1–7)", "알아두면 좋아요",
 [("영업시간", "대부분 늦은 오후부터; 18:00–20:00가 가장 붐빔"), ("예약", "주말엔 미리 전화하거나 18:00 전에 도착"), ("방식", "대부분 테이블에서 직접 굽고, 훠궈 콤보도 많아요"), ("반납일", "마지막 날은 21:00 전에 스쿠터 반납 — 일찍 먹거나 걸어서 다시 오기")],
 "팁",
 ["술을 마셨다면 운전 금지 — 스쿠터는 두고 Grab을 부르세요.", "호앙지에우 거리에 세 곳이 나란히 있어요 (2–4).", "호앙혼과 뚜이머또는 동쪽에 있고 일몰 뷰가 좋아요.", "관리인이 있는 주차장에만 세우고 잠그세요."],
 [("Nậm Nướng 1900 (쩐푸)", "저녁", "시내 근처의 아주 붐비는 테이블 그릴; 직원이 구워 줘요."),
  ("Nậm Nướng Đà Lạt (호앙지에우)", "저녁", "원조 Nậm Nướng: 테이블 그릴, 음악, 활기찬 분위기."),
  ("BBQ Garden (뷔페)", "저녁", "호앙지에우 거리의 무제한 구이·훠궈 뷔페."),
  ("Bánh tráng nướng Dì Đinh", "오후", "유명한 라이스페이퍼 구이 '베트남 피자' 길거리 간식; 약간 줄 서요."),
  ("Tiệm nướng Khói Thông", "저녁", "소나무 언덕 뷰 구이집; 닭구이와 대나무밥."),
  ("Tiệm nướng Our Memory", "저녁", "언덕 경사면의 구이·훠궈 콤보, 야경; 주차 공간이 좁아요."),
  ("Tiệm Gà Hạnh Phúc", "점심 또는 저녁", "대나무밥 닭구이와 라에 닭 훠궈."),
  ("Tiệm nướng Hoàng Hôn", "일몰", "시내 동쪽 언덕의 구이집, 일몰 뷰로 유명."),
  ("Túi Mơ To Garden Restaurant", "일몰", "꽃이 가득한 정원 레스토랑, 언덕 뷰; 바비큐와 훠궈.")])
T["ja"] = _mk("ダラットのおすすめBBQ：人気焼肉店9選マップ | Van Phu", "ダラットBBQマップ",
 "ダラットでGoogleマップの口コミが多いBBQ・焼き料理の店9選 — テーブル焼肉、竹筒ご飯と焼き鳥、ライスペーパー“ピザ” — 営業時間・道案内・無料PDF付き。",
 "ひんやりしたダラットの夜はBBQが一番。Googleマップで口コミの多い焼き料理の店9選 — テーブル焼肉から竹筒ご飯の焼き鳥、名物のライスペーパー“ピザ”まで — をワンタップ道案内付きで紹介。",
 "市内（1–7）", "知っておきたいこと",
 [("営業時間", "ほとんどが夕方から。18:00〜20:00が一番混む"), ("予約", "週末は電話するか18:00前に"), ("スタイル", "多くはテーブルで焼くタイプ。鍋とのセットも"), ("返却日", "最終日は21:00までにスクーター返却 — 早めに食べるか歩いて戻って")],
 "ポイント",
 ["お酒を飲んだら運転しない — バイクは置いて Grab で。", "ホアンジエウ通りに3店が並んでいます（2〜4）。", "ホアンホンと Túi Mơ To は東側で夕日がきれい。", "見張りのいる駐輪場に停め、鍵をかけて。"],
 [("Nậm Nướng 1900（チャンフー通り）", "夜", "中心部近くの大人気テーブル焼肉。スタッフが焼くのを手伝ってくれます。"),
  ("Nậm Nướng Đà Lạt（ホアンジエウ通り）", "夜", "元祖 Nậm Nướng。テーブル焼肉と音楽でにぎやか。"),
  ("BBQ Garden（ビュッフェ）", "夜", "ホアンジエウ通りの焼肉＆鍋食べ放題。"),
  ("Bánh tráng nướng Dì Đinh", "午後", "名物の焼きライスペーパー“ベトナムピザ”。少し並びます。"),
  ("Tiệm nướng Khói Thông", "夜", "松の丘を望む焼肉店。焼き鳥と竹筒ご飯も。"),
  ("Tiệm nướng Our Memory", "夜", "斜面に建つ焼肉＆鍋セットの店、夜景がきれい。駐車場は狭め。"),
  ("Tiệm Gà Hạnh Phúc", "昼または夜", "竹筒ご飯と焼き鳥、ラーエー入りの鶏鍋。"),
  ("Tiệm nướng Hoàng Hôn", "夕日", "街の東の丘にある焼肉店。夕日の眺めで有名。"),
  ("Túi Mơ To Garden Restaurant", "夕日", "花いっぱいの庭園レストラン、丘の眺め。BBQと鍋。")])
T["th"] = _mk("ปิ้งย่างดาลัด: แผนที่ 9 ร้านยอดนิยม | Van Phu", "แผนที่ร้านปิ้งย่างดาลัด",
 "แผนที่ 9 ร้านปิ้งย่างในดาลัดที่มีรีวิวบน Google Maps มากที่สุด — ย่างบนโต๊ะ ไก่ย่างข้าวหลาม และพิซซ่าแผ่นแป้ง — พร้อมเวลาเปิด เส้นทาง และ PDF ฟรี",
 "เย็นที่หนาวในดาลัดต้องกินปิ้งย่าง นี่คือ 9 ร้านที่มีรีวิวบน Google Maps มากที่สุด ตั้งแต่ย่างบนโต๊ะ ไก่ย่างข้าวหลาม ไปจนถึงแผ่นแป้งย่างชื่อดัง พร้อมนำทางแตะเดียว",
 "ในเมือง (1–7)", "ควรรู้",
 [("เวลาเปิด", "ส่วนใหญ่เปิดช่วงบ่ายแก่ ๆ คนเยอะสุด 18:00–20:00"), ("จองโต๊ะ", "เสาร์อาทิตย์ควรโทรจองหรือไปก่อน 18:00"), ("รูปแบบ", "ส่วนใหญ่ย่างเองบนโต๊ะ มีชุดสุกี้ด้วย"), ("วันคืนรถ", "วันสุดท้ายคืนรถก่อน 21:00 — กินเร็วขึ้นหรือเดินกลับมา")],
 "เคล็ดลับ",
 ["ดื่มแล้วห้ามขับ — จอดรถไว้แล้วเรียก Grab", "ถนน Hoang Dieu มี 3 ร้านติดกัน (2–4)", "Hoang Hon และ Túi Mơ To อยู่ฝั่งตะวันออก วิวพระอาทิตย์ตก", "จอดเฉพาะลานที่มีคนเฝ้าและล็อกรถ"],
 [("Nậm Nướng 1900 (Tran Phu)", "ช่วงค่ำ", "ร้านย่างบนโต๊ะคนแน่นใกล้ใจกลางเมือง พนักงานช่วยย่าง"),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "ช่วงค่ำ", "Nậm Nướng ร้านแรก ย่างบนโต๊ะ มีดนตรี บรรยากาศคึกคัก"),
  ("BBQ Garden (บุฟเฟต์)", "ช่วงค่ำ", "บุฟเฟต์ปิ้งย่างและสุกี้ไม่อั้นบนถนน Hoang Dieu"),
  ("Bánh tráng nướng Dì Đinh", "ช่วงบ่าย", "แผ่นแป้งย่าง 'พิซซ่าเวียดนาม' ชื่อดัง ต้องต่อคิวนิดหน่อย"),
  ("Tiệm nướng Khói Thông", "ช่วงค่ำ", "ร้านปิ้งย่างวิวเนินสน มีไก่ย่างและข้าวหลาม"),
  ("Tiệm nướng Our Memory", "ช่วงค่ำ", "ชุดปิ้งย่างและสุกี้บนเนินชัน วิวกลางคืน ที่จอดรถน้อย"),
  ("Tiệm Gà Hạnh Phúc", "มื้อกลางวันหรือเย็น", "ไก่ย่างข้าวหลามและสุกี้ไก่ใบเอ"),
  ("Tiệm nướng Hoàng Hôn", "พระอาทิตย์ตก", "ร้านปิ้งย่างบนเนินฝั่งตะวันออก ขึ้นชื่อเรื่องวิวพระอาทิตย์ตก"),
  ("Túi Mơ To Garden Restaurant", "พระอาทิตย์ตก", "ร้านอาหารสวนดอกไม้ วิวเนินเขา มีปิ้งย่างและสุกี้")])
T["id"] = _mk("BBQ Terbaik di Da Lat: Peta 9 Restoran Bakar Populer | Van Phu", "Peta BBQ Da Lat",
 "Peta 9 restoran BBQ dan bakar dengan ulasan terbanyak di Da Lat — panggangan di meja, ayam nasi bambu dan 'pizza' kertas nasi — dengan jam buka, petunjuk arah dan PDF gratis.",
 "Malam yang dingin di Da Lat paling pas untuk BBQ. Ini 9 tempat bakar dengan ulasan terbanyak di Google Maps — dari panggangan di meja sampai ayam nasi bambu dan 'pizza' kertas nasi yang terkenal — dengan petunjuk arah sekali ketuk.",
 "Di kota (1–7)", "Perlu diketahui",
 [("Jam buka", "kebanyakan buka sore; paling ramai 18:00–20:00"), ("Reservasi", "akhir pekan telepon dulu atau datang sebelum 18:00"), ("Gaya", "kebanyakan bakar sendiri di meja, sering ada paket hotpot"), ("Hari terakhir sewa", "kembalikan motor sebelum 21:00 — makan lebih awal atau kembali jalan kaki")],
 "Tips",
 ["Jangan berkendara setelah minum — tinggalkan motor dan naik Grab.", "Jalan Hoang Dieu punya tiga tempat bersebelahan (2–4).", "Hoang Hon dan Túi Mơ To di sisi timur dengan pemandangan senja.", "Parkir hanya di tempat berpenjaga dan kunci motor."],
 [("Nậm Nướng 1900 (Tran Phu)", "Malam", "Restoran panggang di meja yang sangat ramai dekat pusat; staf membantu memanggang."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Malam", "Nậm Nướng yang pertama: panggang di meja, musik dan suasana ramai."),
  ("BBQ Garden (prasmanan)", "Malam", "Prasmanan bakar dan hotpot sepuasnya di Jalan Hoang Dieu."),
  ("Bánh tráng nướng Dì Đinh", "Sore", "Jajanan kertas nasi bakar 'pizza Vietnam' yang terkenal; biasanya antre sebentar."),
  ("Tiệm nướng Khói Thông", "Malam", "Restoran bakar dengan pemandangan bukit pinus; ayam bakar dan nasi bambu."),
  ("Tiệm nướng Our Memory", "Malam", "Paket bakar dan hotpot di lereng dengan pemandangan malam; parkir sempit."),
  ("Tiệm Gà Hạnh Phúc", "Makan siang atau malam", "Ayam bakar nasi bambu dan hotpot ayam daun lá é."),
  ("Tiệm nướng Hoàng Hôn", "Senja", "Tempat bakar di lereng bukit timur kota, terkenal dengan pemandangan senja."),
  ("Túi Mơ To Garden Restaurant", "Senja", "Restoran taman penuh bunga dengan pemandangan bukit; BBQ dan hotpot.")])
T["ms"] = _mk("BBQ Terbaik di Da Lat: Peta 9 Restoran Bakar Popular | Van Phu", "Peta BBQ Da Lat",
 "Peta 9 restoran BBQ dan bakar dengan ulasan terbanyak di Da Lat — panggang di meja, ayam nasi buluh dan 'piza' kertas beras — dengan waktu buka, arah dan PDF percuma.",
 "Malam sejuk di Da Lat memang sesuai untuk BBQ. Ini 9 tempat bakar dengan ulasan terbanyak di Google Maps — dari panggang di meja hingga ayam nasi buluh dan 'piza' kertas beras yang terkenal — dengan arah sekali sentuh.",
 "Dalam bandar (1–7)", "Perlu tahu",
 [("Waktu buka", "kebanyakan buka lewat petang; paling sesak 18:00–20:00"), ("Tempahan", "hujung minggu telefon dahulu atau datang sebelum 18:00"), ("Gaya", "kebanyakan bakar sendiri di meja, selalunya dengan set steamboat"), ("Hari terakhir sewa", "pulangkan skuter sebelum 21:00 — makan lebih awal atau datang semula berjalan kaki")],
 "Tip",
 ["Jangan menunggang selepas minum — tinggalkan skuter dan naik Grab.", "Jalan Hoang Dieu ada tiga tempat bersebelahan (2–4).", "Hoang Hon dan Túi Mơ To di sebelah timur dengan pemandangan senja.", "Letak skuter hanya di tempat berpengawal dan kunci."],
 [("Nậm Nướng 1900 (Tran Phu)", "Malam", "Restoran panggang di meja yang sangat sesak dekat pusat; kakitangan bantu memanggang."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Malam", "Nậm Nướng yang asal: panggang di meja, muzik dan suasana meriah."),
  ("BBQ Garden (bufet)", "Malam", "Bufet bakar dan steamboat sepuas hati di Jalan Hoang Dieu."),
  ("Bánh tráng nướng Dì Đinh", "Petang", "Snek kertas beras bakar 'piza Vietnam' yang terkenal; biasanya beratur sekejap."),
  ("Tiệm nướng Khói Thông", "Malam", "Restoran bakar dengan pemandangan bukit pain; ayam bakar dan nasi buluh."),
  ("Tiệm nướng Our Memory", "Malam", "Set bakar dan steamboat di lereng dengan pemandangan malam; parkir terhad."),
  ("Tiệm Gà Hạnh Phúc", "Tengah hari atau malam", "Ayam bakar nasi buluh dan steamboat ayam daun lá é."),
  ("Tiệm nướng Hoàng Hôn", "Senja", "Tempat bakar di lereng bukit timur bandar, terkenal dengan pemandangan senja."),
  ("Túi Mơ To Garden Restaurant", "Senja", "Restoran taman penuh bunga dengan pemandangan bukit; BBQ dan steamboat.")])
T["de"] = _mk("Bestes BBQ in Da Lat: Karte mit 9 beliebten Grill-Restaurants | Van Phu", "BBQ-Karte Da Lat",
 "Karte der 9 Grill- und BBQ-Restaurants mit den meisten Google-Maps-Bewertungen in Da Lat – Tischgrill, Hähnchen mit Bambusreis und Reispapier-„Pizza“ – mit Öffnungszeiten, Route und kostenlosem PDF.",
 "Ein kühler Abend in Da Lat ist wie gemacht für Barbecue. Hier sind die 9 Grill-Lokale mit den meisten Google-Maps-Bewertungen – vom Tischgrill über Hähnchen mit Bambusreis bis zur berühmten Reispapier-„Pizza“ – mit Route per Fingertipp.",
 "In der Stadt (1–7)", "Gut zu wissen",
 [("Öffnungszeiten", "die meisten öffnen am späten Nachmittag; am vollsten 18:00–20:00"), ("Reservieren", "am Wochenende anrufen oder vor 18:00 kommen"), ("Stil", "meist Grill am Tisch, oft mit Hotpot-Kombi"), ("Letzter Miettag", "Roller bis 21:00 zurückgeben – früher essen oder zu Fuß zurückkommen")],
 "Tipps",
 ["Nach Alkohol nicht fahren – Roller stehen lassen und Grab nehmen.", "An der Hoang-Dieu-Straße liegen drei Lokale nebeneinander (2–4).", "Hoang Hon und Túi Mơ To liegen im Osten mit Blick auf den Sonnenuntergang.", "Nur auf bewachten Parkplätzen abstellen und abschließen."],
 [("Nậm Nướng 1900 (Tran Phu)", "Abend", "Sehr gefragtes Tischgrill-Restaurant nahe dem Zentrum; das Personal hilft beim Grillen."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Abend", "Das ursprüngliche Nậm Nướng: Tischgrill, Musik und viel Betrieb."),
  ("BBQ Garden (Buffet)", "Abend", "Grill- und Hotpot-Buffet à discrétion an der Hoang-Dieu-Straße."),
  ("Bánh tráng nướng Dì Đinh", "Nachmittag", "Berühmter gegrillter Reispapier-Snack („vietnamesische Pizza“); kurze Schlange einplanen."),
  ("Tiệm nướng Khói Thông", "Abend", "Grill-Restaurant mit Blick auf Kiefernhügel; gegrilltes Hähnchen und Bambusreis."),
  ("Tiệm nướng Our Memory", "Abend", "Grill- und Hotpot-Kombis am Hang mit Nachtblick; wenig Parkplätze."),
  ("Tiệm Gà Hạnh Phúc", "Mittag oder Abend", "Gegrilltes Hähnchen mit Bambusreis und Hühner-Hotpot mit Lá-é-Kraut."),
  ("Tiệm nướng Hoàng Hôn", "Sonnenuntergang", "Grill am Hang östlich der Stadt, bekannt für den Sonnenuntergang."),
  ("Túi Mơ To Garden Restaurant", "Sonnenuntergang", "Garten-Restaurant voller Blumen mit Hügelblick; BBQ und Hotpot.")])
T["fr"] = _mk("Meilleur barbecue à Da Lat : carte de 9 grills populaires | Van Phu", "Carte des barbecues de Da Lat",
 "Carte des 9 restaurants de grillades les plus notés sur Google Maps à Da Lat — grill de table, poulet au riz en bambou et « pizza » de galette de riz — avec horaires, itinéraire et PDF gratuit.",
 "Une soirée fraîche à Da Lat appelle un barbecue. Voici les 9 adresses de grillades les plus notées sur Google Maps — du grill de table au poulet au riz en bambou et à la célèbre « pizza » de galette de riz — avec itinéraire en un clic.",
 "En ville (1–7)", "Bon à savoir",
 [("Horaires", "la plupart ouvrent en fin d'après-midi ; affluence 18 h–20 h"), ("Réservation", "le week-end, appelez ou arrivez avant 18 h"), ("Formule", "surtout grill à table, souvent avec une fondue (hotpot)"), ("Dernier jour de location", "rendez le scooter avant 21 h — dînez plus tôt ou revenez à pied")],
 "Conseils",
 ["Pas de conduite après avoir bu — laissez le scooter et prenez un Grab.", "Trois adresses côte à côte rue Hoang Dieu (2–4).", "Hoang Hon et Túi Mơ To sont à l'est, avec vue sur le coucher du soleil.", "Garez-vous uniquement sur un parking gardé et verrouillez."],
 [("Nậm Nướng 1900 (Tran Phu)", "Soir", "Grill de table très fréquenté près du centre ; le personnel aide à griller."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Soir", "Le Nậm Nướng d'origine : grill de table, musique et ambiance animée."),
  ("BBQ Garden (buffet)", "Soir", "Buffet grillades et hotpot à volonté rue Hoang Dieu."),
  ("Bánh tráng nướng Dì Đinh", "Après-midi", "La célèbre galette de riz grillée, « pizza vietnamienne » de rue ; petite file d'attente."),
  ("Tiệm nướng Khói Thông", "Soir", "Grill avec vue sur les collines de pins ; poulet grillé et riz en bambou."),
  ("Tiệm nướng Our Memory", "Soir", "Formules grill et hotpot sur une pente avec vue de nuit ; peu de places de parking."),
  ("Tiệm Gà Hạnh Phúc", "Midi ou soir", "Poulet grillé au riz en bambou et fondue de poulet aux herbes lá é."),
  ("Tiệm nướng Hoàng Hôn", "Coucher du soleil", "Grill à flanc de colline à l'est de la ville, réputé pour son coucher de soleil."),
  ("Túi Mơ To Garden Restaurant", "Coucher du soleil", "Restaurant-jardin fleuri avec vue sur les collines ; barbecue et hotpot.")])
T["es"] = _mk("Mejor barbacoa en Da Lat: mapa de 9 parrillas populares | Van Phu", "Mapa de barbacoas de Da Lat",
 "Mapa de los 9 restaurantes de parrilla con más reseñas en Google Maps en Da Lat — parrilla en la mesa, pollo con arroz en bambú y la «pizza» de papel de arroz — con horarios, ruta y PDF gratis.",
 "Una noche fresca en Da Lat pide barbacoa. Aquí tienes los 9 lugares de parrilla con más reseñas en Google Maps — de la parrilla en la mesa al pollo con arroz en bambú y la famosa «pizza» de papel de arroz — con ruta en un toque.",
 "En la ciudad (1–7)", "Conviene saber",
 [("Horario", "la mayoría abre a media tarde; más lleno de 18:00 a 20:00"), ("Reserva", "los fines de semana llama antes o llega antes de las 18:00"), ("Estilo", "casi todos son de parrilla en la mesa, a menudo con combo de hotpot"), ("Último día de alquiler", "devuelve el scooter antes de las 21:00: cena antes o vuelve a pie")],
 "Consejos",
 ["Si bebes, no conduzcas: deja el scooter y pide un Grab.", "En la calle Hoang Dieu hay tres sitios juntos (2–4).", "Hoang Hon y Túi Mơ To están al este, con vistas al atardecer.", "Aparca solo en parkings vigilados y cierra el candado."],
 [("Nậm Nướng 1900 (Tran Phu)", "Noche", "Parrilla en la mesa muy concurrida cerca del centro; el personal ayuda a asar."),
  ("Nậm Nướng Đà Lạt (Hoang Dieu)", "Noche", "El Nậm Nướng original: parrilla en la mesa, música y mucho ambiente."),
  ("BBQ Garden (bufé)", "Noche", "Bufé libre de parrilla y hotpot en la calle Hoang Dieu."),
  ("Bánh tráng nướng Dì Đinh", "Tarde", "La famosa «pizza vietnamita» de papel de arroz a la parrilla; suele haber algo de cola."),
  ("Tiệm nướng Khói Thông", "Noche", "Parrilla con vistas a las colinas de pinos; pollo asado y arroz en bambú."),
  ("Tiệm nướng Our Memory", "Noche", "Combos de parrilla y hotpot en una ladera con vistas nocturnas; poco aparcamiento."),
  ("Tiệm Gà Hạnh Phúc", "Comida o cena", "Pollo asado con arroz en bambú y hotpot de pollo con hierba lá é."),
  ("Tiệm nướng Hoàng Hôn", "Atardecer", "Parrilla en una ladera al este de la ciudad, famosa por su atardecer."),
  ("Túi Mơ To Garden Restaurant", "Atardecer", "Restaurante jardín lleno de flores con vistas a las colinas; barbacoa y hotpot.")])
T["he"] = _mk("הברביקיו הכי טוב בדלאט: מפה של 9 מסעדות גריל פופולריות | Van Phu", "מפת הברביקיו של דלאט",
 "מפה של 9 מסעדות הגריל עם הכי הרבה ביקורות ב-Google Maps בדלאט — גריל על השולחן, עוף עם אורז בבמבוק ו'פיצה' מנייר אורז — עם שעות פתיחה, ניווט ו-PDF בחינם.",
 "ערב קריר בדלאט נועד לברביקיו. הנה 9 מקומות הגריל עם הכי הרבה ביקורות ב-Google Maps — מגריל על השולחן ועד עוף עם אורז בבמבוק וה'פיצה' המפורסמת מנייר אורז — עם ניווט בלחיצה אחת.",
 "בעיר (1–7)", "כדאי לדעת",
 [("שעות", "רובם נפתחים אחר הצהריים המאוחרים; הכי עמוס 18:00–20:00"), ("הזמנה", "בסופי שבוע התקשרו מראש או הגיעו לפני 18:00"), ("סגנון", "בעיקר גריל על השולחן, לרוב עם קומבו הוט-פוט"), ("יום ההשכרה האחרון", "החזירו את הקטנוע עד 21:00 — אכלו מוקדם או חזרו ברגל")],
 "טיפים",
 ["שתיתם — לא נוהגים: השאירו את הקטנוע והזמינו Grab.", "ברחוב הואנג זיאו יש שלושה מקומות צמודים (2–4).", "Hoàng Hôn ו-Túi Mơ To נמצאים במזרח עם נוף לשקיעה.", "חונים רק בחניון שמור ונועלים."],
 [("Nậm Nướng 1900 (טראן פו)", "ערב", "גריל על השולחן עמוס מאוד ליד המרכז; הצוות עוזר לצלות."),
  ("Nậm Nướng Đà Lạt (הואנג זיאו)", "ערב", "ה-Nậm Nướng המקורי: גריל על השולחן, מוזיקה ואווירה תוססת."),
  ("BBQ Garden (בופה)", "ערב", "בופה גריל והוט-פוט ללא הגבלה ברחוב הואנג זיאו."),
  ("Bánh tráng nướng Dì Đinh", "אחר הצהריים", "חטיף רחוב מפורסם של נייר אורז צלוי, 'פיצה וייטנאמית'; לרוב יש תור קצר."),
  ("Tiệm nướng Khói Thông", "ערב", "מסעדת גריל עם נוף לגבעות האורנים; עוף צלוי ואורז בבמבוק."),
  ("Tiệm nướng Our Memory", "ערב", "קומבו גריל והוט-פוט על מדרון עם נוף לילי; מעט חניה."),
  ("Tiệm Gà Hạnh Phúc", "צהריים או ערב", "עוף צלוי עם אורז בבמבוק והוט-פוט עוף עם עשב לה-אה."),
  ("Tiệm nướng Hoàng Hôn", "שקיעה", "גריל על צלע גבעה במזרח העיר, מפורסם בנוף השקיעה."),
  ("Túi Mơ To Garden Restaurant", "שקיעה", "מסעדת גן מלאה פרחים עם נוף לגבעות; ברביקיו והוט-פוט.")])

from content._langs import inject as _inject
_inject(T, __name__)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_VI = {"nn1900": "Nậm Nướng 1900 Trần Phú", "namnuong": "Nậm Nướng Đà Lạt Hoàng Diệu", "bbqgarden": "BBQ Garden Đà Lạt buffet",
       "didinh": "Bánh tráng nướng Dì Đinh", "khoithong": "Tiệm nướng Khói Thông", "ourmemory": "Tiệm nướng Our Memory",
       "gahanhphuc": "Tiệm Gà Hạnh Phúc gà nướng cơm lam", "hoanghon": "Tiệm nướng Hoàng Hôn", "tuimotog": "Túi Mơ To Garden Restaurant"}
def img_link(sid):
    """Temporary photo link: Google Images search for the restaurant name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_VI[sid] + " Đà Lạt")
