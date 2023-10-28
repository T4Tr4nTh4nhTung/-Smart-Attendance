# Hệ thống Điểm Danh Tự Động Sử Dụng Nhận Diện Khuôn Mặt

Dự án này là một Hệ thống Điểm Danh Tự Động sử dụng công nghệ nhận diện khuôn mặt, được thực hiện bằng Python và một số thư viện bao gồm OpenCV, face_recognition, Mediapipe, và nhiều thư viện khác. Dự án giúp đơn giản hóa quy trình điểm danh bằng việc sử dụng công nghệ nhận diện khuôn mặt để tự động đánh dấu sự hiện diện của sinh viên.

## Mục Lục
- [Tính Năng](#tính-năng)
- [Cài Đặt](#cài-đặt)
- [Sử Dụng](#sử-dụng)
- [Thư Viện Đã Sử Dụng](#thư-viện-đã-sử-dụng)
- [Cách Hoạt Động](#cách-hoạt-động)
- [Đóng Góp](#đóng-góp)
- [Giấy Phép](#giấy-phép)

## Tính Năng
- Tự động nhận diện và điểm danh dựa trên nhận diện khuôn mặt.
- Cung cấp giao diện đồ họa (GUI) để dễ dàng tương tác.
- Cho phép xóa nội dung tệp CSV điểm danh và thoát ứng dụng qua menu tệp.

## Cài Đặt
Để chạy dự án này trên máy tính của bạn, hãy tuân theo các bước cài đặt sau:

1. Sao Chép Dự Án:
git clone [[https://github.com/your/repo.git](https://github.com/T4Tr4nTh4nhTung/-Smart-Attendance/tree/Mediapipe-version)](https://github.com/T4Tr4nTh4nhTung/-Smart-Attendance.git)

2. Cài Đặt Thư Viện Cần Thiết:
Bạn cần cài đặt một số thư viện Python. Sử dụng các lệnh sau để cài đặt chúng:
pip install opencv-python
pip install face-recognition
pip install numpy
pip install pandas
pip install mediapipe
pip install pillow

Lưu ý: Thư viện winsound được tích hợp sẵn với Python, không cần cài đặt thêm.

## Sử Dụng
### Chuẩn Bị:
Chuẩn bị một thư mục chứa hình ảnh của những người mà bạn muốn theo dõi điểm danh. Hình ảnh nên được đặt trong một thư mục có tên là 'Pe' trong thư mục dự án. Bạn cũng có thể tổ chức hình ảnh theo tên lớp, ví dụ: 'Pe/Lớp1/SinhVien1.jpg', để tạo sự sắp xếp.

### Chạy Ứng Dụng:
Chạy tệp main.py. Điều này sẽ mở giao diện đồ họa cho việc điểm danh.

### Nhận Diện Khuôn Mặt:
Ứng dụng sử dụng nhận diện khuôn mặt để phát hiện và so sánh khuôn mặt với hình ảnh đã chuẩn bị.

### Đánh Dấu Điểm Danh:
Khi một khuôn mặt được nhận diện, hệ thống sẽ đánh dấu điểm danh bằng cách ghi tên, lớp, thời gian và ngày vào một tệp CSV.

### Xem Bản Ghi Điểm Danh:
Các bản ghi điểm danh được hiển thị trong giao diện GUI trong một cây thư mục (Treeview).

### Xóa Tệp CSV:
Bạn có thể xóa dữ liệu điểm danh bằng cách chọn "Xóa CSV" trong menu tệp.

### Thoát Ứng Dụng:
Bạn có thể thoát ứng dụng bằng cách chọn "Thoát" từ menu tệp.

## Thư Viện Đã Sử Dụng
Dự án sử dụng các thư viện sau:
- OpenCV (cv2): Cho xử lý hình ảnh và video.
- face_recognition: Cho nhận diện và nhận diện khuôn mặt.
- numpy (np): Cho các thao tác số học và xử lý mảng.
- pandas (pd): Cho làm việc với bảng dữ liệu (CSV).
- mediapipe: Cho nhận diện khuôn mặt sử dụng thư viện MediaPipe.
- PIL (Python Imaging Library): Cho xử lý và hiển thị hình ảnh.
- tkinter: Cho việc tạo giao diện đồ họa người dùng (GUI).
- winsound: Cho phát thông báo âm thanh.
- threading: Cho hỗ trợ đa luồng.

## Cách Hoạt Động
Ứng dụng chụp video từ camera máy tính và liên tục xử lý các khung hình. Khi phát hiện một khuôn mặt bằng MediaPipe, nó so sánh khuôn mặt đã phát hiện với hình ảnh đã chuẩn bị. Nếu có sự khớp, điểm danh được đánh dấu cho người tương ứng. Các bản ghi điểm danh được lưu trữ trong tệp CSV.

## Đóng Góp
Chúng tôi rất hoan nghênh mọi sự đóng góp vào dự án này. Nếu bạn muốn đóng góp hoặc báo cáo lỗi, vui lòng tạo một Issue hoặc Pull Request trên GitHub của chúng tôi.

## Giấy Phép
Dự án này được phân phối dưới giấy phép [Tên Giấy Phép]. Xem [Tệp Giấy Phép](LICENSE.md) để biết thêm chi tiết.

