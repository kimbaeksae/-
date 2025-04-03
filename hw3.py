def get_fixed_price(discount_price, discount_rate):
    return int(discount_price / (1 - discount_rate / 100))

def main():
    dis_rate = int(input("할인율은? "))
    A_dis = int(input("A 상품의 할인된 가격은? "))
    B_dis = int(input("B 상품의 할인된 가격은? "))

    A_fix = get_fixed_price(A_dis, dis_rate)
    B_fix = get_fixed_price(B_dis, dis_rate)

    print("A 상품의 정가는", A_fix, "원")
    print("B 상품의 정가는", B_fix, "원")

main()
