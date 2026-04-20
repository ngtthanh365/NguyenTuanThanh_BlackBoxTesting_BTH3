def chu_vi_hcn(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Lỗi: Input phải là số"
    if a <= 0 or b <= 0:
        return "Lỗi: Kích thước phải > 0"
    return 2 * (a + b)


# test nhanh
print(chu_vi_hcn(5, 3))