"""Da Lat Flower Festival 2026 (11th edition) — shared data for the page (/flower-festival-2026/) and the printable PDF.
Facts from Lâm Đồng's press briefing of 8 Oct 2026 as reported by Thanh Niên, VTV and Dân tộc & Phát triển:
19–31 Dec 2026 (planned), theme "Da Lat – a harmony of flowers and music", 11 main + 25 side programmes.
All dates are the organisers' planned dates and may change — the page says so. Coordinates/cids from Google Maps 2026-10-14."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours
SPOTS = [
    ("lamvien",   11.9393622, 108.4452030, "7416178250348386697",  True, "24h"),
    ("vuonhoa",   11.9502479, 108.4498289, "7108760654706798290",  True, "06:30–18:00"),
    ("tqtpark",   11.9447140, 108.4499820, "15091502291687936884", True, "day"),
    ("xuanhuong", 11.9407361, 108.4415404, "5068828939661738804",  True, "free"),
]
CENTER = _PM.CENTER
SLUG = "flower-festival-2026"
PDF = "VanPhu-Dalat-Flower-Festival-2026"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 4
LEGW = 220
MAPH = 520
H1PT = 22
MAXKM = 2.0
RINGS = (1, 2)
SIDE = {}
JITTER = {}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Da Lat Flower Festival 2026: Dates, Programme & Venue Map | Van Phu", "Da Lat Flower Festival 2026",
 "Da Lat Flower Festival 2026 (11th edition): planned for 19–31 December 2026 — opening and closing at Lam Vien Square, flower exhibitions, flower streets — with a venue map, tips and a free PDF.",
 "The 11th Da Lat Flower Festival is planned for 19–31 December 2026, themed \"Da Lat – a harmony of flowers and music\", with 11 main and 25 side programmes. Flower streets and displays spread across the city and are planned to stay until after Lunar New Year. Dates are the organisers' plan and may change.",
 "Festival venues (1–4)", "Programme (planned)",
 [("1–25 Dec", "Lam Dong international orchid exhibition — Tran Quoc Toan Park"), ("18 Dec – 3 Jan", "international flower and ornamental plant exhibition — Da Lat Flower Park"), ("19 Dec, evening", "opening ceremony — Lam Vien Square"), ("31 Dec, evening", "closing and New Year 2027 show — Lam Vien Square")],
 "Tips",
 ["Book your room and scooter early — late December is peak season.", "On opening and closing nights the roads around Lam Vien Square get very busy; park a few streets away and walk.", "Evening shows end after 21:00 — rent for an extra day so you can bring the scooter back the next morning.", "Flower streets are spread across the city — a scooter is the easiest way to see them."],
 [("Lam Vien Square", "Evening", "Main stage: opening on 19 Dec and the closing / New Year 2027 show on 31 Dec (planned)."),
  ("Da Lat Flower Park", "Morning", "International flower and ornamental plant exhibition, 18 Dec 2026 – 3 Jan 2027 (planned)."),
  ("Tran Quoc Toan Park", "Daytime", "Lam Dong international orchid exhibition, 1–25 Dec (planned)."),
  ("Xuan Huong Lake", "Any time", "Flower installations and photo spots around the lake.")])
T["vi"] = _mk("Festival Hoa Đà Lạt 2026: thời gian, chương trình và bản đồ | Văn Phú", "Festival Hoa Đà Lạt 2026",
 "Festival Hoa Đà Lạt lần thứ XI dự kiến 19–31/12/2026 — khai mạc và bế mạc tại quảng trường Lâm Viên, triển lãm hoa, con đường hoa — có bản đồ địa điểm, mẹo và PDF miễn phí.",
 "Festival Hoa Đà Lạt lần thứ XI dự kiến diễn ra 19–31/12/2026 với chủ đề \"Đà Lạt – Bản giao hòa của sắc hoa và âm nhạc\", gồm 11 chương trình chính và 25 chương trình hưởng ứng. Con đường hoa và tiểu cảnh trải khắp thành phố, dự kiến giữ đến qua Tết. Thời gian là dự kiến của ban tổ chức và có thể thay đổi.",
 "Địa điểm festival (1–4)", "Chương trình (dự kiến)",
 [("1–25/12", "Triển lãm lan hồ điệp quốc tế Lâm Đồng — công viên Trần Quốc Toản"), ("18/12 – 3/1", "Triển lãm hoa, cây cảnh quốc tế — Vườn hoa Đà Lạt"), ("Tối 19/12", "Khai mạc — quảng trường Lâm Viên"), ("Tối 31/12", "Bế mạc và chương trình chào năm mới 2027 — quảng trường Lâm Viên")],
 "Lưu ý",
 ["Đặt phòng và thuê xe sớm — cuối tháng 12 là mùa cao điểm.", "Tối khai mạc và bế mạc, đường quanh quảng trường Lâm Viên rất đông; gửi xe cách vài con đường rồi đi bộ.", "Chương trình tối kết thúc sau 21:00 — nên thuê thêm 1 ngày để trả xe sáng hôm sau.", "Con đường hoa trải khắp thành phố — đi xe máy là tiện nhất."],
 [("Quảng trường Lâm Viên", "Buổi tối", "Sân khấu chính: khai mạc 19/12 và bế mạc, chào năm mới 2027 ngày 31/12 (dự kiến)."),
  ("Vườn hoa Đà Lạt", "Buổi sáng", "Triển lãm hoa, cây cảnh quốc tế, 18/12/2026 – 3/1/2027 (dự kiến)."),
  ("Công viên Trần Quốc Toản", "Ban ngày", "Triển lãm lan hồ điệp quốc tế Lâm Đồng, 1–25/12 (dự kiến)."),
  ("Hồ Xuân Hương", "Cả ngày", "Tiểu cảnh hoa và điểm check-in quanh hồ.")])
T["ru"] = _mk("Фестиваль цветов в Далате 2026: даты, программа и карта | Van Phu", "Фестиваль цветов Далата 2026",
 "Фестиваль цветов Далата 2026 (11-й): планируется 19–31 декабря 2026 — открытие и закрытие на площади Ламвьен, выставки цветов, цветочные улицы — карта площадок, советы и бесплатный PDF.",
 "11-й Фестиваль цветов Далата планируется на 19–31 декабря 2026 года под темой «Далат — гармония цветов и музыки»: 11 основных и 25 сопутствующих программ. Цветочные улицы и композиции появятся по всему городу и, по плану, останутся до окончания Тэта. Даты — план организаторов и могут измениться.",
 "Площадки фестиваля (1–4)", "Программа (план)",
 [("1–25 дек.", "международная выставка орхидей Ламдонга — парк Чанкуоктоан"), ("18 дек. – 3 янв.", "международная выставка цветов и декоративных растений — Цветочный парк Далата"), ("19 дек., вечер", "открытие — площадь Ламвьен"), ("31 дек., вечер", "закрытие и новогоднее шоу 2027 — площадь Ламвьен")],
 "Советы",
 ["Бронируйте жильё и байк заранее — конец декабря — пик сезона.", "В вечера открытия и закрытия улицы у площади Ламвьен переполнены; оставьте байк в паре кварталов и пройдитесь пешком.", "Вечерние шоу заканчиваются после 21:00 — возьмите байк на лишний день и верните утром.", "Цветочные улицы по всему городу — на байке их удобнее всего объехать."],
 [("Площадь Ламвьен", "Вечер", "Главная сцена: открытие 19 декабря и закрытие / встреча 2027 года 31 декабря (план)."),
  ("Цветочный парк Далата", "Утро", "Международная выставка цветов и декоративных растений, 18.12.2026 – 3.01.2027 (план)."),
  ("Парк Чанкуоктоан", "Днём", "Международная выставка орхидей Ламдонга, 1–25 декабря (план)."),
  ("Озеро Суанхыонг", "В любое время", "Цветочные композиции и фототочки вокруг озера.")])
T["zh"] = _mk("2026 大叻花节：日期、节目与场地地图 | Van Phu", "2026 大叻花节",
 "第十一届大叻花节计划于 2026 年 12 月 19–31 日举行——林园广场开幕和闭幕、花卉展览、花街——附场地地图、提示和免费 PDF。",
 "第十一届大叻花节计划于 2026 年 12 月 19–31 日举行，主题为“大叻——花与音乐的交响”，共 11 个主要节目和 25 个配套活动。花街和花卉景观遍布全城，计划保留到春节之后。日期为主办方计划，可能变动。",
 "花节场地（1–4）", "节目（计划）",
 [("12 月 1–25 日", "林同国际蝴蝶兰展——陈国瓒公园"), ("12 月 18 日 – 1 月 3 日", "国际花卉与观赏植物展——大叻花园"), ("12 月 19 日晚", "开幕式——林园广场"), ("12 月 31 日晚", "闭幕式及 2027 新年晚会——林园广场")],
 "提示",
 ["尽早订房和租车——12 月下旬是旺季。", "开幕和闭幕当晚林园广场周边非常拥挤；把车停在几条街外再步行。", "晚间演出在 21:00 之后结束——多租一天，第二天早上再还车。", "花街遍布全城——骑摩托车最方便。"],
 [("林园广场", "晚上", "主舞台：12 月 19 日开幕，12 月 31 日闭幕及迎接 2027 新年（计划）。"),
  ("大叻花园", "上午", "国际花卉与观赏植物展，2026.12.18 – 2027.1.3（计划）。"),
  ("陈国瓒公园", "白天", "林同国际蝴蝶兰展，12 月 1–25 日（计划）。"),
  ("春香湖", "全天", "湖边的花卉景观和打卡点。")])
T["ko"] = _mk("2026 달랏 꽃 축제: 일정, 프로그램, 장소 지도 | Van Phu", "2026 달랏 꽃 축제",
 "제11회 달랏 꽃 축제는 2026년 12월 19–31일 예정 — 럼비엔 광장 개막·폐막, 꽃 전시, 꽃길 — 장소 지도, 팁, 무료 PDF.",
 "제11회 달랏 꽃 축제는 2026년 12월 19–31일에 \"달랏 – 꽃과 음악의 하모니\"를 주제로 열릴 예정이며, 주요 프로그램 11개와 부대 행사 25개가 준비됩니다. 꽃길과 꽃 장식이 도시 곳곳에 설치되어 설날 이후까지 유지될 계획입니다. 일정은 주최 측 계획이며 바뀔 수 있습니다.",
 "축제 장소 (1–4)", "프로그램 (예정)",
 [("12월 1–25일", "럼동 국제 호접란 전시 — 쩐꾸옥또안 공원"), ("12월 18일 – 1월 3일", "국제 꽃·관상식물 전시 — 달랏 꽃 정원"), ("12월 19일 저녁", "개막식 — 럼비엔 광장"), ("12월 31일 저녁", "폐막 및 2027 새해 공연 — 럼비엔 광장")],
 "팁",
 ["숙소와 오토바이는 일찍 예약하세요 — 12월 말은 성수기입니다.", "개막·폐막 날 저녁에는 럼비엔 광장 주변이 매우 붐빕니다. 몇 블록 떨어진 곳에 주차하고 걸어가세요.", "저녁 공연은 21:00 이후에 끝나요 — 하루 더 빌려 다음 날 아침에 반납하세요.", "꽃길이 도시 곳곳에 있어 오토바이로 둘러보는 게 가장 편해요."],
 [("럼비엔 광장", "저녁", "메인 무대: 12월 19일 개막, 12월 31일 폐막·2027 새해맞이 (예정)."),
  ("달랏 꽃 정원", "오전", "국제 꽃·관상식물 전시, 2026.12.18 – 2027.1.3 (예정)."),
  ("쩐꾸옥또안 공원", "낮", "럼동 국제 호접란 전시, 12월 1–25일 (예정)."),
  ("쑤언흐엉 호수", "언제든", "호수 주변의 꽃 장식과 포토존.")])
T["ja"] = _mk("ダラット花祭り2026：日程・プログラム・会場マップ | Van Phu", "ダラット花祭り2026",
 "第11回ダラット花祭りは2026年12月19–31日に開催予定。ラムヴィエン広場での開幕・閉幕、花の展示、花の通り。会場マップ・ヒント・無料PDF付き。",
 "第11回ダラット花祭りは2026年12月19–31日に「ダラット — 花と音楽のハーモニー」をテーマに開催予定で、メインプログラム11、関連イベント25が予定されています。花の通りや装飾は街じゅうに設けられ、テト（旧正月）明けまで残される計画です。日程は主催者の予定で、変更の可能性があります。",
 "会場（1–4）", "プログラム（予定）",
 [("12月1–25日", "ラムドン国際胡蝶蘭展 — チャンクオックトアン公園"), ("12月18日 – 1月3日", "国際花・観賞植物展 — ダラット花園"), ("12月19日夜", "開幕式 — ラムヴィエン広場"), ("12月31日夜", "閉幕式と2027年新年ショー — ラムヴィエン広場")],
 "ヒント",
 ["宿とバイクは早めに予約を — 12月下旬はハイシーズンです。", "開幕・閉幕の夜はラムヴィエン広場周辺がとても混雑します。数ブロック離れて停めて歩きましょう。", "夜のショーは21:00過ぎに終わります — 1日延長して翌朝に返却を。", "花の通りは街じゅうにあるので、バイクで回るのが一番便利です。"],
 [("ラムヴィエン広場", "夜", "メインステージ：12月19日に開幕、12月31日に閉幕と2027年の年越し（予定）。"),
  ("ダラット花園", "午前", "国際花・観賞植物展、2026年12月18日 – 2027年1月3日（予定）。"),
  ("チャンクオックトアン公園", "日中", "ラムドン国際胡蝶蘭展、12月1–25日（予定）。"),
  ("スアンフーン湖", "いつでも", "湖のまわりの花の装飾とフォトスポット。")])
T["th"] = _mk("เทศกาลดอกไม้ดาลัด 2026: วันจัดงาน โปรแกรม และแผนที่ | Van Phu", "เทศกาลดอกไม้ดาลัด 2026",
 "เทศกาลดอกไม้ดาลัดครั้งที่ 11 กำหนดจัด 19–31 ธันวาคม 2026 — พิธีเปิดและปิดที่จัตุรัสลัมเวียน นิทรรศการดอกไม้ ถนนดอกไม้ — พร้อมแผนที่ เคล็ดลับ และ PDF ฟรี",
 "เทศกาลดอกไม้ดาลัดครั้งที่ 11 กำหนดจัด 19–31 ธันวาคม 2026 ภายใต้ธีม \"ดาลัด – ความกลมกลืนของดอกไม้และดนตรี\" มีโปรแกรมหลัก 11 รายการและกิจกรรมร่วม 25 รายการ ถนนดอกไม้และการตกแต่งกระจายทั่วเมือง และมีแผนคงไว้จนหลังตรุษญวน วันจัดงานเป็นแผนของผู้จัดและอาจเปลี่ยนแปลง",
 "สถานที่จัดงาน (1–4)", "โปรแกรม (กำหนดการ)",
 [("1–25 ธ.ค.", "นิทรรศการกล้วยไม้ฟาแลนนอปซิสนานาชาติลัมด่ง — สวนเจิ่นก๊วกต๋วน"), ("18 ธ.ค. – 3 ม.ค.", "นิทรรศการดอกไม้และไม้ประดับนานาชาติ — สวนดอกไม้ดาลัด"), ("19 ธ.ค. ค่ำ", "พิธีเปิด — จัตุรัสลัมเวียน"), ("31 ธ.ค. ค่ำ", "พิธีปิดและโชว์ต้อนรับปีใหม่ 2027 — จัตุรัสลัมเวียน")],
 "เคล็ดลับ",
 ["จองที่พักและรถล่วงหน้า — ปลายธันวาคมเป็นช่วงไฮซีซั่น", "คืนพิธีเปิดและปิด ถนนรอบจัตุรัสลัมเวียนแน่นมาก จอดรถห่างออกไปสองสามซอยแล้วเดินเข้าไป", "โชว์ตอนค่ำจบหลัง 21:00 — เช่ารถเพิ่มอีกวันแล้วคืนรถเช้าวันถัดไป", "ถนนดอกไม้กระจายทั่วเมือง — ขี่มอเตอร์ไซค์สะดวกที่สุด"],
 [("จัตุรัสลัมเวียน", "ช่วงค่ำ", "เวทีหลัก: พิธีเปิด 19 ธ.ค. และพิธีปิด/ต้อนรับปี 2027 วันที่ 31 ธ.ค. (กำหนดการ)"),
  ("สวนดอกไม้ดาลัด", "ช่วงเช้า", "นิทรรศการดอกไม้และไม้ประดับนานาชาติ 18 ธ.ค. 2026 – 3 ม.ค. 2027 (กำหนดการ)"),
  ("สวนเจิ่นก๊วกต๋วน", "กลางวัน", "นิทรรศการกล้วยไม้นานาชาติลัมด่ง 1–25 ธ.ค. (กำหนดการ)"),
  ("ทะเลสาบซวนเฮือง", "ทั้งวัน", "การจัดดอกไม้และจุดถ่ายรูปรอบทะเลสาบ")])
T["id"] = _mk("Festival Bunga Da Lat 2026: Tanggal, Program & Peta Lokasi | Van Phu", "Festival Bunga Da Lat 2026",
 "Festival Bunga Da Lat ke-11 direncanakan 19–31 Desember 2026 — pembukaan dan penutupan di Lapangan Lam Vien, pameran bunga, jalan bunga — dengan peta lokasi, tips, dan PDF gratis.",
 "Festival Bunga Da Lat ke-11 direncanakan pada 19–31 Desember 2026 dengan tema \"Da Lat – harmoni bunga dan musik\", berisi 11 program utama dan 25 program pendukung. Jalan bunga dan dekorasi tersebar di seluruh kota dan rencananya dipertahankan hingga setelah Imlek. Tanggal adalah rencana panitia dan bisa berubah.",
 "Lokasi festival (1–4)", "Program (rencana)",
 [("1–25 Des", "pameran anggrek bulan internasional Lam Dong — Taman Tran Quoc Toan"), ("18 Des – 3 Jan", "pameran bunga dan tanaman hias internasional — Taman Bunga Da Lat"), ("19 Des, malam", "pembukaan — Lapangan Lam Vien"), ("31 Des, malam", "penutupan dan pertunjukan Tahun Baru 2027 — Lapangan Lam Vien")],
 "Tips",
 ["Pesan kamar dan motor lebih awal — akhir Desember adalah musim ramai.", "Pada malam pembukaan dan penutupan, jalan di sekitar Lapangan Lam Vien sangat padat; parkir beberapa jalan dari sana lalu jalan kaki.", "Acara malam selesai setelah 21:00 — sewa satu hari ekstra dan kembalikan motor besok paginya.", "Jalan bunga tersebar di seluruh kota — paling mudah dijelajahi dengan motor."],
 [("Lapangan Lam Vien", "Malam", "Panggung utama: pembukaan 19 Des dan penutupan / Tahun Baru 2027 pada 31 Des (rencana)."),
  ("Taman Bunga Da Lat", "Pagi", "Pameran bunga dan tanaman hias internasional, 18 Des 2026 – 3 Jan 2027 (rencana)."),
  ("Taman Tran Quoc Toan", "Siang", "Pameran anggrek internasional Lam Dong, 1–25 Des (rencana)."),
  ("Danau Xuan Huong", "Kapan saja", "Dekorasi bunga dan spot foto di sekitar danau.")])
T["ms"] = _mk("Festival Bunga Da Lat 2026: Tarikh, Program & Peta Lokasi | Van Phu", "Festival Bunga Da Lat 2026",
 "Festival Bunga Da Lat ke-11 dirancang pada 19–31 Disember 2026 — pembukaan dan penutupan di Dataran Lam Vien, pameran bunga, jalan bunga — dengan peta lokasi, tip dan PDF percuma.",
 "Festival Bunga Da Lat ke-11 dirancang pada 19–31 Disember 2026 dengan tema \"Da Lat – harmoni bunga dan muzik\", dengan 11 program utama dan 25 program sampingan. Jalan bunga dan hiasan tersebar di seluruh bandar dan dirancang kekal sehingga selepas Tahun Baru Cina. Tarikh ialah rancangan penganjur dan boleh berubah.",
 "Lokasi festival (1–4)", "Program (rancangan)",
 [("1–25 Dis", "pameran orkid antarabangsa Lam Dong — Taman Tran Quoc Toan"), ("18 Dis – 3 Jan", "pameran bunga dan tumbuhan hiasan antarabangsa — Taman Bunga Da Lat"), ("19 Dis, malam", "majlis pembukaan — Dataran Lam Vien"), ("31 Dis, malam", "penutupan dan persembahan Tahun Baru 2027 — Dataran Lam Vien")],
 "Tip",
 ["Tempah bilik dan motosikal awal — hujung Disember musim puncak.", "Pada malam pembukaan dan penutupan, jalan di sekitar Dataran Lam Vien sangat sesak; letak motosikal beberapa jalan dari situ dan berjalan kaki.", "Persembahan malam tamat selepas 21:00 — sewa sehari lagi dan pulangkan motosikal keesokan paginya.", "Jalan bunga ada di seluruh bandar — paling mudah dilawati dengan motosikal."],
 [("Dataran Lam Vien", "Malam", "Pentas utama: pembukaan 19 Dis dan penutupan / Tahun Baru 2027 pada 31 Dis (rancangan)."),
  ("Taman Bunga Da Lat", "Pagi", "Pameran bunga dan tumbuhan hiasan antarabangsa, 18 Dis 2026 – 3 Jan 2027 (rancangan)."),
  ("Taman Tran Quoc Toan", "Siang", "Pameran orkid antarabangsa Lam Dong, 1–25 Dis (rancangan)."),
  ("Tasik Xuan Huong", "Bila-bila masa", "Hiasan bunga dan tempat bergambar di sekeliling tasik.")])
T["de"] = _mk("Blumenfestival Da Lat 2026: Termine, Programm & Karte | Van Phu", "Blumenfestival Da Lat 2026",
 "Das 11. Blumenfestival Da Lat ist für den 19.–31. Dezember 2026 geplant — Eröffnung und Abschluss auf dem Lam-Vien-Platz, Blumenausstellungen, Blumenstraßen — mit Karte, Tipps und kostenlosem PDF.",
 "Das 11. Blumenfestival Da Lat ist für den 19.–31. Dezember 2026 geplant, Motto: „Da Lat – ein Zusammenklang von Blumen und Musik“, mit 11 Haupt- und 25 Begleitprogrammen. Blumenstraßen und Installationen entstehen in der ganzen Stadt und sollen bis nach dem Mondneujahr (Tết) bleiben. Die Termine sind Planungen der Veranstalter und können sich ändern.",
 "Festivalorte (1–4)", "Programm (geplant)",
 [("1.–25. Dez.", "Internationale Orchideenausstellung Lam Dong — Tran-Quoc-Toan-Park"), ("18. Dez. – 3. Jan.", "Internationale Blumen- und Zierpflanzenausstellung — Blumenpark Da Lat"), ("19. Dez., abends", "Eröffnung — Lam-Vien-Platz"), ("31. Dez., abends", "Abschluss und Neujahrsshow 2027 — Lam-Vien-Platz")],
 "Tipps",
 ["Zimmer und Roller früh buchen — Ende Dezember ist Hochsaison.", "An den Abenden von Eröffnung und Abschluss ist es rund um den Lam-Vien-Platz sehr voll; ein paar Straßen entfernt parken und zu Fuß gehen.", "Abendshows enden nach 21:00 — einen Tag länger mieten und den Roller am nächsten Morgen zurückbringen.", "Die Blumenstraßen sind über die ganze Stadt verteilt — mit dem Roller am einfachsten."],
 [("Lam-Vien-Platz", "Abends", "Hauptbühne: Eröffnung am 19. Dez., Abschluss und Neujahr 2027 am 31. Dez. (geplant)."),
  ("Blumenpark Da Lat", "Morgens", "Internationale Blumen- und Zierpflanzenausstellung, 18.12.2026 – 3.1.2027 (geplant)."),
  ("Tran-Quoc-Toan-Park", "Tagsüber", "Internationale Orchideenausstellung Lam Dong, 1.–25. Dez. (geplant)."),
  ("Xuan-Huong-See", "Jederzeit", "Blumeninstallationen und Fotospots rund um den See.")])
T["fr"] = _mk("Festival des fleurs de Da Lat 2026 : dates, programme et carte | Van Phu", "Festival des fleurs de Da Lat 2026",
 "Le 11e Festival des fleurs de Da Lat est prévu du 19 au 31 décembre 2026 — ouverture et clôture place Lam Vien, expositions florales, rues fleuries — avec carte des lieux, conseils et PDF gratuit.",
 "Le 11e Festival des fleurs de Da Lat est prévu du 19 au 31 décembre 2026 sur le thème « Da Lat – l'harmonie des fleurs et de la musique », avec 11 programmes principaux et 25 programmes associés. Rues fleuries et installations s'étendent dans toute la ville et doivent rester jusqu'après le Têt. Les dates sont celles prévues par les organisateurs et peuvent changer.",
 "Lieux du festival (1–4)", "Programme (prévu)",
 [("1–25 déc.", "exposition internationale d'orchidées de Lam Dong — parc Tran Quoc Toan"), ("18 déc. – 3 janv.", "exposition internationale de fleurs et plantes d'ornement — parc floral de Da Lat"), ("19 déc., soir", "cérémonie d'ouverture — place Lam Vien"), ("31 déc., soir", "clôture et spectacle du Nouvel An 2027 — place Lam Vien")],
 "Conseils",
 ["Réservez chambre et scooter tôt — fin décembre, c'est la haute saison.", "Les soirs d'ouverture et de clôture, les rues autour de la place Lam Vien sont bondées ; garez-vous à quelques rues et finissez à pied.", "Les spectacles du soir finissent après 21 h — louez un jour de plus et rendez le scooter le lendemain matin.", "Les rues fleuries sont dispersées dans la ville — le scooter est le plus pratique."],
 [("Place Lam Vien", "Soir", "Scène principale : ouverture le 19 déc., clôture et Nouvel An 2027 le 31 déc. (prévu)."),
  ("Parc floral de Da Lat", "Matin", "Exposition internationale de fleurs et plantes d'ornement, 18/12/2026 – 3/1/2027 (prévu)."),
  ("Parc Tran Quoc Toan", "Journée", "Exposition internationale d'orchidées de Lam Dong, 1–25 déc. (prévu)."),
  ("Lac Xuan Huong", "À tout moment", "Installations florales et coins photo autour du lac.")])
T["es"] = _mk("Festival de las Flores de Da Lat 2026: fechas, programa y mapa | Van Phu", "Festival de las Flores de Da Lat 2026",
 "El 11.º Festival de las Flores de Da Lat está previsto del 19 al 31 de diciembre de 2026 — apertura y clausura en la plaza Lam Vien, exposiciones florales, calles de flores — con mapa, consejos y PDF gratis.",
 "El 11.º Festival de las Flores de Da Lat está previsto del 19 al 31 de diciembre de 2026 con el lema «Da Lat – armonía de flores y música», con 11 programas principales y 25 complementarios. Calles de flores e instalaciones se reparten por toda la ciudad y está previsto mantenerlas hasta después del Tet. Las fechas son las previstas por los organizadores y pueden cambiar.",
 "Lugares del festival (1–4)", "Programa (previsto)",
 [("1–25 dic.", "exposición internacional de orquídeas de Lam Dong — parque Tran Quoc Toan"), ("18 dic. – 3 ene.", "exposición internacional de flores y plantas ornamentales — Jardín de Flores de Da Lat"), ("19 dic., noche", "inauguración — plaza Lam Vien"), ("31 dic., noche", "clausura y espectáculo de Año Nuevo 2027 — plaza Lam Vien")],
 "Consejos",
 ["Reserva alojamiento y moto con antelación — finales de diciembre es temporada alta.", "Las noches de apertura y clausura las calles junto a la plaza Lam Vien se llenan; aparca a unas calles y sigue a pie.", "Los espectáculos nocturnos terminan después de las 21:00 — alquila un día más y devuelve la moto a la mañana siguiente.", "Las calles de flores están por toda la ciudad — en moto es lo más cómodo."],
 [("Plaza Lam Vien", "Noche", "Escenario principal: inauguración el 19 dic. y clausura / Año Nuevo 2027 el 31 dic. (previsto)."),
  ("Jardín de Flores de Da Lat", "Mañana", "Exposición internacional de flores y plantas ornamentales, 18/12/2026 – 3/1/2027 (previsto)."),
  ("Parque Tran Quoc Toan", "Durante el día", "Exposición internacional de orquídeas de Lam Dong, 1–25 dic. (previsto)."),
  ("Lago Xuan Huong", "Cualquier hora", "Instalaciones florales y rincones para fotos alrededor del lago.")])
T["he"] = _mk("פסטיבל הפרחים של דלאט 2026: תאריכים, תוכנית ומפה | Van Phu", "פסטיבל הפרחים של דלאט 2026",
 "פסטיבל הפרחים ה-11 של דלאט מתוכנן ל-19–31 בדצמבר 2026 — פתיחה וסיום בכיכר לאם וייאן, תערוכות פרחים, רחובות פרחים — עם מפת אתרים, טיפים ו-PDF בחינם.",
 "פסטיבל הפרחים ה-11 של דלאט מתוכנן ל-19–31 בדצמבר 2026 בנושא \"דלאט – הרמוניה של פרחים ומוזיקה\", עם 11 תוכניות מרכזיות ו-25 אירועים נלווים. רחובות פרחים ומיצבים יפוזרו בכל העיר ומתוכננים להישאר עד אחרי טט. התאריכים הם תכנון המארגנים ועשויים להשתנות.",
 "אתרי הפסטיבל (1–4)", "תוכנית (מתוכננת)",
 [("1–25 בדצמבר", "תערוכת סחלבים בינלאומית של לאם דונג — פארק טראן קוק טואן"), ("18 בדצמבר – 3 בינואר", "תערוכת פרחים וצמחי נוי בינלאומית — גן הפרחים של דלאט"), ("19 בדצמבר, ערב", "טקס הפתיחה — כיכר לאם וייאן"), ("31 בדצמבר, ערב", "טקס הסיום ומופע השנה החדשה 2027 — כיכר לאם וייאן")],
 "טיפים",
 ["הזמינו חדר וקטנוע מוקדם — סוף דצמבר הוא שיא העונה.", "בערבי הפתיחה והסיום הרחובות סביב כיכר לאם וייאן עמוסים מאוד; חנו כמה רחובות משם והמשיכו ברגל.", "מופעי הערב מסתיימים אחרי 21:00 — שכרו יום נוסף והחזירו את הקטנוע בבוקר שלמחרת.", "רחובות הפרחים פזורים בכל העיר — הכי נוח לראות אותם בקטנוע."],
 [("כיכר לאם וייאן", "ערב", "הבמה המרכזית: פתיחה ב-19 בדצמבר וסיום / קבלת 2027 ב-31 בדצמבר (מתוכנן)."),
  ("גן הפרחים של דלאט", "בוקר", "תערוכת פרחים וצמחי נוי בינלאומית, 18.12.2026 – 3.1.2027 (מתוכנן)."),
  ("פארק טראן קוק טואן", "במשך היום", "תערוכת סחלבים בינלאומית של לאם דונג, 1–25 בדצמבר (מתוכנן)."),
  ("אגם שואן הואנג", "בכל שעה", "מיצבי פרחים ונקודות צילום סביב האגם.")])

from content._langs import inject as _inject
_inject(T, __name__)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"lamvien": "Quảng trường Lâm Viên Festival Hoa", "vuonhoa": "Vườn hoa Đà Lạt Festival Hoa", "tqtpark": "Công viên Trần Quốc Toản Đà Lạt",
      "xuanhuong": "Hồ Xuân Hương Festival Hoa"}
def img_link(sid):
    """Temporary photo link: Google Images search for the venue."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
