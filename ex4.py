"""
    Phần 1: Phân tích Input / Output
    1. Input của bài toán

    Input là danh sách sách có sẵn:

    books = [
        {"id": 1, "title": "Python Basic", "quantity": 12},
        {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
        {"id": 3, "title": "Clean Code", "quantity": 5},
        {"id": 4, "title": "Database Design", "quantity": 0},
        {"id": 5, "title": "Web API Design", "quantity": 20}
    ]

    Mỗi sách gồm:

    id: mã sách
    title: tên sách
    quantity: số lượng tồn kho
    2. Output mong muốn

    API trả về danh sách sách sắp hết hàng:

    {
        "message": "Danh sách sách sắp hết hàng",
        "data": [
            {
                "id": 2,
                "title": "FastAPI Beginner",
                "quantity": 3
            }
        ]
    }

    Nếu không có sách:

    {
        "message": "Không có sách nào sắp hết hàng",
        "data": []
    }
    3. Điều kiện xác định sách sắp hết hàng

    Một sách được xem là sắp hết hàng khi:

    quantity <= 5

    Ngoài ra:

    Không có quantity → bỏ qua
    quantity < 0 → dữ liệu sai, bỏ qua
    Phần 2: Đề xuất giải pháp lọc dữ liệu
    Giải pháp 1: Dùng vòng lặp for

    Ví dụ:

    low_stock = []

    for book in books:
        if "quantity" not in book:
            continue

        if book["quantity"] < 0:
            continue

        if book["quantity"] <= 5:
            low_stock.append(book)
    Ưu điểm:
    Dễ hiểu
    Dễ debug
    Xử lý điều kiện phức tạp tốt
    Nhược điểm:
    Code dài hơn
    Nhiều dòng hơn
    Giải pháp 2: Dùng List Comprehension

    Ví dụ:

    low_stock = [
        book for book in books
        if "quantity" in book
        and book["quantity"] >= 0
        and book["quantity"] <= 5
    ]
    Ưu điểm:
    Code ngắn
    Viết nhanh
    Phù hợp lọc dữ liệu đơn giản
    Nhược điểm:
    Khó đọc khi điều kiện nhiều
    Khó debug
"""

from fastapi import FastAPI

app = FastAPI()


books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20},

    # dữ liệu lỗi để test
    {"id": 6, "title": "Java Basic"},
    {"id": 7, "title": "Spring Boot", "quantity": -2}
]


@app.get("/books/low-stock")
def get_low_stock_books():

    low_stock_books = []

    for book in books:

        # bỏ qua sách thiếu quantity
        if "quantity" not in book:
            continue

        # bỏ qua quantity âm
        if book["quantity"] < 0:
            continue

        # lấy sách sắp hết hàng
        if book["quantity"] <= 5:
            low_stock_books.append(book)


    if len(low_stock_books) == 0:
        return {
            "message": "Không có sách nào sắp hết hàng",
            "data": []
        }


    return {
        "message": "Danh sách sách sắp hết hàng",
        "data": low_stock_books
    }