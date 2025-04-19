def ㅆ씨발(*니엄마) :
    result = 0
    for num in 니엄마:
        result += num
    return result
hap = 0

hap = ㅆ씨발(1,2,3,4,5)
print(hap)

def ㅆ씨발2(**니엄마) :
    for k in 니엄마.keys():
        print(k, ":", 니엄마[k])
ㅆ씨발2(이름="김철수", 나이=20, 성별="남자")

def genfunc(num) :
    for i in range(0, num) :
        yield i
        print("제너레이터 진행 중")

for data in genfunc(5) :
    print(data)