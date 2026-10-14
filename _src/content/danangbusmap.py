"""Da Lat – Da Nang bus map — shared data for the website page (/da-nang-bus-map/) and the printable PDF.
The Da Lat bus station and the Da Lat offices of bus companies on the Da Nang (and Hoi An) route. Companies kept only when
two or more booking sites / guides agree on the route and the Da Lat office matches a Google Maps listing; coordinates,
place links (cid) and opening hours from Google Maps on 2026-10-15. No fares or timetables: they change often.
Left out (conflicting Da Lat addresses or no Google Maps listing): Quang Dung VIP, Quoc Khanh, Hanh Cafe, Vy Van, Cuc Tung office."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours ("—" = not listed on Google Maps)
SPOTS = [
    ("benxe",        11.9269457, 108.4457730, "2479135965201090611",  True, "24h"),
    ("anphu",        11.9380082, 108.4354291, "3300600387922755092",  True, "07:00–21:00"),
    ("thanhthuy",    11.9736479, 108.4524944, "16090994297299609208", True, "07:30–19:00"),
    ("tankimchi",    11.9776782, 108.4494691, "16912884836238683449", True, "—"),
    ("tanquangdung", 11.9593836, 108.4306848, "14619240149507033149", True, "24h"),
    ("hm",           11.9407553, 108.4541227, "7304723431791610941",  True, "—"),
    ("vietlao",      11.9483738, 108.4302501, "3842278573356208289",  True, "07:30–19:30"),
]
CENTER = _PM.CENTER
SLUG = "da-nang-bus-map"
PDF = "VanPhu-Dalat-Da-Nang-Bus-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 7
LEGW = 200
MAPH = 560
H1PT = 22
MAXKM = 5.0
RINGS = (1, 2, 4)
SIDE = {}
JITTER = {}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Da Lat to Da Nang Bus: Map of the Bus Station & Offices | Van Phu", "Da Lat – Da Nang Bus Map",
 "Map of the Da Lat bus station and the Da Lat offices of 6 bus companies to Da Nang and Hoi An — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung and more — with directions and a free PDF.",
 "Heading north to Da Nang or Hoi An? Here is the Da Lat intercity bus station, where FUTA (Phuong Trang) and several other companies depart, and the Da Lat offices of 6 bus companies on the Da Nang route, with one-tap directions. Fares and timetables change often, so check with the company when you book.",
 "In Da Lat (1–7)", "Good to know",
 [("Travel time", "about 12–14 hours, longer with many stops"), ("Departures", "most buses leave Da Lat in the afternoon or early evening and reach Da Nang the next morning"), ("Hoi An", "some buses also stop in Hoi An — ask when you book"), ("Shuttle", "many companies pick up from central hotels — ask when you book")],
 "Tips",
 ["For a ride this long, ask whether the bus has an onboard toilet.", "Keep your passport, phone and money with you, not in the luggage hold.", "The air-conditioning is cold at night — bring a jacket.", "On many cabin buses you leave your shoes at the door — wear socks."],
 [("Da Lat Intercity Bus Station", "Day & night", "Main bus station on To Hien Thanh Street; FUTA (Phuong Trang), Cuc Tung and other companies leave here for Da Nang. Ticket counters and restrooms."),
  ("An Phu Travel", "Day & evening", "Office on Pham Ngu Lao Street with a waiting area; VIP cabin and double-cabin sleeper buses to Da Nang and Hoi An."),
  ("Thanh Thuy", "Daytime", "Office on Nguyen Tu Luc Street, north of the centre; sleeper and double-cabin buses to Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Office on Mai Anh Dao Street, north of the centre; double-cabin limousines with an onboard toilet."),
  ("Tan Quang Dung", "Day & night", "Office by the Lam Dong sports complex, north-west of the centre; double-cabin limousines with an onboard toilet."),
  ("HM Happycar (Hoang Minh)", "—", "Office in the Pham Hong Thai area; double-cabin buses."),
  ("Viet Lao Travel", "Daytime", "Office on Mai Hac De Street; double-cabin buses.")])
T["vi"] = _mk("Xe Đà Lạt đi Đà Nẵng: bản đồ bến xe và văn phòng nhà xe | Văn Phú", "Bản đồ nhà xe Đà Lạt – Đà Nẵng",
 "Bản đồ bến xe liên tỉnh Đà Lạt và văn phòng tại Đà Lạt của 6 nhà xe tuyến Đà Nẵng – Hội An — An Phú, Thanh Thủy, Tân Kim Chi, Tân Quang Dũng… — có chỉ đường và PDF miễn phí.",
 "Ra Đà Nẵng hay Hội An? Đây là bến xe liên tỉnh Đà Lạt, nơi Phương Trang (FUTA) và nhiều nhà xe khác xuất bến, cùng văn phòng tại Đà Lạt của 6 nhà xe tuyến Đà Nẵng, có nút chỉ đường. Giá vé và giờ chạy thay đổi thường xuyên, nên hỏi nhà xe khi đặt vé.",
 "Tại Đà Lạt (1–7)", "Nên biết",
 [("Thời gian", "khoảng 12–14 tiếng, lâu hơn nếu dừng nhiều"), ("Giờ chạy", "đa số xe rời Đà Lạt buổi chiều hoặc chập tối, sáng hôm sau tới Đà Nẵng"), ("Hội An", "một số xe có ghé Hội An — hỏi khi đặt vé"), ("Trung chuyển", "nhiều nhà xe đón tại khách sạn trung tâm — hỏi khi đặt vé")],
 "Lưu ý",
 ["Chặng dài, nên hỏi xe có nhà vệ sinh trên xe không.", "Giữ hộ chiếu, điện thoại và tiền bên người, không để trong khoang hành lý.", "Máy lạnh ban đêm rất lạnh — mang theo áo khoác.", "Nhiều xe giường phòng phải bỏ giày ở cửa — nên mang tất."],
 [("Bến xe Liên tỉnh Đà Lạt", "Cả ngày đêm", "Bến xe chính trên đường Tô Hiến Thành; Phương Trang (FUTA), Cúc Tùng và nhiều nhà xe khác đi Đà Nẵng xuất bến tại đây. Có quầy vé và nhà vệ sinh."),
  ("An Phú Travel", "Ngày và tối", "Văn phòng trên đường Phạm Ngũ Lão, có chỗ ngồi chờ; xe phòng VIP và phòng đôi đi Đà Nẵng, Hội An."),
  ("Thanh Thủy", "Ban ngày", "Văn phòng trên đường Nguyên Tử Lực, phía bắc trung tâm; xe giường nằm và phòng đôi đi Đà Nẵng."),
  ("Tân Kim Chi Limousine", "—", "Văn phòng trên đường Mai Anh Đào, phía bắc trung tâm; limousine phòng đôi có nhà vệ sinh."),
  ("Tân Quang Dũng", "Cả ngày đêm", "Văn phòng ở khu quy hoạch Liên hiệp Thể thao (sân vận động Lâm Đồng); limousine phòng đôi có nhà vệ sinh."),
  ("HM Happycar (Hoàng Minh)", "—", "Văn phòng ở khu Phạm Hồng Thái; xe phòng đôi."),
  ("Việt Lào Travel", "Ban ngày", "Văn phòng trên đường Mai Hắc Đế; xe phòng đôi.")])
T["ru"] = _mk("Автобус Далат – Дананг: карта автовокзала и офисов перевозчиков | Van Phu", "Карта автобусов Далат – Дананг",
 "Карта автовокзала Далата и далатских офисов 6 автобусных компаний до Дананга и Хойана — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung и другие — с маршрутом и бесплатным PDF.",
 "Едете на север, в Дананг или Хойан? Здесь автовокзал Далата, откуда отправляются FUTA (Phuong Trang) и другие компании, и далатские офисы 6 перевозчиков на маршруте до Дананга, с маршрутом в одно касание. Цены и расписание часто меняются — уточняйте у перевозчика при бронировании.",
 "В Далате (1–7)", "Полезно знать",
 [("В пути", "около 12–14 часов, дольше при частых остановках"), ("Отправление", "большинство автобусов уходит из Далата днём или ранним вечером и приходит в Дананг утром"), ("Хойан", "часть автобусов заезжает в Хойан — спросите при бронировании"), ("Трансфер", "многие компании забирают из отелей в центре — спросите при бронировании")],
 "Советы",
 ["Поездка долгая — спросите, есть ли в автобусе туалет.", "Паспорт, телефон и деньги держите при себе, не в багажном отсеке.", "Ночью кондиционер дует холодно — возьмите куртку.", "Во многих автобусах с капсулами обувь оставляют у входа — наденьте носки."],
 [("Автовокзал Далата", "Днём и ночью", "Главный автовокзал на улице Тохиентхань; отсюда в Дананг уходят FUTA (Phuong Trang), Cuc Tung и другие компании. Кассы и туалеты."),
  ("An Phu Travel", "Днём и вечером", "Офис на улице Фамнгулао с зоной ожидания; VIP-капсулы и двухместные капсулы до Дананга и Хойана."),
  ("Thanh Thuy", "Днём", "Офис на улице Нгуентулык, к северу от центра; спальные автобусы и двухместные капсулы до Дананга."),
  ("Tan Kim Chi Limousine", "—", "Офис на улице Майаньдао, к северу от центра; лимузины с двухместными капсулами и туалетом."),
  ("Tan Quang Dung", "Днём и ночью", "Офис у спорткомплекса Ламдонг, к северо-западу от центра; лимузины с двухместными капсулами и туалетом."),
  ("HM Happycar (Hoang Minh)", "—", "Офис у улицы Фамхонгтхай; автобусы с двухместными капсулами."),
  ("Viet Lao Travel", "Днём", "Офис на улице Майхакде; автобусы с двухместными капсулами.")])
T["zh"] = _mk("大叻到岘港巴士：车站与客运公司办事处地图 | Van Phu", "大叻 – 岘港巴士地图",
 "大叻长途汽车站及 6 家开往岘港、会安的客运公司在大叻的办事处地图——An Phu、Thanh Thuy、Tan Kim Chi、Tan Quang Dung 等——附导航和免费 PDF。",
 "要北上岘港或会安？这里是大叻长途汽车站（FUTA 方庄等多家公司由此发车），以及岘港线 6 家客运公司在大叻的办事处，一键导航。票价和班次经常变动，订票时请向客运公司确认。",
 "大叻市内（1–7）", "须知",
 [("车程", "约 12–14 小时，停站多则更久"), ("发车", "多数班车下午或傍晚从大叻出发，次日早上到岘港"), ("会安", "部分班车经停会安——订票时询问"), ("接送", "许多公司可到市中心酒店接客——订票时询问")],
 "小贴士",
 ["路程很长，订票时问清车上是否有厕所。", "护照、手机和钱随身携带，不要放在行李舱。", "夜间空调很冷——带件外套。", "很多包厢车要在门口脱鞋——建议穿袜子。"],
 [("大叻长途汽车站", "全天", "位于苏宪诚路的主汽车站；FUTA（方庄）、Cuc Tung 等公司开往岘港的班车由此发车。设售票处和洗手间。"),
  ("An Phu Travel", "白天和晚上", "范五老路上的办事处，设候车区；VIP 包厢和双人包厢卧铺车开往岘港、会安。"),
  ("Thanh Thuy", "白天", "市中心北面阮子力路上的办事处；卧铺车和双人包厢车开往岘港。"),
  ("Tan Kim Chi Limousine", "—", "市中心北面梅樱桃路上的办事处；带车载厕所的双人包厢豪华车。"),
  ("Tan Quang Dung", "全天", "市中心西北林同体育中心一带的办事处；带车载厕所的双人包厢豪华车。"),
  ("HM Happycar (Hoang Minh)", "—", "范鸿泰一带的办事处；双人包厢巴士。"),
  ("Viet Lao Travel", "白天", "梅黑帝路上的办事处；双人包厢巴士。")])
T["ko"] = _mk("달랏–다낭 버스: 버스터미널·버스회사 사무실 지도 | Van Phu", "달랏 – 다낭 버스 지도",
 "달랏 시외버스터미널과 다낭·호이안행 버스회사 6곳의 달랏 사무실 지도 — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung 등 — 길찾기와 무료 PDF 포함.",
 "다낭이나 호이안으로 북상하시나요? FUTA(프엉짱) 등 여러 회사가 출발하는 달랏 시외버스터미널과 다낭 노선 버스회사 6곳의 달랏 사무실을 한 번에 길찾기할 수 있습니다. 요금과 시간표는 자주 바뀌니 예약할 때 회사에 확인하세요.",
 "달랏 시내 (1–7)", "알아두기",
 [("소요 시간", "약 12–14시간, 정차가 많으면 더 걸림"), ("출발", "대부분 오후나 이른 저녁에 달랏을 출발해 다음 날 아침 다낭 도착"), ("호이안", "일부 버스는 호이안에도 정차 — 예약 시 문의"), ("픽업", "많은 회사가 시내 호텔에서 픽업 — 예약 시 문의")],
 "팁",
 ["긴 구간이니 차내 화장실이 있는지 물어보세요.", "여권·휴대폰·돈은 짐칸이 아니라 몸에 지니세요.", "밤에는 에어컨이 추워요 — 겉옷을 챙기세요.", "캐빈 버스는 입구에서 신발을 벗는 곳이 많아요 — 양말을 신으세요."],
 [("달랏 시외버스터미널", "주야", "또히엔타인 거리의 메인 터미널. FUTA(프엉짱), Cuc Tung 등의 다낭행 버스가 출발. 매표소·화장실."),
  ("An Phu Travel", "낮·저녁", "팜응우라오 거리의 사무실, 대기 공간 있음. 다낭·호이안행 VIP 캐빈과 2인 캐빈 버스."),
  ("Thanh Thuy", "낮", "시내 북쪽 응우옌뜨륵 거리의 사무실. 다낭행 슬리퍼 버스와 2인 캐빈 버스."),
  ("Tan Kim Chi Limousine", "—", "시내 북쪽 마이아인다오 거리의 사무실. 차내 화장실이 있는 2인 캐빈 리무진."),
  ("Tan Quang Dung", "주야", "시내 북서쪽 럼동 종합운동장 부근 사무실. 차내 화장실이 있는 2인 캐빈 리무진."),
  ("HM Happycar (Hoang Minh)", "—", "팜홍타이 지역 사무실. 2인 캐빈 버스."),
  ("Viet Lao Travel", "낮", "마이학데 거리의 사무실. 2인 캐빈 버스.")])
T["ja"] = _mk("ダラット–ダナンのバス：バスターミナルと各社オフィスの地図 | Van Phu", "ダラット – ダナン バスマップ",
 "ダラット長距離バスターミナルと、ダナン・ホイアン行きバス会社 6 社のダラットのオフィスの地図 — An Phu、Thanh Thuy、Tan Kim Chi、Tan Quang Dung など — ルート案内と無料 PDF 付き。",
 "ダナンやホイアンへ北上しますか？FUTA（フーンチャン）など複数の会社が発着するダラット長距離バスターミナルと、ダナン路線のバス会社 6 社のダラットのオフィスを、ワンタップでルート案内。運賃と時刻表はよく変わるので、予約時に会社へ確認してください。",
 "ダラット市内（1–7）", "知っておきたいこと",
 [("所要時間", "約 12–14 時間、停車が多いとさらにかかる"), ("出発", "多くは午後か夕方にダラットを出て、翌朝ダナンに到着"), ("ホイアン", "ホイアンに停まる便もある — 予約時に確認"), ("送迎", "中心部のホテルまで迎えに来る会社が多い — 予約時に確認")],
 "ヒント",
 ["長距離なので、車内トイレがあるか確認しましょう。", "パスポート・スマホ・お金は荷物室ではなく身につけて。", "夜はエアコンが冷えます — 上着を持って。", "キャビンバスは入口で靴を脱ぐことが多い — 靴下を履いて。"],
 [("ダラット長距離バスターミナル", "昼夜", "トーヒエンタイン通りのメインターミナル。FUTA（フーンチャン）や Cuc Tung などのダナン行きが発車。切符売り場とトイレあり。"),
  ("An Phu Travel", "日中・夜", "ファムグーラオ通りのオフィス、待合スペースあり。ダナン・ホイアン行きの VIP キャビンと 2 人用キャビンの寝台バス。"),
  ("Thanh Thuy", "日中", "中心部の北、グエントゥルック通りのオフィス。ダナン行きの寝台バスと 2 人用キャビンバス。"),
  ("Tan Kim Chi Limousine", "—", "中心部の北、マイアンダオ通りのオフィス。車内トイレ付き 2 人用キャビンのリムジン。"),
  ("Tan Quang Dung", "昼夜", "中心部の北西、ラムドン総合運動場のそばのオフィス。車内トイレ付き 2 人用キャビンのリムジン。"),
  ("HM Happycar (Hoang Minh)", "—", "ファムホンタイ地区のオフィス。2 人用キャビンのバス。"),
  ("Viet Lao Travel", "日中", "マイハックデー通りのオフィス。2 人用キャビンのバス。")])
T["th"] = _mk("รถบัสดาลัด–ดานัง: แผนที่สถานีและสำนักงานบริษัทรถ | Van Phu", "แผนที่รถบัสดาลัด – ดานัง",
 "แผนที่สถานีขนส่งดาลัดและสำนักงานในดาลัดของบริษัทรถ 6 แห่งที่วิ่งไปดานังและฮอยอัน — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung และอื่น ๆ — พร้อมนำทางและ PDF ฟรี",
 "จะขึ้นเหนือไปดานังหรือฮอยอัน? นี่คือสถานีขนส่งระหว่างจังหวัดดาลัด ที่ FUTA (ฟองจาง) และอีกหลายบริษัทออกรถ และสำนักงานในดาลัดของบริษัทรถ 6 แห่งในเส้นทางดานัง กดนำทางได้ทันที ค่าโดยสารและเวลารถเปลี่ยนบ่อย ควรสอบถามบริษัทตอนจอง",
 "ในดาลัด (1–7)", "ควรรู้",
 [("เวลาเดินทาง", "ประมาณ 12–14 ชั่วโมง นานกว่านี้ถ้าจอดบ่อย"), ("เวลาออก", "ส่วนใหญ่ออกจากดาลัดช่วงบ่ายหรือหัวค่ำ ถึงดานังเช้าวันรุ่งขึ้น"), ("ฮอยอัน", "บางคันแวะฮอยอันด้วย — ถามตอนจอง"), ("รถรับส่ง", "หลายบริษัทรับจากโรงแรมในตัวเมือง — ถามตอนจอง")],
 "เคล็ดลับ",
 ["ทางไกล ควรถามว่ารถมีห้องน้ำในตัวไหม", "เก็บพาสปอร์ต โทรศัพท์ และเงินไว้กับตัว ไม่ใส่ในช่องเก็บสัมภาระ", "แอร์ตอนกลางคืนหนาว — พกเสื้อแจ็กเก็ต", "รถห้องนอนหลายคันต้องถอดรองเท้าที่ประตู — ใส่ถุงเท้าไป"],
 [("สถานีขนส่งระหว่างจังหวัดดาลัด", "ทั้งวันทั้งคืน", "สถานีหลักบนถนนโตเหียนแทงห์ รถไปดานังของ FUTA (ฟองจาง), Cuc Tung และบริษัทอื่นออกจากที่นี่ มีเคาน์เตอร์ขายตั๋วและห้องน้ำ"),
  ("An Phu Travel", "กลางวันถึงค่ำ", "สำนักงานบนถนนฝ่ามหงูหลาว มีที่นั่งรอ รถห้อง VIP และห้องคู่ไปดานังและฮอยอัน"),
  ("Thanh Thuy", "กลางวัน", "สำนักงานบนถนนเงวียนตื่อหลึก ทางเหนือของตัวเมือง รถนอนและรถห้องคู่ไปดานัง"),
  ("Tan Kim Chi Limousine", "—", "สำนักงานบนถนนไมอันห์ดาว ทางเหนือของตัวเมือง ลีมูซีนห้องคู่มีห้องน้ำ"),
  ("Tan Quang Dung", "ทั้งวันทั้งคืน", "สำนักงานใกล้ศูนย์กีฬาเลิมด่ง ทางตะวันตกเฉียงเหนือของตัวเมือง ลีมูซีนห้องคู่มีห้องน้ำ"),
  ("HM Happycar (Hoang Minh)", "—", "สำนักงานย่านฝ่ามห่งท้าย รถห้องคู่"),
  ("Viet Lao Travel", "กลางวัน", "สำนักงานบนถนนไมฮักเด รถห้องคู่")])
T["id"] = _mk("Bus Da Lat ke Da Nang: Peta Terminal & Kantor Bus | Van Phu", "Peta Bus Da Lat – Da Nang",
 "Peta terminal bus Da Lat dan kantor di Da Lat dari 6 perusahaan bus ke Da Nang dan Hoi An — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung, dan lainnya — dengan petunjuk arah dan PDF gratis.",
 "Mau ke utara, ke Da Nang atau Hoi An? Ini terminal bus antarkota Da Lat, tempat FUTA (Phuong Trang) dan beberapa perusahaan lain berangkat, serta kantor di Da Lat dari 6 perusahaan bus rute Da Nang, dengan petunjuk arah sekali ketuk. Tarif dan jadwal sering berubah, jadi tanyakan ke perusahaan saat memesan.",
 "Di Da Lat (1–7)", "Perlu diketahui",
 [("Waktu tempuh", "sekitar 12–14 jam, lebih lama jika banyak berhenti"), ("Keberangkatan", "sebagian besar bus berangkat dari Da Lat siang atau sore dan tiba di Da Nang keesokan paginya"), ("Hoi An", "beberapa bus juga berhenti di Hoi An — tanyakan saat memesan"), ("Antar-jemput", "banyak perusahaan menjemput dari hotel di pusat kota — tanyakan saat memesan")],
 "Tips",
 ["Perjalanannya panjang — tanyakan apakah bus punya toilet.", "Simpan paspor, ponsel, dan uang di badan, bukan di bagasi.", "AC dingin di malam hari — bawa jaket.", "Di banyak bus kabin sepatu dilepas di pintu — pakai kaus kaki."],
 [("Terminal Bus Antarkota Da Lat", "Siang & malam", "Terminal utama di Jalan To Hien Thanh; bus FUTA (Phuong Trang), Cuc Tung, dan lainnya ke Da Nang berangkat dari sini. Loket tiket dan toilet."),
  ("An Phu Travel", "Siang & malam hari", "Kantor di Jalan Pham Ngu Lao dengan ruang tunggu; bus kabin VIP dan kabin ganda ke Da Nang dan Hoi An."),
  ("Thanh Thuy", "Siang hari", "Kantor di Jalan Nguyen Tu Luc, utara pusat kota; bus tidur dan kabin ganda ke Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Kantor di Jalan Mai Anh Dao, utara pusat kota; limousine kabin ganda dengan toilet."),
  ("Tan Quang Dung", "Siang & malam", "Kantor dekat kompleks olahraga Lam Dong, barat laut pusat kota; limousine kabin ganda dengan toilet."),
  ("HM Happycar (Hoang Minh)", "—", "Kantor di area Pham Hong Thai; bus kabin ganda."),
  ("Viet Lao Travel", "Siang hari", "Kantor di Jalan Mai Hac De; bus kabin ganda.")])
T["ms"] = _mk("Bas Da Lat ke Da Nang: Peta Stesen & Pejabat Bas | Van Phu", "Peta Bas Da Lat – Da Nang",
 "Peta stesen bas Da Lat dan pejabat di Da Lat bagi 6 syarikat bas ke Da Nang dan Hoi An — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung dan lain-lain — dengan arah dan PDF percuma.",
 "Mahu ke utara, ke Da Nang atau Hoi An? Ini stesen bas antara bandar Da Lat, tempat FUTA (Phuong Trang) dan beberapa syarikat lain bertolak, serta pejabat di Da Lat bagi 6 syarikat bas laluan Da Nang, dengan arah sekali sentuh. Tambang dan jadual kerap berubah, jadi semak dengan syarikat semasa menempah.",
 "Di Da Lat (1–7)", "Perlu tahu",
 [("Masa perjalanan", "kira-kira 12–14 jam, lebih lama jika banyak berhenti"), ("Bertolak", "kebanyakan bas bertolak dari Da Lat pada petang atau awal malam dan tiba di Da Nang pagi esoknya"), ("Hoi An", "sesetengah bas juga berhenti di Hoi An — tanya semasa menempah"), ("Pengangkutan", "banyak syarikat mengambil dari hotel di pusat bandar — tanya semasa menempah")],
 "Tip",
 ["Perjalanan jauh — tanya sama ada bas ada tandas.", "Simpan pasport, telefon dan wang pada badan, bukan di ruang bagasi.", "Penghawa dingin sejuk pada waktu malam — bawa jaket.", "Dalam banyak bas kabin, kasut ditanggalkan di pintu — pakai stoking."],
 [("Stesen Bas Antara Bandar Da Lat", "Siang & malam", "Stesen utama di Jalan To Hien Thanh; bas FUTA (Phuong Trang), Cuc Tung dan lain-lain ke Da Nang bertolak dari sini. Kaunter tiket dan tandas."),
  ("An Phu Travel", "Siang & petang", "Pejabat di Jalan Pham Ngu Lao dengan ruang menunggu; bas kabin VIP dan kabin berdua ke Da Nang dan Hoi An."),
  ("Thanh Thuy", "Siang hari", "Pejabat di Jalan Nguyen Tu Luc, utara pusat bandar; bas tidur dan kabin berdua ke Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Pejabat di Jalan Mai Anh Dao, utara pusat bandar; limousine kabin berdua dengan tandas."),
  ("Tan Quang Dung", "Siang & malam", "Pejabat berhampiran kompleks sukan Lam Dong, barat laut pusat bandar; limousine kabin berdua dengan tandas."),
  ("HM Happycar (Hoang Minh)", "—", "Pejabat di kawasan Pham Hong Thai; bas kabin berdua."),
  ("Viet Lao Travel", "Siang hari", "Pejabat di Jalan Mai Hac De; bas kabin berdua.")])
T["de"] = _mk("Bus Da Lat – Da Nang: Karte von Busbahnhof und Busbüros | Van Phu", "Busse Da Lat – Da Nang: Karte",
 "Karte des Busbahnhofs Da Lat und der Büros von 6 Busunternehmen nach Da Nang und Hoi An in Da Lat — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung und weitere — mit Navigation und kostenlosem PDF.",
 "Weiter nach Norden, nach Da Nang oder Hoi An? Hier sind der Fernbusbahnhof von Da Lat, wo FUTA (Phuong Trang) und mehrere andere Unternehmen abfahren, und die Büros von 6 Busunternehmen auf der Strecke nach Da Nang, mit Navigation per Fingertipp. Preise und Fahrpläne ändern sich oft — beim Buchen beim Unternehmen nachfragen.",
 "In Da Lat (1–7)", "Gut zu wissen",
 [("Fahrzeit", "etwa 12–14 Stunden, mit vielen Stopps länger"), ("Abfahrt", "die meisten Busse fahren nachmittags oder am frühen Abend in Da Lat ab und erreichen Da Nang am nächsten Morgen"), ("Hoi An", "einige Busse halten auch in Hoi An — beim Buchen fragen"), ("Abholung", "viele Unternehmen holen an Hotels im Zentrum ab — beim Buchen fragen")],
 "Tipps",
 ["Bei so einer langen Fahrt fragen, ob der Bus eine Toilette hat.", "Pass, Handy und Geld am Körper tragen, nicht im Gepäckraum.", "Die Klimaanlage ist nachts kalt — Jacke mitnehmen.", "In vielen Kabinenbussen zieht man an der Tür die Schuhe aus — Socken tragen."],
 [("Fernbusbahnhof Da Lat", "Tag & Nacht", "Hauptbusbahnhof an der To-Hien-Thanh-Straße; FUTA (Phuong Trang), Cuc Tung und andere fahren hier nach Da Nang ab. Ticketschalter und Toiletten."),
  ("An Phu Travel", "Tag & Abend", "Büro an der Pham-Ngu-Lao-Straße mit Wartebereich; VIP-Kabinen- und Doppelkabinen-Schlafbusse nach Da Nang und Hoi An."),
  ("Thanh Thuy", "Tagsüber", "Büro an der Nguyen-Tu-Luc-Straße nördlich des Zentrums; Schlafbusse und Doppelkabinen nach Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Büro an der Mai-Anh-Dao-Straße nördlich des Zentrums; Doppelkabinen-Limousinen mit Bordtoilette."),
  ("Tan Quang Dung", "Tag & Nacht", "Büro am Sportkomplex Lam Dong nordwestlich des Zentrums; Doppelkabinen-Limousinen mit Bordtoilette."),
  ("HM Happycar (Hoang Minh)", "—", "Büro im Viertel Pham Hong Thai; Busse mit Doppelkabinen."),
  ("Viet Lao Travel", "Tagsüber", "Büro an der Mai-Hac-De-Straße; Busse mit Doppelkabinen.")])
T["fr"] = _mk("Bus Da Lat – Da Nang : carte de la gare routière et des agences | Van Phu", "Carte des bus Da Lat – Da Nang",
 "Carte de la gare routière de Da Lat et des agences à Da Lat de 6 compagnies de bus vers Da Nang et Hoi An — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung et d'autres — avec itinéraire et PDF gratuit.",
 "Vous remontez vers Da Nang ou Hoi An ? Voici la gare routière interprovinciale de Da Lat, d'où partent FUTA (Phuong Trang) et plusieurs autres compagnies, et les agences à Da Lat de 6 compagnies de la ligne Da Nang, avec itinéraire en un geste. Tarifs et horaires changent souvent : vérifiez auprès de la compagnie à la réservation.",
 "À Da Lat (1–7)", "Bon à savoir",
 [("Durée", "environ 12–14 heures, plus avec de nombreux arrêts"), ("Départs", "la plupart des bus quittent Da Lat l'après-midi ou en début de soirée et arrivent à Da Nang le lendemain matin"), ("Hoi An", "certains bus s'arrêtent aussi à Hoi An — demandez à la réservation"), ("Navette", "beaucoup de compagnies viennent chercher à l'hôtel au centre — demandez à la réservation")],
 "Conseils",
 ["Pour un trajet aussi long, demandez si le bus a des toilettes.", "Gardez passeport, téléphone et argent sur vous, pas en soute.", "La climatisation est froide la nuit — prenez une veste.", "Dans beaucoup de bus à cabines, on laisse ses chaussures à l'entrée — mettez des chaussettes."],
 [("Gare routière interprovinciale de Da Lat", "Jour et nuit", "Gare principale rue To Hien Thanh ; FUTA (Phuong Trang), Cuc Tung et d'autres partent d'ici pour Da Nang. Guichets et toilettes."),
  ("An Phu Travel", "Jour et soir", "Agence rue Pham Ngu Lao avec salle d'attente ; bus-couchettes à cabines VIP et cabines doubles vers Da Nang et Hoi An."),
  ("Thanh Thuy", "En journée", "Agence rue Nguyen Tu Luc, au nord du centre ; bus-couchettes et cabines doubles vers Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Agence rue Mai Anh Dao, au nord du centre ; limousines à cabines doubles avec toilettes à bord."),
  ("Tan Quang Dung", "Jour et nuit", "Agence près du complexe sportif de Lam Dong, au nord-ouest du centre ; limousines à cabines doubles avec toilettes à bord."),
  ("HM Happycar (Hoang Minh)", "—", "Agence dans le quartier Pham Hong Thai ; bus à cabines doubles."),
  ("Viet Lao Travel", "En journée", "Agence rue Mai Hac De ; bus à cabines doubles.")])
T["es"] = _mk("Autobús Da Lat – Da Nang: mapa de la estación y las oficinas | Van Phu", "Mapa de autobuses Da Lat – Da Nang",
 "Mapa de la estación de autobuses de Da Lat y de las oficinas en Da Lat de 6 compañías de autobús a Da Nang y Hoi An — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung y más — con indicaciones y PDF gratis.",
 "¿Vas al norte, a Da Nang o Hoi An? Aquí están la estación de autobuses interprovincial de Da Lat, de donde salen FUTA (Phuong Trang) y otras compañías, y las oficinas en Da Lat de 6 compañías de la ruta a Da Nang, con indicaciones en un toque. Precios y horarios cambian a menudo: confírmalos con la compañía al reservar.",
 "En Da Lat (1–7)", "Conviene saber",
 [("Duración", "unas 12–14 horas, más con muchas paradas"), ("Salidas", "la mayoría sale de Da Lat por la tarde o al anochecer y llega a Da Nang a la mañana siguiente"), ("Hoi An", "algunos autobuses también paran en Hoi An — pregunta al reservar"), ("Traslado", "muchas compañías recogen en hoteles del centro — pregunta al reservar")],
 "Consejos",
 ["Para un viaje tan largo, pregunta si el autobús tiene baño.", "Lleva el pasaporte, el móvil y el dinero encima, no en el maletero.", "El aire acondicionado es frío de noche — lleva una chaqueta.", "En muchos autobuses de cabinas se dejan los zapatos en la puerta — lleva calcetines."],
 [("Estación de autobuses interprovincial de Da Lat", "Día y noche", "Estación principal en la calle To Hien Thanh; de aquí salen a Da Nang FUTA (Phuong Trang), Cuc Tung y otras compañías. Taquillas y baños."),
  ("An Phu Travel", "Día y noche temprana", "Oficina en la calle Pham Ngu Lao con sala de espera; autobuses cama con cabinas VIP y dobles a Da Nang y Hoi An."),
  ("Thanh Thuy", "Durante el día", "Oficina en la calle Nguyen Tu Luc, al norte del centro; autobuses cama y cabinas dobles a Da Nang."),
  ("Tan Kim Chi Limousine", "—", "Oficina en la calle Mai Anh Dao, al norte del centro; limusinas con cabinas dobles y baño a bordo."),
  ("Tan Quang Dung", "Día y noche", "Oficina junto al complejo deportivo de Lam Dong, al noroeste del centro; limusinas con cabinas dobles y baño a bordo."),
  ("HM Happycar (Hoang Minh)", "—", "Oficina en la zona de Pham Hong Thai; autobuses con cabinas dobles."),
  ("Viet Lao Travel", "Durante el día", "Oficina en la calle Mai Hac De; autobuses con cabinas dobles.")])
T["he"] = _mk("אוטובוס מדלאט לדא נאנג: מפת התחנה המרכזית ומשרדי החברות | Van Phu", "מפת אוטובוסים דלאט – דא נאנג",
 "מפה של התחנה המרכזית בדלאט ושל משרדי 6 חברות אוטובוסים לדא נאנג ולהוי אן בדלאט — An Phu, Thanh Thuy, Tan Kim Chi, Tan Quang Dung ועוד — עם ניווט ו-PDF בחינם.",
 "נוסעים צפונה לדא נאנג או להוי אן? הנה התחנה הבין-עירונית של דלאט, שממנה יוצאים FUTA (Phuong Trang) ועוד חברות, ומשרדי 6 חברות האוטובוסים בקו דא נאנג בדלאט, עם ניווט בלחיצה אחת. מחירים ולוחות זמנים משתנים לעיתים קרובות — בדקו מול החברה בהזמנה.",
 "בדלאט (1–7)", "כדאי לדעת",
 [("משך הנסיעה", "בערך 12–14 שעות, יותר עם הרבה עצירות"), ("יציאות", "רוב האוטובוסים יוצאים מדלאט אחר הצהריים או בערב המוקדם ומגיעים לדא נאנג בבוקר שלמחרת"), ("הוי אן", "חלק מהאוטובוסים עוצרים גם בהוי אן — שאלו בהזמנה"), ("הסעה", "חברות רבות אוספות ממלונות במרכז — שאלו בהזמנה")],
 "טיפים",
 ["בנסיעה כזאת ארוכה, שאלו אם יש שירותים באוטובוס.", "דרכון, טלפון וכסף — עליכם, לא בתא המטען.", "המזגן קר בלילה — קחו מעיל.", "בהרבה אוטובוסי תאים חולצים נעליים בכניסה — לבשו גרביים."],
 [("התחנה הבין-עירונית של דלאט", "יום ולילה", "התחנה הראשית ברחוב טו הייאן טאן; מכאן יוצאים לדא נאנג FUTA (Phuong Trang), Cuc Tung וחברות אחרות. קופות ושירותים."),
  ("An Phu Travel", "יום וערב", "משרד ברחוב פאם נגו לאו עם אזור המתנה; אוטובוסי שינה עם תאי VIP ותאים זוגיים לדא נאנג ולהוי אן."),
  ("Thanh Thuy", "במשך היום", "משרד ברחוב נגוין טו לוק, צפונית למרכז; אוטובוסי שינה ותאים זוגיים לדא נאנג."),
  ("Tan Kim Chi Limousine", "—", "משרד ברחוב מאי אן דאו, צפונית למרכז; לימוזינות עם תאים זוגיים ושירותים."),
  ("Tan Quang Dung", "יום ולילה", "משרד ליד מתחם הספורט של לאם דונג, צפון-מערבית למרכז; לימוזינות עם תאים זוגיים ושירותים."),
  ("HM Happycar (Hoang Minh)", "—", "משרד באזור פאם הונג טאי; אוטובוסים עם תאים זוגיים."),
  ("Viet Lao Travel", "במשך היום", "משרד ברחוב מאי האק דה; אוטובוסים עם תאים זוגיים.")])

from content._langs import inject as _inject
_inject(T, __name__)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"benxe": "Bến xe liên tỉnh Đà Lạt", "anphu": "An Phú Travel Phạm Ngũ Lão", "thanhthuy": "Nhà xe Thanh Thủy Nguyên Tử Lực",
      "tankimchi": "Tân Kim Chi Limousine Mai Anh Đào", "tanquangdung": "Tân Quang Dũng Limousine", "hm": "HM Happycar Hoàng Minh",
      "vietlao": "Việt Lào Travel Mai Hắc Đế"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
