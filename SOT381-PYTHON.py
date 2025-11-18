# Bai 1
def bai1():
    num = int(input("Nhập số cần kiểm tra: "))
    if num % 2 == 0 and num > 10 and num % 3 == 0:
        print("Số thỏa mãn tất cả điều kiện.")
    else:
        print("Số KHÔNG thỏa mãn đủ điều kiện.")

# Bai 2
def bai2():
    a = 15 - 3 * 4 + 2 ** 3
    b = (15 - 3) * (4 + 2) ** 3
    c = 10 % 3 + 5 // 2 * 4
    print("a =", a)
    print("b =", b)
    print("c =", c)

# Bai 3
def bai3():
    total = 100
    total -= 25
    total *= 2
    total /= 5
    total += 10
    print("Kết quả cuối cùng:", total)

# Bai 4
def bai4():
    text = input("Nhập chuỗi cần kiểm tra: ")
    if "Python" in text and "Programming" in text:
        print("Chuỗi chứa cả 'Python' và 'Programming'.")
    else:
        print("Chuỗi KHÔNG chứa đủ hai từ.")
