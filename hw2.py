
def get_interger(prompt):
    return int(input(prompt))


def exchange(money):
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        num = money // coin
        money %= coin
        print(coin,"원 동전의 개수: ", num)
    
bill = get_interger("동전으로 교환하고자 하는 금액은? ")
exchange(bill)



