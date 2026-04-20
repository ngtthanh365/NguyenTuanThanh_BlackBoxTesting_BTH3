def dien_tich_hcn(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Lỗi: Input phải là số"
    if a <= 0 or b <= 0:
        return "Lỗi: Kích thước phải > 0"
    return a * b


# test nhanh
print(dien_tich_hcn(5, 3))