sel = int(input("입력할 진수를 입력하세요(2/8/10/16): "))
num = input("값을 입력하세요: ")

if sel == 2:
    num10 = int(num, 2)
if sel == 8:
    num10 = int(num, 8)
if sel == 10:
    num10 = int(num, 10)
if sel == 16:
    num10 = int(num, 16)

print("2진수 ==> ", bin(num10))
print("8진수 ==> ", oct(num10))
print("10진수 ==> ", num10)
print("16진수 ==> ", hex(num10))
