pi = 3.14
print("이 코드는 원의 반지름을 입력받아 원의 둘레와 넓이를 구하는 코드입니다.\n")
print("반지름을 입력해주세요")
input_a = float(input("반지름 입력> "))
print("원의 둘레: ",input_a * 2 * pi)
print("원의 넓이: ",(input_a ** 2) * pi)