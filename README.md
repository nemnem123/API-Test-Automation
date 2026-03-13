Helper: luôn dọn DynamoDB trước khi test
Test POST /echo (chỉ test tạo dữ liệu)
Test GET /echo sau khi đã POST
Test DELETE /echo
    - Test độc lập
    - Không phụ thuộc thứ tự test khác
    - Tự chuẩn bị dữ liệu trước khi xoá
Test dữ liệu đầu vào sai kiểu:
    name đáng lẽ là string nhưng gửi number

