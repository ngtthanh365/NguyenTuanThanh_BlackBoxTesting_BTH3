def ucln(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Lỗi: Input phải là số nguyên"

    if a == 0 and b == 0:
        return "Lỗi: Không xác định"

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


# test nhanh
print(ucln(12, 18))