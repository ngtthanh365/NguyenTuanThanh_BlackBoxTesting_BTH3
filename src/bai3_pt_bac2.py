import math

def giai_pt_bac2(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Lỗi: Input phải là số"

    if a == 0:
        # phương trình bậc 1
        if b == 0:
            if c == 0:
                return "Vô số nghiệm"
            else:
                return "Vô nghiệm"
        return -c / b

    delta = b*b - 4*a*c

    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)


# test nhanh
print(giai_pt_bac2(1, -3, 2))