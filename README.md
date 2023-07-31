# Attendance Checker - Hệ thống điểm danh tự động bằng nhận diện khuôn mặt

## Xin chào các bạn!
Đây là dự án "Attendance Checker" do mình phát triển nhằm giải quyết vấn đề điểm danh trong trường học. Ai trong chúng ta cũng biết rằng việc điểm danh thủ công có thể mất thời gian và gây ra nhiều sai sót. Vì vậy, mình đã quyết định xây dựng một hệ thống điểm danh tự động, sử dụng công nghệ nhận diện khuôn mặt, để giúp chúng ta tiết kiệm thời gian và làm cho quá trình điểm danh trở nên hiệu quả hơn.

## Yêu cầu cài đặt
Trước khi chạy dự án, bạn cần cài đặt một số thư viện cần thiết. Dưới đây là hướng dẫn cài đặt các thư viện này:

### 1. OpenCV (cv2):
OpenCV là thư viện xử lý ảnh và video rất mạnh mẽ trong Python. Bạn có thể cài đặt OpenCV bằng lệnh pip như sau:
pip install opencv-python

### 2. face_recognition:
face_recognition là thư viện sử dụng để nhận diện khuôn mặt trong hình ảnh. Bạn có thể cài đặt face_recognition bằng lệnh pip như sau:
pip install face-recognition

### 3. numpy (np):
numpy là thư viện để làm việc với mảng và các thao tác số học. Bạn có thể cài đặt numpy bằng lệnh pip như sau:
pip install numpy

### 4. pandas (pd):
pandas là thư viện để làm việc với bảng dữ liệu (CSV). Bạn có thể cài đặt pandas bằng lệnh pip như sau:
pip install pandas

### 5. mtcnn:
mtcnn là thư viện nhận diện khuôn mặt trong hình ảnh. Bạn có thể cài đặt mtcnn bằng lệnh pip như sau:
pip install mtcnn

### 6. tkinter:
tkinter là thư viện để xây dựng giao diện người dùng đơn giản và thân thiện. Bạn có thể cài đặt tkinter bằng lệnh pip như sau:
pip install tk

### 7. PIL:
PIL (Python Imaging Library) là thư viện để làm việc với hình ảnh. Bạn có thể cài đặt PIL bằng lệnh pip như sau:
pip install pillow


### 8. winsound:
winsound là thư viện sử dụng để phát âm thanh thông báo khi điểm danh thành công. Bạn không cần phải cài đặt thư viện này, vì nó là một thư viện được tích hợp sẵn trong Python.


## Hướng dẫn sử dụng
1. Clone dự án từ GitHub về máy tính của bạn.
2. Cài đặt các thư viện cần thiết như đã hướng dẫn ở phần trên.
3. Chuẩn bị dữ liệu khuôn mặt cho việc nhận diện. Lưu hình ảnh của các bạn sinh viên trong thư mục "Pe".
4. Mở file "main.py" và chạy dự án.
5. Cửa sổ camera sẽ hiển thị để nhận diện khuôn mặt và điểm danh tự động.

## Cảm ơn vì đã quan tâm đến dự án của mình!
Tôi hy vọng rằng dự án "Attendance Checker" sẽ giúp ích cho cộng đồng sinh viên và học sinh. Hãy thoải mái tham khảo và sử dụng dự án này để cải thiện quy trình điểm danh trong lớp học. Nếu bạn có bất kỳ ý kiến đóng góp hoặc câu hỏi nào, hãy liên hệ với mình. Chúc các bạn học tập vui vẻ và thành công!
