# NguyenTuanThanh_BlackBoxTesting_BTH3
# 🧪 BÀI THỰC HÀNH 03

## KIỂM THỬ HỘP ĐEN (BLACK BOX TESTING)

---

## 📌 Giới thiệu

Bài thực hành này nhằm mục đích áp dụng các kỹ thuật **kiểm thử hộp đen (Black Box Testing)** để kiểm tra tính đúng đắn của các chương trình xử lý dữ liệu đầu vào và đầu ra.

Khác với kiểm thử hộp trắng, phương pháp này không quan tâm đến cấu trúc bên trong của chương trình mà tập trung vào việc kiểm tra chức năng thông qua các tập dữ liệu kiểm thử.

---

## 🎯 Nội dung thực hiện

Bài thực hành gồm 8 bài toán:

1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày trong tháng
5. Kiểm tra số nguyên tố
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của hai số
8. Tính tổng S = 1! + 2! + ... + n!

---

## 🧠 Phương pháp kiểm thử áp dụng

### 1. Phân lớp tương đương (Equivalence Partitioning)

Dữ liệu đầu vào được chia thành các nhóm:

* **Lớp hợp lệ (Valid Class):**

  * Dữ liệu đúng định dạng và nằm trong phạm vi cho phép

* **Lớp không hợp lệ (Invalid Class):**

  * Dữ liệu âm, ngoài phạm vi
  * Dữ liệu sai kiểu (string, ký tự...)

👉 Mục tiêu: giảm số lượng test nhưng vẫn đảm bảo độ bao phủ.

---

### 2. Phân tích giá trị biên (Boundary Value Analysis)

Các giá trị đặc biệt được lựa chọn để kiểm thử:

* 0, 1, -1
* Giá trị nhỏ nhất / lớn nhất
* Các điểm chuyển trạng thái

👉 Đây là nơi lỗi thường xảy ra nên cần kiểm tra kỹ.

---

## 🧪 Thiết kế kiểm thử

### ✔ Test hợp lệ

* Kiểm tra với dữ liệu đúng
* Đảm bảo chương trình trả kết quả chính xác

### ✔ Test không hợp lệ

* Input sai kiểu
* Input ngoài phạm vi
* Input âm hoặc không hợp lệ

### ✔ Test giá trị biên

* Kiểm tra tại các điểm giới hạn
* Xác định khả năng xử lý edge case

---

## 📂 Cấu trúc thư mục

```
.
├── src/                # Mã nguồn chương trình
├── testcases/          # Danh sách test case
│   ├── valid_cases.md
│   └── invalid_cases.md
├── results/            # Kết quả kiểm thử
│   └── test_results.txt
└── README.md
```

---

## ⚙️ Quy trình thực hiện

1. Xây dựng chương trình cho từng bài toán
2. Xác định Input / Output
3. Áp dụng:

   * Phân lớp tương đương
   * Giá trị biên
4. Thiết kế test case
5. Thực thi kiểm thử
6. Ghi nhận kết quả

---

## 🔧 Quản lý bằng GitHub

* Sử dụng **Issue** để quản lý test case:

  * Issue #1: Test hợp lệ
  * Issue #2: Test lỗi + biên

* Sử dụng **Commit** để:

  * cập nhật code
  * thêm test case
  * ghi nhận kết quả

👉 Issue được đóng thông qua commit (close #ID) để đảm bảo quy trình phát triển.

---

## 📊 Kết quả kiểm thử

* Tất cả test case hợp lệ: PASS
* Tất cả test case không hợp lệ: PASS
* Các giá trị biên được xử lý chính xác

👉 Chương trình hoạt động đúng theo yêu cầu.

---

## ✅ Kết luận

Bài thực hành đã áp dụng thành công các kỹ thuật kiểm thử hộp đen:

* Phân lớp tương đương giúp giảm số lượng test
* Giá trị biên giúp phát hiện lỗi tiềm ẩn

Kết quả cho thấy hệ thống xử lý đúng trong cả trường hợp bình thường và ngoại lệ.

---

## 👨‍💻 Tác giả

* Họ tên: Nguyễn Tuấn Thành
* Môn học: Đánh giá và kiểm định chất lượng phần mềm

---
