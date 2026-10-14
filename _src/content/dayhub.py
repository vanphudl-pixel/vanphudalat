"""Parent page 'Da Lat day trip on your own by motorbike' — lists the self-drive route maps (routenew, routecheckin) as cards,
links the related itineraries already on the site, FAQ.
vi + en (same languages as the route maps)."""
LANGS = ["vi", "en"]
SLUG = {"vi": "da-lat-1-ngay-tu-tuc", "en": "da-lat-day-trip-by-motorbike"}
UPDATED = "2026-10-15"
T = {
"vi": {
 "title": "Đà Lạt 1 ngày tự túc bằng xe máy: lộ trình như tour, tự chọn giờ | Văn Phú",
 "h1": "Đà Lạt 1 ngày tự túc bằng xe máy",
 "desc": "Lộ trình Đà Lạt 1 ngày tự túc bằng xe máy, đi đúng các điểm như tour ghép: thứ tự đi, giờ gợi ý, số km, xe nào phù hợp và bản đồ PDF miễn phí. Thuê xe 150.000 VND/ngày.",
 "lead": "Thay vì đi tour ghép, bạn tự chạy xe máy theo đúng lộ trình các tour 1 ngày phổ biến — tự chọn giờ xuất phát, ở lại lâu ở điểm mình thích, bỏ qua điểm không hợp. Mỗi lộ trình có bản đồ đánh số theo thứ tự, giờ gợi ý, số km và gợi ý nên đi xe nào.",
 "routes_h": "Chọn lộ trình",
 "stops": "Các điểm", "km": "Cả vòng khoảng {km} km đường chim bay (tiệm → các điểm → tiệm)", "open": "Xem bản đồ lộ trình", "pdf": "Tải PDF",
 "verdict": {
  "routenew": "Hợp gia đình có trẻ em và người thích khu vui chơi. Đường dài, nhiều dốc — nên đi Honda Air Blade 125cc.",
  "routecheckin": "Hợp người thích chụp ảnh. Quãng đường ngắn hơn — đi xe máy điện được nếu ghé tiệm đổi pin buổi trưa (20.000 VND), hoặc đi Air Blade cho thoải mái.",
 },
 "more_h": "Lộ trình 1 ngày khác trên trang",
 "more": [("art:caudat", "Săn mây, ngắm bình minh đồi chè Cầu Đất"), ("art:waterfalls", "Các thác quanh Đà Lạt: Datanla, Prenn, thác Voi, Pongour"), ("routes", "5 cung đường xe máy quanh Đà Lạt"), ("art:days3", "Lịch trình Đà Lạt 3 ngày"), ("hub", "Tất cả địa điểm du lịch Đà Lạt theo hướng")],
 "faq_h": "Câu hỏi thường gặp",
 "faq": [
  ("Đà Lạt 1 ngày tự túc bằng xe máy có khó không?", "Không khó nếu bạn đã quen chạy xe tay ga: đi theo Google Maps, chạy chậm ở đường đèo và khúc cua, đội mũ bảo hiểm và tuân thủ luật giao thông. Nên xuất phát sớm, nhất là mùa mưa vì mưa thường đến buổi chiều."),
  ("Thuê xe máy đi 1 ngày bao nhiêu tiền?", "150.000 VND/ngày cho mọi xe — Honda Vision, Honda Air Blade 125cc hoặc xe máy điện — gồm mũ bảo hiểm và giá đỡ điện thoại. Không cọc tiền mặt: bạn để lại hộ chiếu hoặc CCCD."),
  ("Nên chọn lộ trình nào?", "Thích chụp ảnh và muốn đi gọn thì chọn lộ trình check-in điểm hot; đi cùng trẻ em hoặc thích khu vui chơi thì chọn lộ trình điểm mới 2026."),
  ("Đi xe máy điện được lộ trình nào?", "Lộ trình check-in đi được nếu ghé tiệm đổi pin buổi trưa (một pin khoảng 35–40 km, đổi pin 20.000 VND). Lộ trình điểm mới dài và nhiều dốc — nên đi Honda Air Blade 125cc."),
  ("Có cần đặt xe trước không?", "Nên nhắn trước qua WhatsApp, Zalo hoặc WeChat để giữ xe. Thuê từ 2 ngày, tiệm giao xe miễn phí tới khách sạn ở trung tâm."),
 ],
},
"en": {
 "title": "Da Lat Day Trip by Motorbike: Tour Routes on Your Own | Van Phu",
 "h1": "Da Lat Day Trip on Your Own by Motorbike",
 "desc": "Self-guided Da Lat day trips by motorbike that follow the popular group tours: stop order, suggested times, distances, which bike to take and free PDF maps. Bike rental 150,000 VND per day.",
 "lead": "Instead of a group tour, ride the same day-tour routes on your own motorbike — start when you like, stay longer where you like, skip what you don't. Each route has a numbered map in riding order, suggested times, distances and which bike to take.",
 "routes_h": "Choose a route",
 "stops": "Stops", "km": "Whole loop about {km} km in a straight line (shop → stops → shop)", "open": "Open the route map", "pdf": "Download PDF",
 "verdict": {
  "routenew": "Good for families with kids and theme-park fans. Long and hilly — take a Honda Air Blade 125cc.",
  "routecheckin": "Good for photo lovers. Shorter — fine on an electric scooter with a battery swap at our shop at lunch (20,000 VND), or take an Air Blade for comfort.",
 },
 "more_h": "More day trips on this site",
 "more": [("art:caudat", "Cloud hunting and sunrise at the Cau Dat tea hills"), ("art:waterfalls", "Waterfalls near Da Lat: Datanla, Prenn, Elephant Falls, Pongour"), ("routes", "5 motorbike routes around Da Lat"), ("art:days3", "Da Lat in 3 days"), ("hub", "All places to visit in Da Lat by direction")],
 "faq_h": "Frequently asked questions",
 "faq": [
  ("Is a self-guided Da Lat day trip by motorbike hard?", "Not if you are used to an automatic scooter: follow Google Maps, ride slowly on passes and bends, wear a helmet and follow the traffic rules. Start early, especially in the rainy season, when rain usually comes in the afternoon."),
  ("How much does a bike cost for one day?", "150,000 VND per day for any bike — Honda Vision, Honda Air Blade 125cc or an electric scooter — with a helmet and a phone holder. No cash deposit: you leave your passport or ID card."),
  ("Which route should I choose?", "Love photos and want a compact day: the hot check-in route. With kids or keen on theme parks: the new attractions 2026 route."),
  ("Which route works on an electric scooter?", "The check-in route, with a battery swap at our shop at lunch (one battery is about 35–40 km, a swap costs 20,000 VND). The new attractions route is long and hilly — take a Honda Air Blade 125cc."),
  ("Do I need to book the bike in advance?", "It's best to message us on WhatsApp, Zalo or WeChat to hold a bike. For 2 days or more we deliver free to hotels in the centre."),
 ],
},
}
