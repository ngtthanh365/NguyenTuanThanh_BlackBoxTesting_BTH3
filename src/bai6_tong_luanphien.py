def tong_luan_phien(n):
    if not isinstance(n, int):
        return "Lỗi: Input phải là số nguyên"

    if n <= 0:
        return "Lỗi: n phải > 0"

    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s -= i
        else:
            s += i
    return s


# test nhanh
print(tong_luan_phien(5))