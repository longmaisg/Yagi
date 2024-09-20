# Yagi
Data processing of Yagi's donations

There are several files here:
- get_yagi_data.py: scrawl data and save to CSV after each 50 pages
- plot_yagi.py: process data from CSV and over-write data in plot_yagi.html
- plot_yagi.html: show data dynamically + search box

NOTE: only some pages are scrawled and shown in the html.

All prompts using ChatGPT can be found here: https://chatgpt.com/share/66edd7db-186c-800a-868a-b3e2c4097351


# For Vietnamese

Data Science + Check var

Chào mọi người,

Trong bài viết này mình trình bày bài tập nhỏ áp dụng Data Science trong cuộc sống một cách nhẹ nhàng.

Hiện tại chủ đề về ChatGPT & prompt engineer đang hot trong cộng đồng machine learning, còn chủ đề Check var cũng đang hot. Vì vậy, mình thử kết hợp prompt engineer + check var như sau:

- Yêu cầu ChatGPT viết code để scrawl dữ liệu danh sách ủng hộ bão lũ (Yagi).
- Yêu cầu ChatGPT plot danh sách này.

Phần scrawl dữ liệu khá đơn giản. Tuy nhiên phần plot danh sách khá dài dòng:
- Đầu tiên, mình yêu cầu plot sao cho hiện lên thông tin mỗi node (mỗi lần chuyển khoản) khi di chuyển chuột. ChatGPT dùng plotly trong python
- Sau đó, mình yêu cầu thêm là phải có nút search. Plotly trong python không làm được điều này nên mình yêu cầu dùng html.
- Khi đó, ChatGPT dùng python để tạo ra file html và thêm vào code javascript.
- Kết quả không tốt lắm. Sau đó mình yêu cầu tạo ra 1 file html template.
- Sau đó mình yêu cầu process data trong python, và ghi thêm vào file html.

Mình không hài lòng lắm với kết quả. Tuy nhiên, rõ ràng mình đã không phải viết một dòng code nào. ChatGPT viết toàn bộ code!

Toàn bộ prompt mình dùng: https://chatgpt.com/share/66edd7db-186c-800a-868a-b3e2c4097351
Code github: https://github.com/longmaisg/Yagi/tree/main
Bài viết trên blog: https://louismaiblog.blogspot.com/2024/09/data-processing-of-yagis-donations.html

Trong hình là plot 100 trang sao kê đầu tiên. Ví dụ mình thấy “Fan ruot Tran Thanh va Louis Pham ung ho bao lu” 2000 đồng.
