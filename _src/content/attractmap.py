"""Da Lat attractions map — website page (/attractions-map/).
29 places from the attraction list in a Klook travel blog (updated 16 June 2026), each checked against Google Maps on 2026-10-28:
coordinates, Google Maps place link and opening hours come from Google Maps; ticket prices are reference prices taken from
recent visitor reviews, not from the operators. Left out because they could not be found on Google Maps: K'Ho Gong Culture
(Xa Lat), Chuon Chuon Bistro and the Bali Green Hills gate (Greenland 2). Opening hours shown as "—" are not listed on Google Maps."""
from content import photomap as _PM
from content.attractmap_tr import TR as _TR

# id, lat, lng, Google Maps cid or place_id, ok on electric scooter, hours ("—" = not listed on Google Maps)
SPOTS = [
    ("datanla",     11.9034324, 108.4496999, "17928424083927973989",    True,  "7:30–16:30"),
    ("valleylove",  11.9788096, 108.4483081, "ChIJc6HmQ70ScTER9nFcY5EPR7k", True, "7:30–17:00"),
    ("samten",      11.7018809, 108.4197296, "ChIJneCVGe5HcTERs3KKPMik6WM", False, "6:00–20:00"),
    ("flowerplateau", 11.9266145, 108.3712692, "ChIJy0IMmMttcTERFDhXzzS1jB4", True, "7:00–16:30"),
    ("freshgarden", 11.9476933, 108.4090729, "ChIJzXuSUrZtcTERMCq6MmWKNTg", True, "7:30–17:30"),
    ("zoodoo",      12.1120052, 108.5861358, "ChIJ2UqhWvYIcTERBsIJ4kIZl30", False, "8:00–16:00"),
    ("langbiang",   12.0193208, 108.4243879, "ChIJVVVVVaV0cTERz91NGuxuAQQ", False, "7:30–17:00"),
    ("robin",       11.9232151, 108.4437784, "ChIJE8cuCEcTcTERB0WLwyEghrw", True, "7:30–11:45, 13:00–16:45"),
    ("madame",      11.9460096, 108.4258434, "ChIJ84s2rABtcTERcfxQq6Ao1lI", True, "8:00–17:00 (nghỉ Chủ nhật)"),
    ("nuivoi",      11.8265196, 108.4346029, "ChIJKQgUQY8VcTEReZ1UtHSLN1A", False, "8:00–17:00"),
    ("tuyenlam",    11.8998298, 108.4298302, "ChIJm1asQ0xrcTER3KoyuLidX4E", True, "—"),
    ("delight",     11.9582632, 108.4744012, "ChIJg8vJa9UTcTER5OVTIDW4c8c", True, "9:00–22:00"),
    ("tunnel",      11.8825052, 108.4115694, "ChIJv2dGwzhrcTERWbixSfB_mD0", True, "7:00–17:00"),
    ("fairytale",   11.9484697, 108.4029385, "ChIJCcTm2xdtcTERLlbemsPGwVI", True, "7:30–17:00"),
    ("domaine",     11.9496557, 108.4302407, "ChIJ94S-Y9UScTER509fieB9s5I", True, "7:30–11:30, 13:30–17:30"),
    ("pongour",     11.6893042, 108.2656291, "9280240154432551472", False, "7:30–17:00"),
    ("melinh",      11.9001793, 108.3467509, "ChIJKXhINe5rcTERGZUo9qBLUpc", False, "7:30–17:00"),
    ("prenntea",    11.8727353, 108.4684633, "ChIJ20_4v9oVcTERZl_nL0P-Ub0", True, "—"),
    ("voi",         11.8230091, 108.3364973, "5705245422110093707", False, "—"),
    ("linhan",      11.8244336, 108.3335918, "ChIJ957z5P9BcTERJEaADqvwbC8", False, "5:00–17:00"),
    ("nightmarket", 11.9414015, 108.4372912, "ChIJw-dBTv8TcTERPCSnIa35zyE", True, "17:30–24:00"),
    ("vanthanh",    11.9470427, 108.4131516, "ChIJ81XqLIttcTERxaKfjsUtgdc", True, "7:00–17:00"),
    ("longdinh",    11.8644829, 108.5669851, "ChIJq0AhxvEXcTER-_j5nIaMviI", False, "8:00–16:30"),
    ("linhphuoc",   11.9446332, 108.4993224, "ChIJ24TIxRsTcTERG9_-OgIyiSA", True, "—"),
    ("wonderland",  11.8959589, 108.4127443, "ChIJR-Vg6JtrcTERYyYuo7kdjiw", True, "8:00–17:00"),
    ("cauddat",     11.8790807, 108.5605075, "ChIJw3brp90WcTERTv8rLO16P2U", False, "6:00–18:00"),
    ("mongoland",   11.9157314, 108.3392217, "ChIJ5T-k5YBtcTERonwbdDhPzUg", False, "7:00–17:30"),
    ("mongmo",      11.9778728, 108.4451520, "ChIJa_Qc87wScTER41LYPsXeeyM", True, "7:30–17:30"),
    ("tuimoto",     11.9409956, 108.4836846, "ChIJITZmC34TcTERvSGZ7bPair0", True, "7:30–21:30"),
]
CENTER = _PM.CENTER
SLUG = "self-guided-attractions"
PDF = None  # no printable PDF yet — the PDF button is hidden when this is None
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 6
LEGW = 200
MAPH = 470
H1PT = 22
MAXKM = 36.0
RINGS = (5, 15, 30)
SIDE = {}
JITTER = {}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["vi"] = _mk("Các điểm du lịch tự túc ở Đà Lạt: 29 địa điểm, giờ mở cửa và cách đi | Văn Phú", "Các điểm du lịch tự túc ở Đà Lạt",
 "29 điểm du lịch tự túc ở Đà Lạt: thác, đồi chè, chùa, chợ đêm, vườn hoa — giờ mở cửa theo Google Maps, giá vé tham khảo và chỉ đường từng điểm.",
 "29 điểm đến hay được khách ghi trong lịch trình Đà Lạt: thác, đồi chè, chùa, vườn hoa và chợ đêm. Phần lớn nằm trong bán kính 15 km quanh hồ Xuân Hương; Pongour, Samten Hills và ZooDoo đi xa hơn, nên xếp cho ngày riêng.",
 "Địa điểm (1–29)", "Thời gian đẹp",
 [("Mùa khô (khoảng tháng 11–4)", "trời ít mưa hơn, dễ ngắm hoa và đi xa"), ("Sáng sớm", "đồi chè, Đồi Mộng Mơ và Langbiang hay có mây và sương đẹp hơn"), ("Ngày trong tuần", "ít khách hơn hẳn các cuối tuần"), ("Cuối tuần & Tết", "Valley of Love, Fresh Garden, Langbiang đông và dễ kẹt xe")],
 "Lưu ý",
 ["Giá vé trong bản đồ là giá tham khảo từ đánh giá khách gần đây — kiểm tra lại tại cổng trước khi đi.",
  "Madame De Dalat nghỉ Chủ nhật; nhà thờ Domaine de Marie nghỉ trưa 11:30–13:30.",
  "Thác Voi và Tea Resort Prenn có đánh giá nói thác tạm đóng và dịch vụ chưa đầy đủ — hỏi trước khi đi xa.",
  "Samten Hills, ZooDoo và Pongour cách trung tâm 25–35 km — nên đi xe máy 125cc hoặc xe máy điện có pin đủ."],
 [("Thác Datanla", "Buổi sáng", "Thác giữa rừng thông đèo Prenn; xuống thác bằng máng trượt 2,4 km hoặc đi bộ. Giá vé tham khảo 30.000–50.000 VND, trò chơi tính thêm."),
  ("Thung lũng Tình Yêu", "Buổi sáng hoặc chiều", "Khu công viên rộng với vườn hoa, cầu kính, máng trượt và xe trượt. Đánh giá gần đây cho biết vé khoảng 250.000 VND nếu vào toàn bộ khu; nên đến trước 3 tiếng để đi hết."),
  ("Samten Hills", "Buổi sáng", "Khu chùa Phật giáo Tây Tạng ở Đơn Dương, có bánh xe kinh bằng đồng lớn (theo đánh giá khách). Cách trung tâm khoảng 27 km."),
  ("Cao nguyên Hoa (Flower Plateau)", "Buổi sáng", "Khu sinh thái trên đồi Tà Nung với nhà gỗ giữa rừng thông và vườn hoa. Đường đua go-kart xuống dốc là điểm vui của khu này theo đánh giá khách."),
  ("Fresh Garden", "Buổi sáng", "Vườn hoa rộng ở Vạn Thành, có sở thú, hồ cá và quán cà phê. Vé có đồ uống; khách hay đặt online rẻ hơn."),
  ("ZooDoo", "Buổi sáng", "Sở thú trong rừng thông ở Lạc Dương (cách trung tâm khoảng 25 km), đi tour có hướng dẫn 1,5–2 giờ. Số khách mỗi ngày có hạn nên đặt trước ít nhất một ngày."),
  ("Núi Langbiang", "Buổi sáng sớm", "Núi cao khoảng 2.167 m; đi xe jeep hoặc xe chuyên dụng lên đỉnh Radar, hoặc đi bộ theo rừng. Ngày nhiều mây thì không thấy được toàn cảnh."),
  ("Đồi Robin và cáp treo", "Buổi sáng", "Ga cáp treo khoảng 2 km tới Thiền viện Trúc Lâm, mất khoảng 10–15 phút mỗi chiều. Vé khứ hồi tham khảo khoảng 150.000 VND."),
  ("Madame De Dalat", "Buổi sáng", "Biệt thự cũ của bà Trần Lệ Xuân, xây năm 1958, có vườn và bảo tàng. Vé khoảng 150.000–180.000 VND theo đánh giá; nghỉ Chủ nhật."),
  ("Rừng thông Núi Voi", "Cả ngày", "Rừng thông đỏ hiếm với nhiều cây cổ thụ, có thác bậc, chèo kayak và go-kart. Go-kart khoảng 250.000 VND theo đánh giá."),
  ("Hồ Tuyền Lâm", "Chiều muộn", "Hồ rộng khoảng 320 ha, cách trung tâm khoảng 5 km; đạp vịt, thuyền và ngắm hoàng hôn ven hồ. Có đánh giá phàn nàn về rác ven hồ."),
  ("Delight Park Đà Lạt", "Buổi tối", "Công viên giải trí có vườn hoa, trò chơi và show ánh sáng về đêm. Show Âu Lạc có đánh giá trái chiều, nên xem lịch trước."),
  ("Đường hầm điêu khắc", "Buổi sáng", "Hành lang đất sét đỏ có tượng mô tả lịch sử và cảnh quan thành phố. Vé khoảng 120.000 VND/người theo đánh giá; khu 'Vô cực' bên hồ hay được chụp ảnh."),
  ("Fairytale Land (Vùng Đất Cổ Tích)", "Buổi sáng", "Khu vườn theo phong cách cổ tích, nhà tròn kiểu Hobbit và hầm rượu Vĩnh Tiến. Vé khoảng 90.000 VND; uống rượu tính thêm."),
  ("Nhà thờ Domaine de Marie", "Buổi sáng", "Nhà thờ màu hồng trên đồi Mai Anh, có vườn hoa; vào cửa miễn phí. Giờ đẹp là sáng sớm, nhớ không đứng chặn lối lễ."),
  ("Thác Pongour", "Cả ngày", "Thác bảy bậc đá phủ rêu, cách Đà Lạt khoảng 50 km; xe điện xuống thác khoảng 15.000 VND mỗi chiều. Đường trơn sau mưa."),
  ("Đồn điền cà phê Mê Linh", "Buổi sáng", "Đồn điền cà phê có tour tham quan khâu chế biến và xem chồn hương làm cà phê Weasel. Có cơm lam và thịt nướng."),
  ("Tea Resort Prenn", "Buổi sáng", "Khu nghỉ dưỡng cạnh thác Prenn, có trò chơi ngoài trời. Đánh giá gần đây nhận xét dịch vụ và tiện ích chưa đồng đều; hỏi trước khi mua vé."),
  ("Thác Voi (Nam Ban)", "Buổi sáng", "Thác lớn cạnh chùa Linh Ẩn, cách trung tâm khoảng 17 km. Có lúc tạm đóng; khi đó vẫn ngắm được từ chùa."),
  ("Chùa Linh Ẩn", "Buổi sáng", "Chùa có tượng Phật Bà Quan Âm cao 71 m và tượng Di Lặc trắng. Vào cửa miễn phí, gửi xe miễn phí."),
  ("Chợ đêm Đà Lạt", "Buổi tối", "Chợ đêm ở đường Nguyễn Thị Minh Khai, mở từ khoảng 17:30 đến tối khuya. Có bánh tráng nướng, sữa đậu nành nóng, bánh ướt lòng gà. Cẩn thận người chèo kéo."),
  ("Làng hoa Vạn Thành", "Buổi sáng", "Làng hoa và rau củ ở Vạn Thành; vé khoảng 100.000 VND/người theo đánh giá. Hoa đẹp nhất theo mùa, nên xem trước ảnh."),
  ("Bảo tàng Trà Long Đỉnh", "Buổi sáng", "Bảo tàng trà ở Trại Mát với tour sản xuất và uống trà; vé khoảng 100.000–150.000 VND tùy gói. Có ưu đãi đồ uống trong vé."),
  ("Chùa Linh Phước", "Buổi sáng", "Chùa ghép mảnh sành sứ và kính kín tường, có tháp bảy tầng và điện Phật. Vào cửa miễn phí, cách trung tâm khoảng 6 km."),
  ("Dalat Wonderland", "Buổi sáng", "Khu vui chơi cạnh hồ Tuyền Lâm, có ATV, máng trượt và sở thú nhỏ. Đánh giá gần đây phàn nàn một số trò đóng hoặc cũ."),
  ("Đồi chè Cầu Đất", "Buổi sáng", "Đồi chè xanh cách trung tâm khoảng 15 km, nổi tiếng săn mây lúc bình minh. Giờ mở cửa theo Google Maps là 6:00–18:00, khác với bài Klook."),
  ("Mongo Land", "Buổi sáng", "Công viên theo phong cách Mông Cổ với lều yurt, cừu, lạc đà và máng trượt cầu vồng dài. Vé khoảng 140.000 VND gồm một đồ uống; xem lại bài Klook vì mô tả công viên chưa chính xác."),
  ("Đồi Mộng Mơ", "Buổi sáng", "Đồi vườn khoảng 12 ha với hoa và cây tạo hình. Vé khoảng 250.000 VND người lớn theo đánh giá; nên đi từ tháng 11 đến tháng 6."),
  ("Tiệm cà phê Túi Mơ To", "Chiều muộn", "Quán cà phê đồi có vườn cúc họa mi và xích đu, hợp ngắm hoàng hôn. Đồ uống được đánh giá tốt; cuối tuần đông.")])
