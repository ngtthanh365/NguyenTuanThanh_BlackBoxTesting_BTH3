def so_ngay_trong_thang(thang, nam):
    if not isinstance(thang, int) or not isinstance(nam, int):
        return "Lỗi: Input phải là số nguyên"

    if thang < 1 or thang > 12:
        return "Lỗi: Tháng không hợp lệ"

    if nam <= 0:
        return "Lỗi: Năm không hợp lệ"

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        # tháng 2
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        return 28


# test nhanh
print(so_ngay_trong_thang(2, 2024))