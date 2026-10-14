"""Da Lat cloud-hunting & sunrise map — shared data for the website page (/cloud-hunting-map/) and the printable PDF.
Spots = the places Vietnamese travel media name most for "săn mây" (vietnambooking, PLO); coordinates, Google Maps
place links (cid) and opening hours were taken from Google Maps on 2026-10-14.
Shared labels (directions, legend, CTA, address…) are reused from the photo-spot map."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours
SPOTS = [
    ("lake",      11.9407360, 108.4415400, "5068828939661738804",  True,  "free"),
    ("tuyenlam",  11.8998298, 108.4298302, "9322343170370087644",  True,  "free"),
    ("phucduc",   11.9946058, 108.4285696, "18226080706872373889", True,  "free"),
    ("dapu",      11.9820625, 108.4038125, "2826969636196874658",  False, "free"),
    ("honbo",     11.9736875, 108.4894375, "8782362652869302433",  False, "free"),
    ("radar",     12.0325110, 108.4134518, "14635748176987148738", False, "7:30–17:00"),
    ("caudat",    11.8790810, 108.5605080, "7295685080430411598",  False, "6:00–18:00"),
    ("caudatsky", 11.8922897, 108.5684294, "10111923930379290121", False, "4:30–18:00"),
]
CENTER = _PM.CENTER
SLUG = "cloud-hunting-map"
PDF = "VanPhu-Dalat-Cloud-Hunting-Map"
GUIDES = {}
ARTICLE = "caudat"
LANGS = list(_PM.LANGS)
NCENTER = 0
MAPH = 520
H1PT = 21
LEGW = 300
SIDE = {"lake": "b", "tuyenlam": "r", "phucduc": "r", "dapu": "l", "honbo": "r", "radar": "r", "caudat": "bl", "caudatsky": "l"}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, check, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "check": check, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS if x[0] != "honbo"], s))}

T = {}
T["en"] = _mk("Cloud Hunting in Da Lat: Map of 8 Sunrise Spots | Van Phu", "Da Lat Cloud Hunting & Sunrise Map",
 "Where to hunt clouds (săn mây) and watch the sunrise in Da Lat: map of 8 spots with opening hours, the best months and hours, and directions — plus a free PDF.",
 "Seeing a sea of clouds at dawn is Da Lat's signature experience. Here are 8 places to watch it — from the lake in town to the Cau Dat tea hills — with one-tap directions. Our shop opens at 4:30 am, in time for sunrise.",
 "In and near town (1–4)",
 "Clouds are never guaranteed — they depend on the weather that morning. Opening hours are from Google Maps (October 2026).",
 "When are the clouds best?",
 [("Season", "rainy months (about June–August) give the most clouds; cold mornings at the end of the year are also good"), ("Time", "be there 4:30–6:30, before and just after sunrise"), ("Weather", "best after a rainy night with still air"), ("Not every day", "on dry, windy mornings there may be no clouds at all")],
 "Tips for a dawn ride",
 ["Leave in the dark: ride slowly, lights on, and watch for fog.", "Bring a warm jacket and gloves — mornings are cold.", "Da Phu Hill: the last part is steep — park at the bottom and walk up.", "Lang Biang's Radar Peak opens at 7:30 — go for morning views rather than sunrise."],
 [("Xuan Huong Lake", "Sunrise", "Mist over the water at dawn, right in the city centre."),
  ("Tuyen Lam Lake", "Sunrise", "Mist rising from the lake between pine hills."),
  ("Thien Phuc Duc Hill", "Before sunrise", "Short, steep walk to a wide view over the city and pine hills; known for its lone pine."),
  ("Da Phu Hill", "Before sunrise", "Open hilltop above the forest; clouds fill the valley on good mornings."),
  ("Lang Biang – Radar Peak", "Morning", "The highest viewpoint near Da Lat; jeeps go up from the base."),
  ("Cau Dat tea hills", "Early morning", "Tea rows and clouds over the valley; the hill opens at 6:00."),
  ("Cau Dat cloud-hunting spot (Thien Duong San May)", "4:30–6:30", "Paid viewpoint that opens at 4:30; guests mention a ticket with a drink and breakfast.")])
T["vi"] = _mk("Săn mây Đà Lạt: bản đồ 8 điểm ngắm bình minh đẹp nhất | Văn Phú", "Bản đồ săn mây và ngắm bình minh Đà Lạt",
 "Săn mây và ngắm bình minh Đà Lạt ở đâu: bản đồ 8 điểm có giờ mở cửa, tháng và giờ đẹp nhất, chỉ đường — tải miễn phí bản PDF.",
 "Ngắm biển mây lúc bình minh là trải nghiệm đặc trưng của Đà Lạt. Đây là 8 điểm săn mây — từ hồ Xuân Hương trong thành phố đến đồi chè Cầu Đất — có nút chỉ đường. Văn Phú mở cửa từ 4:30 sáng, kịp đi săn mây.",
 "Trong và gần thành phố (1–4)",
 "Mây không phải ngày nào cũng có — tùy thời tiết sáng hôm đó. Giờ mở cửa lấy từ Google Maps (tháng 10/2026).",
 "Khi nào có mây đẹp?",
 [("Mùa", "mùa mưa (khoảng tháng 6–8) nhiều mây nhất; những sáng lạnh cuối năm cũng đẹp"), ("Giờ", "có mặt lúc 4:30–6:30, trước và ngay sau bình minh"), ("Thời tiết", "đẹp nhất sau một đêm mưa, trời lặng gió"), ("Không phải ngày nào cũng có", "sáng khô, gió nhiều có thể không có mây")],
 "Lưu ý khi đi sớm",
 ["Đi lúc trời còn tối: chạy chậm, bật đèn, cẩn thận sương mù.", "Mang áo ấm và găng tay — sáng sớm rất lạnh.", "Đồi Đa Phú: đoạn cuối dốc — nên gửi xe dưới chân đồi rồi đi bộ lên.", "Đỉnh Radar Langbiang mở cửa 7:30 — hợp ngắm view buổi sáng hơn là bình minh."],
 [("Hồ Xuân Hương", "Bình minh", "Sương mù trên mặt hồ lúc rạng sáng, ngay trung tâm."),
  ("Hồ Tuyền Lâm", "Bình minh", "Sương bốc lên từ mặt hồ giữa những đồi thông."),
  ("Đồi Thiên Phúc Đức", "Trước bình minh", "Đi bộ ngắn nhưng dốc, view rộng nhìn thành phố và đồi thông; nổi tiếng với cây thông cô đơn."),
  ("Đồi Đa Phú", "Trước bình minh", "Đỉnh đồi trống trên rừng thông; sáng đẹp mây phủ kín thung lũng."),
  ("Langbiang – đỉnh Radar", "Buổi sáng", "Điểm ngắm cao nhất gần Đà Lạt; có xe jeep đưa lên từ chân núi."),
  ("Đồi chè Cầu Đất", "Sáng sớm", "Đồi chè và mây trên thung lũng; mở cửa từ 6:00."),
  ("Thiên Đường Săn Mây Cầu Đất", "4:30–6:30", "Điểm ngắm có thu vé, mở cửa 4:30; khách cho biết vé kèm nước và bữa sáng.")])
T["ru"] = _mk("Охота за облаками в Далате: карта 8 мест для рассвета | Van Phu", "Карта охоты за облаками и рассветов Далата",
 "Где смотреть море облаков и рассвет в Далате: карта 8 мест с часами работы, лучшими месяцами и временем и маршрутом — плюс бесплатный PDF.",
 "Море облаков на рассвете — визитная карточка Далата. Вот 8 мест, откуда его видно, — от озера в центре до чайных холмов Каудат — с маршрутом в одно касание. Наш прокат открывается в 4:30, как раз к рассвету.",
 "В городе и рядом (1–4)",
 "Облака бывают не каждый день — всё зависит от погоды в то утро. Часы работы — по Google Maps (октябрь 2026).",
 "Когда облака лучше всего?",
 [("Сезон", "в сезон дождей (примерно июнь–август) облаков больше всего; холодные утра в конце года тоже хороши"), ("Время", "будьте на месте в 4:30–6:30, до и сразу после рассвета"), ("Погода", "лучше всего после дождливой ночи, в безветрие"), ("Не каждый день", "сухим ветреным утром облаков может не быть")],
 "Советы для поездки на рассвете",
 ["Выезжаете в темноте: медленно, с фарами, осторожно в тумане.", "Возьмите тёплую куртку и перчатки — утром холодно.", "Холм Дафу: последний участок крутой — оставьте байк внизу и поднимитесь пешком.", "Пик Радар на Ланг Бьянг открывается в 7:30 — это для утренних видов, а не рассвета."],
 [("Озеро Сюанхыонг", "Рассвет", "Туман над водой на рассвете, прямо в центре."),
  ("Озеро Туйенлам", "Рассвет", "Туман поднимается над озером среди сосновых холмов."),
  ("Холм Тхиен Фук Дык", "До рассвета", "Короткий крутой подъём к широкому виду на город и сосны; известен одинокой сосной."),
  ("Холм Дафу", "До рассвета", "Открытая вершина над лесом; в удачное утро облака заполняют долину."),
  ("Ланг Бьянг — пик Радар", "Утро", "Самая высокая смотровая точка у Далата; наверх ходят джипы."),
  ("Чайные холмы Каудат", "Раннее утро", "Чайные ряды и облака над долиной; открыто с 6:00."),
  ("Смотровая Каудат (Тхиен Дыонг Сан Мэй)", "4:30–6:30", "Платная смотровая, открывается в 4:30; гости пишут, что в билет входят напиток и завтрак.")])
T["zh"] = _mk("大叻追云攻略：8个日出观云点地图 | Van Phu", "大叻追云 & 日出地图",
 "大叻哪里追云（săn mây）、看日出：8个地点地图，含开放时间、最佳月份和时段、导航——还可免费下载 PDF。",
 "清晨看云海是大叻最具代表性的体验。这里有8个观云点——从市中心的春香湖到 Cau Dat 茶山——一键导航。我们店早上4:30开门，赶得上日出。",
 "市区及附近（1–4）",
 "云海不是每天都有——取决于当天早上的天气。开放时间来自 Google 地图（2026年10月）。",
 "什么时候云最美？",
 [("季节", "雨季（约6–8月）云最多；年底寒冷的早晨也不错"), ("时间", "4:30–6:30 到达，日出前后"), ("天气", "雨夜过后、无风的早晨最好"), ("不是每天都有", "干燥多风的早晨可能完全没有云")],
 "清晨骑行提示",
 ["天黑出发：慢行、开灯，注意雾。", "带上厚外套和手套——清晨很冷。", "Da Phu 山：最后一段很陡——把车停在山脚，步行上去。", "朗边山雷达峰 7:30 才开——适合看早晨风景，不适合看日出。"],
 [("春香湖", "日出", "黎明时湖面薄雾，就在市中心。"),
  ("宣林湖", "日出", "松林山丘间湖面升起的薄雾。"),
  ("天福德山 Thien Phuc Duc", "日出前", "短而陡的步道，可俯瞰城市和松林；以孤独的松树闻名。"),
  ("Da Phu 山", "日出前", "森林上方的开阔山顶；天气好时云海填满山谷。"),
  ("朗边山 – 雷达峰", "上午", "大叻附近最高的观景点；山脚有吉普车上山。"),
  ("Cau Dat 茶山", "清晨", "茶园和山谷上的云；6:00 开放。"),
  ("Cau Dat 追云天堂 Thien Duong San May", "4:30–6:30", "收费观景点，4:30 开门；有游客提到门票含饮料和早餐。")])
T["ko"] = _mk("달랏 구름 사냥: 일출 명소 8곳 지도 | Van Phu", "달랏 구름 사냥 & 일출 지도",
 "달랏에서 구름 바다(săn mây)와 일출을 볼 수 있는 곳: 운영 시간, 최적의 달과 시간, 길찾기가 있는 8곳 지도 — 무료 PDF도 있습니다.",
 "새벽 구름 바다는 달랏을 대표하는 경험입니다. 시내 쑤언흐엉 호수부터 꺼우닷 차밭까지 8곳을 원터치 길찾기와 함께 소개합니다. 저희 가게는 새벽 4:30에 문을 열어 일출에 맞출 수 있어요.",
 "시내와 근교 (1–4)",
 "구름은 매일 보장되지 않아요 — 그날 아침 날씨에 달려 있습니다. 운영 시간은 Google 지도 기준(2026년 10월).",
 "구름은 언제 가장 좋나요?",
 [("계절", "우기(약 6–8월)에 구름이 가장 많고, 연말의 추운 아침도 좋아요"), ("시간", "4:30–6:30, 일출 전후에 도착"), ("날씨", "비 온 다음 날 바람 없는 아침이 가장 좋아요"), ("매일은 아님", "건조하고 바람 부는 아침엔 구름이 없을 수 있어요")],
 "새벽 라이딩 팁",
 ["어두울 때 출발: 천천히, 라이트 켜고, 안개 조심.", "따뜻한 재킷과 장갑 챙기기 — 새벽은 추워요.", "다푸 언덕: 마지막 구간이 가팔라요 — 아래에 주차하고 걸어 올라가세요.", "랑비앙 레이더 봉우리는 7:30 개장 — 일출보다는 아침 전망용."],
 [("쑤언흐엉 호수", "일출", "시내 한가운데, 새벽 호수 위 물안개."),
  ("뚜옌럼 호수", "일출", "소나무 언덕 사이 호수에서 피어오르는 안개."),
  ("티엔푹득 언덕", "일출 전", "짧지만 가파른 길 끝에 도시와 소나무 언덕 전망; 외로운 소나무로 유명."),
  ("다푸 언덕", "일출 전", "숲 위의 탁 트인 언덕; 좋은 날엔 구름이 계곡을 채워요."),
  ("랑비앙 – 레이더 봉우리", "오전", "달랏 근처 가장 높은 전망대; 아래에서 지프로 올라감."),
  ("꺼우닷 차밭", "이른 아침", "차밭과 계곡 위 구름; 6:00 개장."),
  ("꺼우닷 구름 전망대 (티엔즈엉산머이)", "4:30–6:30", "유료 전망대, 4:30 개장; 음료와 아침 식사가 포함된 티켓이라는 후기.")])
T["ja"] = _mk("ダラットの雲海ハンティング：日の出スポット8選マップ | Van Phu", "ダラット雲海＆日の出マップ",
 "ダラットで雲海（săn mây）と日の出を見るならここ：開門時間、ベストな月と時間帯、道案内付きの8か所マップ — 無料PDFも。",
 "夜明けの雲海はダラットを代表する体験。街なかのスアンフオン湖からカウダットの茶畑まで8か所をワンタップ道案内付きで紹介。当店は朝4:30から営業、日の出に間に合います。",
 "市内と近郊（1–4）",
 "雲海は毎日見られるわけではありません — その朝の天気次第です。開門時間は Googleマップ（2026年10月）より。",
 "雲海がきれいなのはいつ？",
 [("季節", "雨季（6〜8月ごろ）が最も多く、年末の寒い朝もおすすめ"), ("時間", "4:30〜6:30、日の出の前後に到着"), ("天気", "雨の翌朝で風のない日がベスト"), ("毎日ではない", "乾いて風の強い朝は雲が出ないことも")],
 "早朝ライドのコツ",
 ["暗いうちの出発：ゆっくり、ライト点灯、霧に注意。", "暖かい上着と手袋を — 早朝はかなり寒い。", "ダフーの丘：最後は急坂 — 麓にバイクを停めて歩いて登ろう。", "ランビアンのレーダー峰は7:30開門 — 日の出より朝の景色向け。"],
 [("スアンフオン湖", "日の出", "市の中心、夜明けの湖面に立つ朝霧。"),
  ("トゥエンラム湖", "日の出", "松の丘に囲まれた湖から立ちのぼる霧。"),
  ("ティエンフックドゥックの丘", "日の出前", "短いが急な道の先に街と松林の大パノラマ。一本松で有名。"),
  ("ダフーの丘", "日の出前", "森の上の開けた丘。条件がよい朝は谷が雲で埋まります。"),
  ("ランビアン – レーダー峰", "午前", "ダラット近郊でいちばん高い展望地。麓からジープで上がります。"),
  ("カウダット茶畑", "早朝", "茶畑と谷にかかる雲。6:00開園。"),
  ("カウダット雲海スポット（ティエンズオンサンマイ）", "4:30〜6:30", "4:30開門の有料展望地。ドリンクと朝食付きのチケットとの口コミあり。")])
T["th"] = _mk("ล่าทะเลหมอกดาลัด: แผนที่ 8 จุดชมพระอาทิตย์ขึ้น | Van Phu", "แผนที่ล่าทะเลหมอก & พระอาทิตย์ขึ้นดาลัด",
 "ล่าทะเลหมอก (săn mây) และชมพระอาทิตย์ขึ้นที่ไหนในดาลัด: แผนที่ 8 จุด พร้อมเวลาเปิด เดือนและเวลาที่ดีที่สุด และเส้นทาง — ดาวน์โหลด PDF ฟรี",
 "ทะเลหมอกยามเช้าคือประสบการณ์ซิกเนเจอร์ของดาลัด นี่คือ 8 จุดชม ตั้งแต่ทะเลสาบในเมืองถึงไร่ชา Cau Dat พร้อมนำทางแตะเดียว ร้านเราเปิด 4:30 น. ทันพระอาทิตย์ขึ้น",
 "ในและใกล้เมือง (1–4)",
 "ทะเลหมอกไม่ได้มีทุกวัน — ขึ้นอยู่กับอากาศเช้าวันนั้น เวลาเปิดจาก Google Maps (ตุลาคม 2026)",
 "ทะเลหมอกสวยช่วงไหน?",
 [("ฤดู", "หน้าฝน (ราวมิถุนายน–สิงหาคม) หมอกเยอะที่สุด เช้าที่หนาวช่วงปลายปีก็สวย"), ("เวลา", "ไปถึง 4:30–6:30 ก่อนและหลังพระอาทิตย์ขึ้น"), ("อากาศ", "ดีที่สุดหลังคืนที่ฝนตกและลมสงบ"), ("ไม่ได้มีทุกวัน", "เช้าที่แห้งและลมแรงอาจไม่มีหมอกเลย")],
 "เคล็ดลับขี่รถตอนเช้ามืด",
 ["ออกตอนยังมืด: ขี่ช้า เปิดไฟ ระวังหมอก", "เอาเสื้อกันหนาวและถุงมือไปด้วย — เช้ามืดหนาวมาก", "เนิน Da Phu: ช่วงสุดท้ายชันมาก — จอดรถข้างล่างแล้วเดินขึ้น", "ยอด Radar บนหลางเบียงเปิด 7:30 — เหมาะชมวิวตอนเช้ามากกว่าพระอาทิตย์ขึ้น"],
 [("ทะเลสาบซวนเฮือง", "พระอาทิตย์ขึ้น", "หมอกบนผิวน้ำยามรุ่งสาง กลางเมือง"),
  ("ทะเลสาบเตวียนเลิม", "พระอาทิตย์ขึ้น", "หมอกลอยขึ้นจากทะเลสาบท่ามกลางเนินสน"),
  ("เนินเทียนฟุกดึ๊ก", "ก่อนพระอาทิตย์ขึ้น", "เดินสั้นแต่ชัน วิวกว้างเห็นเมืองและเนินสน ขึ้นชื่อเรื่องต้นสนโดดเดี่ยว"),
  ("เนิน Da Phu", "ก่อนพระอาทิตย์ขึ้น", "ยอดเนินโล่งเหนือป่า เช้าที่ดีหมอกจะเต็มหุบเขา"),
  ("หลางเบียง – ยอด Radar", "ช่วงเช้า", "จุดชมวิวที่สูงที่สุดใกล้ดาลัด มีรถจี๊ปพาขึ้นจากตีนเขา"),
  ("ไร่ชา Cau Dat", "เช้าตรู่", "ไร่ชาและทะเลหมอกเหนือหุบเขา เปิด 6:00"),
  ("จุดล่าทะเลหมอก Cau Dat (Thien Duong San May)", "4:30–6:30", "จุดชมวิวเสียค่าเข้า เปิด 4:30 มีรีวิวว่าตั๋วรวมเครื่องดื่มและอาหารเช้า")])
T["id"] = _mk("Berburu Awan di Da Lat: Peta 8 Spot Matahari Terbit | Van Phu", "Peta Berburu Awan & Matahari Terbit Da Lat",
 "Di mana berburu awan (săn mây) dan melihat matahari terbit di Da Lat: peta 8 spot dengan jam buka, bulan dan jam terbaik serta petunjuk arah — plus PDF gratis.",
 "Lautan awan saat fajar adalah pengalaman khas Da Lat. Ini 8 tempat untuk melihatnya — dari danau di pusat kota sampai kebun teh Cau Dat — dengan petunjuk arah sekali ketuk. Toko kami buka pukul 4:30, pas untuk matahari terbit.",
 "Di dalam dan dekat kota (1–4)",
 "Awan tidak dijamin setiap hari — tergantung cuaca pagi itu. Jam buka dari Google Maps (Oktober 2026).",
 "Kapan awannya paling bagus?",
 [("Musim", "musim hujan (sekitar Juni–Agustus) paling banyak awan; pagi dingin di akhir tahun juga bagus"), ("Waktu", "tiba pukul 4:30–6:30, sebelum dan sesaat setelah matahari terbit"), ("Cuaca", "terbaik setelah malam hujan dan angin tenang"), ("Tidak setiap hari", "pagi yang kering dan berangin bisa tanpa awan")],
 "Tips berkendara subuh",
 ["Berangkat saat masih gelap: pelan, lampu menyala, waspada kabut.", "Bawa jaket hangat dan sarung tangan — pagi sangat dingin.", "Bukit Da Phu: bagian akhir curam — parkir di bawah lalu jalan kaki.", "Puncak Radar Lang Biang buka pukul 7:30 — untuk pemandangan pagi, bukan matahari terbit."],
 [("Danau Xuan Huong", "Matahari terbit", "Kabut di atas air saat fajar, di pusat kota."),
  ("Danau Tuyen Lam", "Matahari terbit", "Kabut naik dari danau di antara bukit pinus."),
  ("Bukit Thien Phuc Duc", "Sebelum matahari terbit", "Jalan singkat tapi curam ke pemandangan kota dan bukit pinus; terkenal dengan pinus tunggalnya."),
  ("Bukit Da Phu", "Sebelum matahari terbit", "Puncak terbuka di atas hutan; di pagi yang baik awan memenuhi lembah."),
  ("Lang Biang – Puncak Radar", "Pagi", "Titik pandang tertinggi dekat Da Lat; jip naik dari kaki gunung."),
  ("Kebun teh Cau Dat", "Pagi-pagi", "Kebun teh dan awan di atas lembah; buka pukul 6:00."),
  ("Spot berburu awan Cau Dat (Thien Duong San May)", "4:30–6:30", "Titik pandang berbayar, buka pukul 4:30; tamu menyebut tiket termasuk minuman dan sarapan.")])
T["ms"] = _mk("Memburu Awan di Da Lat: Peta 8 Lokasi Matahari Terbit | Van Phu", "Peta Memburu Awan & Matahari Terbit Da Lat",
 "Di mana memburu awan (săn mây) dan melihat matahari terbit di Da Lat: peta 8 lokasi dengan waktu buka, bulan dan masa terbaik serta arah — serta PDF percuma.",
 "Lautan awan pada waktu subuh ialah pengalaman ikonik Da Lat. Ini 8 tempat untuk melihatnya — dari tasik di pusat bandar hingga ladang teh Cau Dat — dengan arah sekali sentuh. Kedai kami buka jam 4:30 pagi, sempat untuk matahari terbit.",
 "Dalam dan dekat bandar (1–4)",
 "Awan tidak dijamin setiap hari — bergantung pada cuaca pagi itu. Waktu buka daripada Google Maps (Oktober 2026).",
 "Bila awan paling cantik?",
 [("Musim", "musim hujan (kira-kira Jun–Ogos) paling banyak awan; pagi sejuk hujung tahun juga cantik"), ("Masa", "tiba jam 4:30–6:30, sebelum dan sejurus selepas matahari terbit"), ("Cuaca", "terbaik selepas malam hujan dan angin tenang"), ("Bukan setiap hari", "pagi kering dan berangin mungkin tiada awan langsung")],
 "Tip menunggang waktu subuh",
 ["Bertolak ketika masih gelap: perlahan, lampu menyala, berhati-hati dengan kabus.", "Bawa jaket tebal dan sarung tangan — pagi sangat sejuk.", "Bukit Da Phu: bahagian akhir curam — letak motor di bawah dan berjalan naik.", "Puncak Radar Lang Biang buka jam 7:30 — untuk pemandangan pagi, bukan matahari terbit."],
 [("Tasik Xuan Huong", "Matahari terbit", "Kabus di atas air waktu subuh, di tengah bandar."),
  ("Tasik Tuyen Lam", "Matahari terbit", "Kabus naik dari tasik di antara bukit pain."),
  ("Bukit Thien Phuc Duc", "Sebelum matahari terbit", "Jalan pendek tetapi curam ke pemandangan bandar dan bukit pain; terkenal dengan pokok pain tunggal."),
  ("Bukit Da Phu", "Sebelum matahari terbit", "Puncak terbuka di atas hutan; pada pagi yang baik awan memenuhi lembah."),
  ("Lang Biang – Puncak Radar", "Pagi", "Tempat tinjauan tertinggi berhampiran Da Lat; jip naik dari kaki gunung."),
  ("Ladang teh Cau Dat", "Awal pagi", "Ladang teh dan awan di atas lembah; buka jam 6:00."),
  ("Lokasi memburu awan Cau Dat (Thien Duong San May)", "4:30–6:30", "Tempat tinjauan berbayar, buka jam 4:30; pelawat menyebut tiket termasuk minuman dan sarapan.")])
T["de"] = _mk("Wolkenjagd in Da Lat: Karte mit 8 Sonnenaufgangs-Spots | Van Phu", "Wolkenjagd & Sonnenaufgang in Da Lat",
 "Wo man in Da Lat das Wolkenmeer (săn mây) und den Sonnenaufgang sieht: Karte mit 8 Orten, Öffnungszeiten, besten Monaten und Uhrzeiten und Route – plus kostenloses PDF.",
 "Das Wolkenmeer im Morgengrauen ist das Markenzeichen von Da Lat. Hier sind 8 Orte dafür – vom See im Zentrum bis zu den Teehügeln von Cau Dat – mit Route per Fingertipp. Unser Laden öffnet um 4:30 Uhr, rechtzeitig zum Sonnenaufgang.",
 "In und nahe der Stadt (1–4)",
 "Wolken sind nie garantiert – es hängt vom Wetter an diesem Morgen ab. Öffnungszeiten laut Google Maps (Oktober 2026).",
 "Wann sind die Wolken am schönsten?",
 [("Saison", "in der Regenzeit (etwa Juni–August) die meisten Wolken; kalte Morgen zum Jahresende sind auch gut"), ("Uhrzeit", "um 4:30–6:30 vor Ort sein, kurz vor und nach Sonnenaufgang"), ("Wetter", "am besten nach einer Regennacht bei Windstille"), ("Nicht jeden Tag", "an trockenen, windigen Morgen gibt es oft gar keine Wolken")],
 "Tipps für die Fahrt im Morgengrauen",
 ["Im Dunkeln losfahren: langsam, mit Licht, Vorsicht bei Nebel.", "Warme Jacke und Handschuhe mitnehmen – die Morgen sind kalt.", "Da-Phu-Hügel: das letzte Stück ist steil – unten parken und zu Fuß hinauf.", "Der Radar-Gipfel am Lang Biang öffnet um 7:30 – eher für Morgenaussicht als für Sonnenaufgang."],
 [("Xuan-Huong-See", "Sonnenaufgang", "Nebel über dem Wasser im Morgengrauen, mitten im Zentrum."),
  ("Tuyen-Lam-See", "Sonnenaufgang", "Nebel steigt zwischen Kiefernhügeln vom See auf."),
  ("Thien-Phuc-Duc-Hügel", "Vor Sonnenaufgang", "Kurzer, steiler Weg zu weitem Blick über Stadt und Kiefern; bekannt für die einsame Kiefer."),
  ("Da-Phu-Hügel", "Vor Sonnenaufgang", "Offene Kuppe über dem Wald; an guten Morgen füllt das Wolkenmeer das Tal."),
  ("Lang Biang – Radar-Gipfel", "Vormittag", "Höchster Aussichtspunkt bei Da Lat; Jeeps fahren vom Fuß hinauf."),
  ("Teehügel von Cau Dat", "Früher Morgen", "Teefelder und Wolken über dem Tal; ab 6:00 geöffnet."),
  ("Wolken-Aussichtspunkt Cau Dat (Thien Duong San May)", "4:30–6:30", "Kostenpflichtiger Aussichtspunkt, öffnet um 4:30; laut Gästen mit Getränk und Frühstück im Ticket.")])
T["fr"] = _mk("Chasse aux nuages à Da Lat : carte de 8 spots au lever du soleil | Van Phu", "Chasse aux nuages & lever du soleil à Da Lat",
 "Où voir la mer de nuages (săn mây) et le lever du soleil à Da Lat : carte de 8 spots avec horaires, meilleurs mois et heures, itinéraire — plus un PDF gratuit.",
 "La mer de nuages à l'aube est l'expérience emblématique de Da Lat. Voici 8 endroits pour la voir — du lac en centre-ville aux collines de thé de Cau Dat — avec itinéraire en un clic. Notre boutique ouvre à 4 h 30, à temps pour le lever du soleil.",
 "En ville et autour (1–4)",
 "Les nuages ne sont jamais garantis : tout dépend de la météo du matin. Horaires d'après Google Maps (octobre 2026).",
 "Quand les nuages sont-ils les plus beaux ?",
 [("Saison", "la saison des pluies (environ juin–août) offre le plus de nuages ; les matins froids de fin d'année aussi"), ("Heure", "soyez sur place entre 4 h 30 et 6 h 30, avant et juste après le lever du soleil"), ("Météo", "idéal après une nuit de pluie, sans vent"), ("Pas tous les jours", "par matin sec et venteux, il peut n'y avoir aucun nuage")],
 "Conseils pour rouler à l'aube",
 ["Départ dans la nuit : roulez lentement, phares allumés, attention au brouillard.", "Prenez une veste chaude et des gants — les matins sont froids.", "Colline de Da Phu : la fin est raide — garez-vous en bas et montez à pied.", "Le pic Radar du Lang Biang ouvre à 7 h 30 — pour la vue du matin plutôt que le lever du soleil."],
 [("Lac Xuan Huong", "Lever du soleil", "Brume sur l'eau à l'aube, en plein centre."),
  ("Lac Tuyen Lam", "Lever du soleil", "Brume qui monte du lac entre les collines de pins."),
  ("Colline Thien Phuc Duc", "Avant le lever du soleil", "Courte montée raide vers une large vue sur la ville et les pins ; connue pour son pin solitaire."),
  ("Colline de Da Phu", "Avant le lever du soleil", "Sommet dégagé au-dessus de la forêt ; les bons matins, les nuages remplissent la vallée."),
  ("Lang Biang – pic Radar", "Matin", "Le plus haut point de vue près de Da Lat ; des jeeps montent depuis le pied."),
  ("Collines de thé de Cau Dat", "Tôt le matin", "Théiers et nuages sur la vallée ; ouvert dès 6 h."),
  ("Spot à nuages de Cau Dat (Thien Duong San May)", "4 h 30–6 h 30", "Point de vue payant ouvert dès 4 h 30 ; selon les visiteurs, le billet inclut une boisson et un petit-déjeuner.")])
T["es"] = _mk("Caza de nubes en Da Lat: mapa de 8 lugares para el amanecer | Van Phu", "Caza de nubes y amaneceres en Da Lat",
 "Dónde ver el mar de nubes (săn mây) y el amanecer en Da Lat: mapa de 8 lugares con horarios, mejores meses y horas y cómo llegar, más un PDF gratis.",
 "El mar de nubes al amanecer es la experiencia más típica de Da Lat. Aquí tienes 8 lugares para verlo, del lago del centro a las colinas de té de Cau Dat, con ruta en un toque. Nuestra tienda abre a las 4:30, a tiempo para el amanecer.",
 "En la ciudad y cerca (1–4)",
 "Las nubes nunca están garantizadas: dependen del tiempo de esa mañana. Horarios según Google Maps (octubre de 2026).",
 "¿Cuándo hay mejores nubes?",
 [("Temporada", "la época de lluvias (aprox. junio–agosto) trae más nubes; las mañanas frías de fin de año también"), ("Hora", "llega entre las 4:30 y las 6:30, antes y justo después del amanecer"), ("Tiempo", "lo mejor es tras una noche de lluvia y sin viento"), ("No todos los días", "en mañanas secas y con viento puede no haber nubes")],
 "Consejos para salir de madrugada",
 ["Sales de noche: despacio, con luces y cuidado con la niebla.", "Lleva chaqueta y guantes: las mañanas son frías.", "Colina Da Phu: el último tramo es empinado; aparca abajo y sube a pie.", "El pico Radar del Lang Biang abre a las 7:30: mejor para vistas de mañana que para el amanecer."],
 [("Lago Xuan Huong", "Amanecer", "Niebla sobre el agua al alba, en pleno centro."),
  ("Lago Tuyen Lam", "Amanecer", "Niebla que sube del lago entre colinas de pinos."),
  ("Colina Thien Phuc Duc", "Antes del amanecer", "Subida corta y empinada a una amplia vista de la ciudad y los pinos; famosa por su pino solitario."),
  ("Colina Da Phu", "Antes del amanecer", "Cima despejada sobre el bosque; las buenas mañanas las nubes llenan el valle."),
  ("Lang Biang – pico Radar", "Mañana", "El mirador más alto cerca de Da Lat; suben jeeps desde la base."),
  ("Colinas de té de Cau Dat", "A primera hora", "Té y nubes sobre el valle; abre a las 6:00."),
  ("Mirador de nubes de Cau Dat (Thien Duong San May)", "4:30–6:30", "Mirador de pago que abre a las 4:30; los visitantes dicen que la entrada incluye bebida y desayuno.")])
T["he"] = _mk("ציד עננים בדלאט: מפה של 8 נקודות זריחה | Van Phu", "מפת ציד עננים וזריחות בדלאט",
 "איפה רואים ים עננים (săn mây) וזריחה בדלאט: מפה של 8 מקומות עם שעות פתיחה, החודשים והשעות הכי טובים וניווט — ועוד PDF בחינם.",
 "ים עננים עם שחר הוא החוויה הכי מזוהה עם דלאט. הנה 8 מקומות לראות אותו — מהאגם במרכז ועד גבעות התה של קאו דאט — עם ניווט בלחיצה אחת. החנות שלנו פותחת ב-4:30, בדיוק לזריחה.",
 "בעיר ובסביבה (1–4)",
 "עננים אף פעם לא מובטחים — זה תלוי במזג האוויר באותו בוקר. שעות הפתיחה לפי Google Maps (אוקטובר 2026).",
 "מתי העננים הכי יפים?",
 [("עונה", "בעונת הגשמים (בערך יוני–אוגוסט) יש הכי הרבה עננים; גם בקרים קרים בסוף השנה טובים"), ("שעה", "להגיע ב-4:30–6:30, לפני הזריחה ומיד אחריה"), ("מזג אוויר", "הכי טוב אחרי לילה גשום ובלי רוח"), ("לא כל יום", "בבוקר יבש וסוער ייתכן שלא יהיו עננים בכלל")],
 "טיפים לרכיבה עם שחר",
 ["יוצאים בחושך: נוסעים לאט, עם אורות, וזהירים בערפל.", "קחו מעיל חם וכפפות — הבקרים קרים.", "גבעת דה פו: הקטע האחרון תלול — חונים למטה ועולים ברגל.", "פסגת הרדאר בלאנג ביאנג נפתחת ב-7:30 — מתאים לנוף בוקר, לא לזריחה."],
 [("אגם שואן הואנג", "זריחה", "ערפל מעל המים עם שחר, בלב העיר."),
  ("אגם טויין לאם", "זריחה", "ערפל שעולה מהאגם בין גבעות אורנים."),
  ("גבעת טיין פוק דוק", "לפני הזריחה", "עלייה קצרה ותלולה לתצפית רחבה על העיר והאורנים; מפורסמת באורן הבודד."),
  ("גבעת דה פו", "לפני הזריחה", "פסגה פתוחה מעל היער; בבקרים טובים העננים ממלאים את העמק."),
  ("לאנג ביאנג – פסגת הרדאר", "בוקר", "התצפית הגבוהה ביותר ליד דלאט; ג'יפים עולים מהבסיס."),
  ("גבעות התה של קאו דאט", "מוקדם בבוקר", "שורות תה ועננים מעל העמק; פתוח מ-6:00."),
  ("נקודת ציד העננים של קאו דאט (Thien Duong San May)", "4:30–6:30", "תצפית בתשלום שנפתחת ב-4:30; לפי מבקרים הכרטיס כולל שתייה וארוחת בוקר.")])


# Hon Bo Hill (added 2026-10-14): east of town above Thai Phien flower village
_HONBO = {
 "en": ("Hon Bo Hill", "Before sunrise", "Highest hill east of town; sunrise and clouds over Thai Phien flower village. The last stretch is steep red dirt — walk it."),
 "vi": ("Đồi Hòn Bồ", "Trước bình minh", "Đồi cao nhất phía đông thành phố; bình minh và mây phủ làng hoa Thái Phiên. Đoạn cuối là đất đỏ dốc — nên gửi xe đi bộ."),
 "ru": ("Холм Хонбо", "До рассвета", "Самый высокий холм на востоке города; рассвет и облака над цветочной деревней Тхайфиен. Последний участок — крутая красная грунтовка, лучше пешком."),
 "zh": ("Hon Bo 山", "日出前", "城东最高的山丘；可看日出和太平花村上的云海。最后一段是陡峭红土路——建议步行。"),
 "ko": ("혼보 언덕", "일출 전", "시내 동쪽에서 가장 높은 언덕; 타이피엔 꽃마을 위의 일출과 구름. 마지막 구간은 가파른 붉은 흙길 — 걸어가세요."),
 "ja": ("ホンボーの丘", "日の出前", "市の東でいちばん高い丘。タイフィエン花村に広がる日の出と雲海。最後は急な赤土の道なので歩いて。"),
 "th": ("เนินหอนโบ", "ก่อนพระอาทิตย์ขึ้น", "เนินที่สูงที่สุดทางตะวันออกของเมือง ชมพระอาทิตย์ขึ้นและทะเลหมอกเหนือหมู่บ้านดอกไม้ Thai Phien ช่วงท้ายเป็นดินแดงชัน — เดินขึ้นดีกว่า"),
 "id": ("Bukit Hon Bo", "Sebelum matahari terbit", "Bukit tertinggi di timur kota; matahari terbit dan awan di atas desa bunga Thai Phien. Bagian akhir tanah merah curam — jalan kaki saja."),
 "ms": ("Bukit Hon Bo", "Sebelum matahari terbit", "Bukit tertinggi di timur bandar; matahari terbit dan awan di atas kampung bunga Thai Phien. Bahagian akhir tanah merah curam — berjalan kaki."),
 "de": ("Hon-Bo-Hügel", "Vor Sonnenaufgang", "Höchster Hügel östlich der Stadt; Sonnenaufgang und Wolken über dem Blumendorf Thai Phien. Das letzte Stück ist steile rote Erde – zu Fuß gehen."),
 "fr": ("Colline de Hon Bo", "Avant le lever du soleil", "La plus haute colline à l'est de la ville ; lever du soleil et nuages sur le village de fleurs de Thai Phien. La fin est une piste de terre rouge raide — à pied."),
 "es": ("Colina Hon Bo", "Antes del amanecer", "La colina más alta al este de la ciudad; amanecer y nubes sobre el pueblo de flores de Thai Phien. El último tramo es tierra roja empinada: súbelo a pie."),
 "he": ("גבעת הון בו", "לפני הזריחה", "הגבעה הגבוהה ביותר במזרח העיר; זריחה ועננים מעל כפר הפרחים טאי פיין. הקטע האחרון עפר אדום תלול — עדיף ברגל."),
}
for _l in LANGS:
    T[_l]["s"]["honbo"] = _HONBO[_l]
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_VI = {"lake": "hồ Xuân Hương bình minh sương mù", "tuyenlam": "hồ Tuyền Lâm bình minh", "phucduc": "đồi Thiên Phúc Đức săn mây",
       "dapu": "đồi Đa Phú săn mây", "honbo": "đồi Hòn Bồ săn mây", "radar": "đỉnh Radar Langbiang", "caudat": "đồi chè Cầu Đất săn mây", "caudatsky": "Thiên Đường Săn Mây Cầu Đất"}
def img_link(sid):
    """Temporary photo link: Google Images search for the Vietnamese place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_VI[sid] + " Đà Lạt")
