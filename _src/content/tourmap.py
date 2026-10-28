"""Da Lat tourist map by motorbike route (/vi/ban-do-du-lich-da-lat/, /da-lat-tourist-map/) — vi + en.
Six loops that start and end at the Van Phu shop, built from places already on our maps (placeshub + attractmap):
coordinates, hours and the electric-scooter flag come from those modules. Distances are straight-line ("đường chim bay");
the by-road figure is an estimate (straight line x 1.3–1.5) and is labelled as one. Owner-approved electric range: 2 batteries,
about 50–60 km in total (changed 2026-10-28)."""
LANGS = ["vi", "en"]
SLUG = {"vi": "ban-do-du-lich-da-lat", "en": "da-lat-tourist-map"}
UPDATED = "2026-10-28"
EV_MAX = 45          # estimated road km an electric scooter loop may have (2 batteries ≈ 50–60 km, keep a margin)
ROAD = (1.3, 1.5)    # straight line → road estimate

# route id, colour, stops in riding order: (source, spot id) — source "hub" = placeshub.spots(), "am" = attractmap
ROUTES = [
    ("center", "#0f7a4f", [("hub", "market"), ("hub", "pink"), ("hub", "crazy"), ("hub", "palace"), ("hub", "station"), ("hub", "lake"), ("hub", "cathedral")]),
    ("south",  "#1f6fd1", [("hub", "datanla"), ("hub", "truclam"), ("hub", "tuyenlam"), ("hub", "clay")]),
    ("west",   "#8a4bd1", [("hub", "dusinh"), ("hub", "vanthanh"), ("am", "freshgarden"), ("am", "fairytale"), ("am", "flowerplateau")]),
    ("north",  "#c06a00", [("hub", "valley"), ("am", "mongmo"), ("hub", "phucduc"), ("hub", "langbiang")]),
    ("east",   "#c0392b", [("hub", "linhphuoc"), ("hub", "honbo"), ("hub", "caudat"), ("hub", "caudatsky")]),
    ("far",    "#5d6d7e", [("hub", "linhan"), ("hub", "voi"), ("hub", "pongour")]),
]