T["en"] = _mk("Self-Guided Attractions in Da Lat: 29 Places, Hours and Directions | Van Phu", "Self-Guided Attractions in Da Lat",
 "29 self-guided attractions in Da Lat: waterfalls, tea hills, pagodas, night market and flower gardens — opening hours from Google Maps, reference ticket prices and directions for each stop.",
 "29 places visitors list in their Da Lat itineraries: waterfalls, tea hills, pagodas, flower gardens and the night market. Most are within 15 km of Xuan Huong Lake; Pongour, Samten Hills and ZooDoo are farther and fit better in a day of their own.",
 "Places (1–29)", "Best time to go",
 [("Dry season (about November–April)", "less rain, easier to see flowers and go farther"), ("Early morning", "tea hills, Dreamy Hill and Langbiang often have better clouds and mist"), ("Weekdays", "far fewer visitors than weekends"), ("Weekends & Tet", "Valley of Love, Fresh Garden and Langbiang are crowded and traffic builds up")],
 "Good to know",
 ["Ticket prices on the map are reference prices from recent visitor reviews — check at the gate before you go.",
  "Madame De Dalat is closed on Sundays; Domaine de Marie closes for lunch, 11:30–13:30.",
  "Reviews say Elephant Falls is sometimes temporarily closed and Tea Resort Prenn has incomplete facilities — ask before you travel far.",
  "Samten Hills, ZooDoo and Pongour are 25–35 km from the centre — use a 125cc motorbike or an electric scooter with a full battery."],
 [("Datanla Waterfall", "Morning", "Waterfall in pine forest on Prenn Pass; ride down the 2.4 km alpine coaster or walk. Reference entry 30,000–50,000 VND, rides extra."),
  ("Valley of Love", "Morning or afternoon", "Large park with flower gardens, a glass bridge, slides and luge carts. Recent reviews put the full-park ticket around 250,000 VND; allow at least 3 hours."),
  ("Samten Hills", "Morning", "Tibetan Buddhist complex in Don Duong with a large copper prayer wheel (per visitor reviews). About 27 km from the centre."),
  ("Flower Plateau (Cao nguyên Hoa)", "Morning", "Eco area on the Ta Nung hills with wooden houses in pine forest and flower gardens. The downhill go-kart track is the main draw."),
  ("Fresh Garden", "Morning", "Large flower garden in Van Thanh with a small zoo, fish ponds and a café. Entry includes a drink; buying online is often cheaper than at the gate."),
  ("ZooDoo", "Morning", "Zoo in pine forest at Lac Duong, about 25 km from the centre; guided tours last 1.5–2 hours. Daily visitor numbers are limited, so book at least a day ahead."),
  ("Langbiang Mountain", "Early morning", "Summit about 2,167 m; reach Radar Hill by jeep or shuttle truck, or hike through the forest. On cloudy days the view can be hidden."),
  ("Robin Hill and cable car", "Morning", "Cable car of about 2 km to Truc Lam Zen Monastery, roughly 10–15 minutes each way. Reference round-trip fare about 150,000 VND."),
  ("Madame De Dalat", "Morning", "Former villa of Tran Le Xuan, built in 1958, with a garden and museum. Reviews put entry around 150,000–180,000 VND; closed on Sundays."),
  ("Nui Voi Pine Forest", "All day", "Rare red pine forest with many old trees, a tiered waterfall, kayaking and go-karts. Go-kart about 250,000 VND according to reviews."),
  ("Tuyen Lam Lake", "Late afternoon", "Lake of about 320 ha, roughly 5 km from the centre; pedal boats and sunset views from the shore. Some reviews mention litter along the shore."),
  ("Delight Park Da Lat", "Evening", "Entertainment park with flower gardens, rides and a night light show. Reviews of the Au Lac show are mixed, so check the schedule first."),
  ("Sculpture Tunnel (Clay Tunnel)", "Morning", "Walkway of red clay sculptures showing local history and scenery. Reviews put entry around 120,000 VND per person; the 'Infinity' area by the lake is popular for photos."),
  ("Fairytale Land", "Morning", "Storybook garden with round Hobbit-style houses and the Vinh Tien wine cellar. Entry about 90,000 VND; wine tasting costs extra."),
  ("Domaine de Marie (Pink Church)", "Morning", "Pink church on Mai Anh Hill with a flower garden; free entry. Go early and do not block the path during Mass."),
  ("Pongour Waterfall", "All day", "Seven-tier waterfall over mossy rock, about 50 km from Da Lat; a golf cart down to the falls costs about 15,000 VND each way. Steps are slippery after rain."),
  ("Me Linh Coffee Garden", "Morning", "Coffee estate with a processing tour and a look at the civets that produce weasel coffee. Serves com lam and grilled meat."),
  ("Tea Resort Prenn", "Morning", "Resort beside Prenn Waterfall with outdoor activities. Recent reviews are mixed on service and facilities, so ask before buying tickets."),
  ("Elephant Falls (Thac Voi)", "Morning", "Big waterfall beside Linh An Pagoda, about 17 km from the centre. Sometimes closed for works; you can still see it from the pagoda."),
  ("Linh An Pagoda", "Morning", "Pagoda with a 71 m Lady Buddha statue and a large Maitreya Buddha. Free entry and free parking."),
  ("Da Lat Night Market", "Evening", "Night market on Nguyen Thi Minh Khai street, open from about 17:30 until late. Try grilled rice paper, hot soy milk and banh uot long ga. Ignore pushy sellers."),
  ("Van Thanh Flower Village", "Morning", "Flower and vegetable village at Van Thanh; entry about 100,000 VND per person according to reviews. Flowers look best in season, so check photos first."),
  ("Long Dinh Tea Museum", "Morning", "Tea museum in Tram Hanh with a production tour and tasting; tickets about 100,000–150,000 VND depending on the package, and some include a drink."),
  ("Linh Phuoc Pagoda", "Morning", "Pagoda decorated with broken porcelain and glass mosaics, with a seven-storey tower and many statues. Free entry, about 6 km from the centre."),
  ("Dalat Wonderland", "Morning", "Fun park beside Tuyen Lam Lake with ATVs, slides and a small zoo. Recent reviews say some rides are closed or old."),
  ("Cau Dat Tea Hill", "Morning", "Green tea hills about 15 km from the centre, popular for sunrise and clouds. Google Maps lists 6:00–18:00, which differs from the Klook article."),
  ("Mongo Land", "Morning", "Mongolian-themed park with yurts, sheep, camels and a long rainbow slide. Ticket about 140,000 VND including a drink. Note: the Klook article describes it as forest-themed; reviews show it is Mongolian-themed."),
  ("Dreamy Hill (Mong Mo Hill)", "Morning", "Garden hill of about 12 hectares with flowers and sculpted plants. Reviews put adult entry around 250,000 VND; best from November to June."),
  ("Tui Mo To Cafe", "Late afternoon", "Hillside café with daisy paths and swings, good for sunset. Drinks are well reviewed; weekends are busy.")])

