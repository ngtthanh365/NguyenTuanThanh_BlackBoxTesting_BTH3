def giai_thua(n):
    if n < 0:
        return "Lỗi"
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def tong_giai_thua(n):
    if not isinstance(n, int):
        return "Lỗi: Input phải là số nguyên"

    if n < 1:
        return "Lỗi: n phải >= 1"

    s = 0
    for i in range(1, n + 1):
        s += giai_thua(i)

    return s


# test nhanh
print(tong_giai_thua(4))