T = {
"vi": {
 "title": "Bản đồ du lịch Đà Lạt 2026: 6 tuyến xe máy, km từ tiệm, đi xe điện được không | Văn Phú",
 "h1": "Bản đồ du lịch Đà Lạt theo tuyến xe máy",
 "desc": "Bản đồ du lịch Đà Lạt chia 6 tuyến xe máy khép kín từ trung tâm: các điểm theo thứ tự, số km, thời gian, tuyến nào đi xe máy điện được, lịch trình 1–4 ngày và PDF bản đồ miễn phí.",
 "lead": "Bản đồ này dành cho người tự chạy xe máy. Mỗi tuyến là một vòng khép kín, đi và về tiệm Văn Phú (1/15/5 Thông Thiên Học), các điểm xếp theo thứ tự chạy để không phải quay đầu. Bấm vào tên tuyến để chỉ hiện tuyến đó trên bản đồ.",
 "toc": "Mục lục", "map_h": "Bản đồ 6 tuyến", "all": "Tất cả", "routes_h": "6 tuyến xe máy quanh Đà Lạt",
 "stops": "Các điểm", "time": "Thời gian", "loop": "Cả vòng", "straight": "km đường chim bay", "road": "đường thật ước khoảng {a}–{b} km",
 "bike": "Nên đi", "ev_ok": "Xe máy điện hoặc Honda Vision. Xe máy điện có 2 pin, tổng khoảng 50–60 km, đủ cho cả vòng",
 "ev_no": "Honda Air Blade 125cc. Tuyến dài hoặc nhiều dốc, không hợp xe máy điện",
 "dir": "Chỉ đường", "hours": "Giờ mở cửa", "open_gm": "Mở cả tuyến trên Google Maps",
 "km_note": "Khoảng cách tính theo đường chim bay từ tiệm; đường thật thường dài hơn 1,3–1,5 lần. Giờ mở cửa lấy từ Google Maps, nên kiểm tra lại trước khi đi.",
 "names": {
  "center": ("Tuyến 1 · Trung tâm Đà Lạt", "Nửa buổi đến 1 buổi", "Chợ, nhà thờ, biệt thự cổ và ga xe lửa đều trong bán kính khoảng 2,5 km. Gửi xe ở bãi có vé, đi bộ giữa các điểm gần nhau. Buổi tối quay lại chợ đêm."),
  "south":  ("Tuyến 2 · Phía Nam – đèo Prenn, hồ Tuyền Lâm", "1 buổi", "Thác, thiền viện trong rừng thông và hồ lớn nhất Đà Lạt. Đường có dốc nhưng ngắn; đi buổi sáng để trời mát, chiều về uống cà phê ven hồ."),
  "west":   ("Tuyến 3 · Phía Tây – làng hoa Vạn Thành, Tà Nung", "1 buổi", "Vườn hoa, làng hoa và các khu sinh thái trên đồi phía Tây. Đường lên Tà Nung quanh co, đi chậm và tránh đi khi trời mưa."),
  "north":  ("Tuyến 4 · Phía Bắc – Thung lũng Tình Yêu, Langbiang", "1 buổi đến cả ngày", "Thung lũng, đồi ngắm cảnh và núi Langbiang ở Lạc Dương. Lên đỉnh Radar bằng xe jeep hoặc đi bộ, không chạy xe máy lên."),
  "east":   ("Tuyến 5 · Phía Đông – Trại Mát, Cầu Đất", "Sáng sớm đến trưa", "Chùa Linh Phước, đồi săn mây và đồi chè Cầu Đất. Muốn ngắm bình minh thì xuất phát khoảng 4:30–5:00; tiệm mở cửa từ 4:30 sáng."),
  "far":    ("Tuyến 6 · Xa phía Nam – Nam Ban, thác Pongour", "Cả ngày", "Chùa Linh Ẩn, thác Voi và thác Pongour, tuyến dài nhất. Đi sớm, đổ xăng trước và về trước khi trời tối."),
 },
 "plan_h": "Lịch trình 1–4 ngày ghép từ các tuyến",
 "plans": [
  ("1 ngày", "Sáng Tuyến 2 (phía Nam), chiều Tuyến 1 (trung tâm), tối chợ đêm.", "day"),
  ("2 ngày 1 đêm", "Ngày 1 như lịch 1 ngày. Ngày 2: sáng sớm Tuyến 5 (bình minh Cầu Đất), chiều nghỉ hoặc dạo Tuyến 1.", "art:days2"),
  ("3 ngày", "Thêm 1 ngày: sáng Tuyến 4 (phía Bắc), chiều Tuyến 3 (phía Tây). Hai tuyến này nằm gần nhau, chạy liền được.", "art:days3"),
  ("4 ngày", "Dành nguyên ngày thứ 4 cho Tuyến 6 (Nam Ban, thác Pongour).", None),
 ],
 "avoid_h": "Không nên ghép",
 "avoid": [
  "Tuyến 5 (Cầu Đất, phía Đông) và Tuyến 6 (Pongour, phía Nam) trong cùng một ngày: hai hướng ngược nhau, đường rất dài.",
  "Tuyến 5 và Tuyến 3 (Tà Nung, phía Tây) trong cùng một buổi: phải băng qua cả thành phố.",
  "Đi các tuyến đèo dốc khi trời mưa to hoặc sương dày lúc tối muộn.",
 ],
 "faq_h": "Hỏi nhanh",
 "faq": [
  ("Có bản đồ du lịch Đà Lạt bản in (PDF) không?", "Có. Mỗi bản đồ chủ đề bên dưới (điểm chụp ảnh, thác, chùa, nhà thờ, săn mây, cà phê view…) đều có file PDF tải miễn phí để in hoặc lưu vào điện thoại."),
  ("Tuyến nào đi xe máy điện được?", "{ev_list}. Mỗi xe máy điện có 2 pin, tổng khoảng 50–60 km, đổi pin tại tiệm 20.000 VND. Các tuyến còn lại dài hoặc nhiều dốc, nên đi Honda Air Blade 125cc."),
  ("Tuyến nào xa nhất?", "{far_name}: cả vòng khoảng {far_km} km đường chim bay, đường thật còn dài hơn. Nên đi trọn một ngày."),
  ("Chỉ có 1 ngày ở Đà Lạt thì đi tuyến nào?", "Sáng chạy Tuyến 2 (thác Datanla, Thiền viện Trúc Lâm, hồ Tuyền Lâm), chiều dạo Tuyến 1 ở trung tâm và tối ra chợ đêm. Đường ngắn, đi xe máy điện được."),
  ("Thuê xe ở Văn Phú bao nhiêu tiền?", "150.000 VND/ngày cho mọi xe (Honda Vision, Air Blade, xe máy điện), kèm mũ bảo hiểm, không cọc tiền, chỉ giữ CCCD hoặc hộ chiếu. Thuê từ 2 ngày được giao xe miễn phí tới khách sạn trong trung tâm."),
 ],
 "themes_h": "Bản đồ chủ đề (có PDF in được)",
 "more_h": "Xem thêm",
 "more": [("hub", "35 địa điểm du lịch Đà Lạt chia theo hướng"), ("routes", "5 lộ trình xe máy quanh Đà Lạt"), ("day", "Đà Lạt 1 ngày tự túc bằng xe máy")],
 "cta_h": "Thuê xe chạy các tuyến này",
 "cta": "Văn Phú mở cửa từ 4:30 sáng mỗi ngày. Mọi xe 150.000 VND/ngày, có mũ bảo hiểm và giá đỡ điện thoại, xe xăng có sẵn 1 lít xăng. Chạy thử và quay video tình trạng xe trước khi nhận. Không uống rượu bia khi lái xe và chấp hành đúng luật giao thông.",
 "shop": "Tiệm Văn Phú – điểm xuất phát",
},
"en": {
 "title": "Da Lat Tourist Map 2026: 6 Motorbike Routes, Distances, Electric Scooter or Not | Van Phu",
 "h1": "Da Lat Tourist Map by Motorbike Route",
 "desc": "A Da Lat tourist map split into 6 motorbike loops from the centre: stops in riding order, distances, time needed, which routes work on an electric scooter, 1–4 day plans and free PDF maps.",
 "lead": "This map is made for riding Da Lat on your own. Each route is a loop that starts and ends at the Van Phu shop (1/15/5 Thong Thien Hoc), with stops in riding order so you never double back. Tap a route name to show only that route on the map.",
 "toc": "Contents", "map_h": "Map of the 6 routes", "all": "All", "routes_h": "6 motorbike routes around Da Lat",
 "stops": "Stops", "time": "Time", "loop": "Whole loop", "straight": "km in a straight line", "road": "by road roughly {a}–{b} km",
 "bike": "Best bike", "ev_ok": "Electric scooter or Honda Vision. An electric scooter has 2 batteries, about 50–60 km in total — enough for the loop",
 "ev_no": "Honda Air Blade 125cc. Long or hilly route, not suited to an electric scooter",
 "dir": "Directions", "hours": "Hours", "open_gm": "Open the whole route in Google Maps",
 "km_note": "Distances are straight-line from the shop; the road is usually 1.3–1.5 times longer. Opening hours are from Google Maps — check again before you go.",
 "names": {
  "center": ("Route 1 · Central Da Lat", "Half a morning to half a day", "The market, churches, old villas and the railway station all sit within about 2.5 km. Park at a guarded lot and walk between nearby sights; come back to the night market in the evening."),
  "south":  ("Route 2 · South – Prenn Pass and Tuyen Lam Lake", "Half a day", "A waterfall, a Zen monastery in the pines and Da Lat's biggest lake. Some climbs but short; go in the cool morning and finish with a lakeside coffee."),
  "west":   ("Route 3 · West – Van Thanh flower village and Ta Nung", "Half a day", "Flower gardens, the flower village and eco-parks on the western hills. The road up to Ta Nung winds a lot — ride slowly and skip it in heavy rain."),
  "north":  ("Route 4 · North – Valley of Love and Lang Biang", "Half to a full day", "A valley, viewpoint hills and Lang Biang Mountain in Lac Duong. Radar Peak is reached by jeep or on foot, not by motorbike."),
  "east":   ("Route 5 · East – Trai Mat and Cau Dat", "Dawn to noon", "Linh Phuoc Pagoda, cloud-hunting hills and the Cau Dat tea hills. For the sunrise leave around 4:30–5:00 — the shop opens at 4:30 am."),
  "far":    ("Route 6 · Far south – Nam Ban and Pongour Falls", "Full day", "Linh An Pagoda, Elephant Falls and Pongour Falls — the longest loop. Start early, fill up before you go and be back before dark."),
 },
 "plan_h": "1–4 day plans built from the routes",
 "plans": [
  ("1 day", "Morning: Route 2 (south). Afternoon: Route 1 (centre). Evening: night market.", "day"),
  ("2 days, 1 night", "Day 1 as above. Day 2: dawn on Route 5 (Cau Dat sunrise), relaxed afternoon in the centre.", "art:days2"),
  ("3 days", "Add a day: Route 4 (north) in the morning and Route 3 (west) in the afternoon — they are next to each other.", "art:days3"),
  ("4 days", "Keep the fourth day for Route 6 (Nam Ban, Pongour Falls).", None),
 ],
 "avoid_h": "Don't combine",
 "avoid": [
  "Route 5 (Cau Dat, east) and Route 6 (Pongour, south) on the same day — opposite directions and a very long ride.",
  "Route 5 and Route 3 (Ta Nung, west) in the same half day — you would cross the whole city.",
  "Hilly routes in heavy rain or thick fog late in the evening.",
 ],
 "faq_h": "Quick answers",
 "faq": [
  ("Is there a printable Da Lat tourist map (PDF)?", "Yes. Every theme map below (photo spots, waterfalls, pagodas, churches, cloud hunting, view cafés…) has a free PDF to print or save on your phone."),
  ("Which routes work on an electric scooter?", "{ev_list}. Each electric scooter has 2 batteries, about 50–60 km in total, with a battery swap at the shop for 20,000 VND. The other routes are long or hilly — take a Honda Air Blade 125cc."),
  ("Which route is the longest?", "{far_name}: the loop is about {far_km} km in a straight line and longer by road. Plan a full day."),
  ("I only have one day in Da Lat — which route?", "Ride Route 2 in the morning (Datanla Waterfall, Truc Lam Monastery, Tuyen Lam Lake), stroll Route 1 in the centre in the afternoon and end at the night market. Short distances, fine on an electric scooter."),
  ("How much is a rental at Van Phu?", "150,000 VND per day for every bike (Honda Vision, Air Blade, electric scooter), free helmet, no cash deposit — you leave your passport or ID card. Free delivery to hotels in central Da Lat for 2+ days."),
 ],
 "themes_h": "Theme maps (with printable PDF)",
 "more_h": "See also",
 "more": [("hub", "Places to visit in Da Lat, grouped by direction"), ("routes", "5 motorbike routes around Da Lat"), ("day", "Da Lat day trip by motorbike on your own")],
 "cta_h": "Rent a bike for these routes",
 "cta": "Van Phu opens at 4:30 am every day. Every bike is 150,000 VND per day with a free helmet and phone holder; gas scooters come with 1 liter of fuel. Test ride and a video of the bike's condition before you go. Vietnam drives on the right; no alcohol when riding, and follow Vietnamese traffic law.",
 "shop": "Van Phu shop – start and finish",
},
}