for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"datanla": "Thác Datanla Đà Lạt", "valleylove": "Thung lũng Tình Yêu Đà Lạt", "samten": "Samten Hills Đơn Dương",
      "flowerplateau": "Cao nguyên Hoa Đà Lạt", "freshgarden": "Fresh Garden Đà Lạt", "zoodoo": "ZooDoo Lạc Dương",
      "langbiang": "Núi Langbiang Đà Lạt", "robin": "Đồi Robin cáp treo Đà Lạt", "madame": "Madame Đà Lạt Trần Lệ Xuân",
      "nuivoi": "Rừng thông Núi Voi Đà Lạt", "tuyenlam": "Hồ Tuyền Lâm Đà Lạt", "delight": "Delight Park Đà Lạt",
      "tunnel": "Đường hầm điêu khắc Đà Lạt", "fairytale": "Fairytale Land Đà Lạt", "domaine": "Nhà thờ Domaine de Marie Đà Lạt",
      "pongour": "Thác Pongour", "melinh": "Đồn điền cà phê Mê Linh Đà Lạt", "prenntea": "Tea Resort Prenn Đà Lạt",
      "voi": "Thác Voi Nam Ban", "linhan": "Chùa Linh Ẩn Đà Lạt", "nightmarket": "Chợ đêm Đà Lạt",
      "vanthanh": "Làng hoa Vạn Thành Đà Lạt", "longdinh": "Bảo tàng Trà Long Đỉnh", "linhphuoc": "Chùa Linh Phước Đà Lạt",
      "wonderland": "Dalat Wonderland", "cauddat": "Đồi chè Cầu Đất Đà Lạt", "mongoland": "Mongo Land Đà Lạt",
      "mongmo": "Đồi Mộng Mơ Đà Lạt", "tuimoto": "Túi Mơ To Đà Lạt"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
