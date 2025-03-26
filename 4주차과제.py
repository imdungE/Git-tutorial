number = input("1. 입력한 수식 계산 2. 두 수 사이의 합> ")
number = int(number)

if number == 1:
    a = input("수식을 입력하세요> ")
    print("%s 결과는 %d입니다" % (a, eval(a)))
elif number == 2:
    a = input("첫 번째 수를 입력하세요> ")
    b = input("두 번째 수를 입력하세요> ")
    a = int(a)
    b = int(b)
    print("%d+...+%d는 %d입니다" % (a, b, sum(range(a, b+1))))
