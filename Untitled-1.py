def para_func (*para) : 
    result = 0
    for num in para : 
        result = result + num
    
    return result

def dic_func (**para) :
    for k in para.keys() :
        print("%s --> %d명입니다." %(k,para[k]))
    print(para)

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)

hap = 0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap)

import random

def getNumber() :
    return random.randrange(1, 46)

lotto = []
num = 0

print("** 로또 추첨을 시작합니다. **\n")

while True :
    num = getNumber()
    if lotto.count(num) == 0 :
        lotto.append(num)
        if len(lotto) >= 6 : 
            break

print("추첨된 로또 번호 ==> ", end = '')
lotto.sort()
for i in range(0,6) :
    print("%d " %lotto[i], end = '')
