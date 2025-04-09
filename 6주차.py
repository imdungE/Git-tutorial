def get_shop_name():
    return "커피 장인"
def get_brench_name():
    return "여의도 본점"
def print_names():
    print(get_shop_name())
    print(get_brench_name())

print_names()

order_detail = []
def make_order(name, qty):
    order_detail.append({"이름": name, "수량": qty})

print(order_detail)
make_order("아메리카노", 2)
make_order("플랫 화이트", 1)
print(order_detail)


def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if button == 1:
        print("#3. (자동으로) 보통커피를 탄다.")
    elif button == 2:
        print("#3. (자동으로) 설탕커피를 탄다.")
    elif button == 3:
        print("#3. (자동으로) 블랙커피를 탄다.")
    else:
        print("#3. (자동으로) 아무커피나 탄다.\n")

    print("#4. (자동으로) 물을 붓는다.")
    print("#5. (자동으로) 스푼으로 젓는다.")
    print()

coffee = int(input("커피 종류를 선택하세요. (1: 보통, 2: 설탕, 3: 블랙)"))
coffee_machine(coffee)
print("커피가 준비되었습니다.")

def cal(v1,v2,op):
    result = 0
    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        result = v1 / v2
    return result

res = 0
var1, var2, oper = 0, 1, ""

oper = input("계산을 입력하세요(+, -, *, /) : ")
var1 = int(input("첫번째 숫자 : "))
var2 = int(input("두번째 숫자 : "))
res = cal(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))

def func1():
    a = 10
    print("func1()에서 a값 %d" %a)
def func2():
    print("func2()에서 a값 %d" %a)

a = 20
func1()
func2()