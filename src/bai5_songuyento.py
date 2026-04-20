def la_so_nguyen_to(n):
    if not isinstance(n, int):
        return "Lỗi: Input phải là số nguyên"

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# test nhanh
print(la_so_nguyen_to(7))