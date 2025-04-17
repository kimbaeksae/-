number = input("세 자리 정수 입력: ")

def read_single_digit(n) :
    digit_kor = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    print(digit_kor[int(n)], end=' ')

def read_number(n) :
    num = str(n)
    for i in range(len(num)):
        read_single_digit(num[i])

if len(number) > 3 or not number.isdigit():
    print("세 자리 이하 정수가 아닙니다.")
else:
    read_number(number)
