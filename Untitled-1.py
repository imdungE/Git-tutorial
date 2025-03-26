print("Hello, World!")
print(10 == 12)
print("가방" < "하마")
a = 1
is_under_3 = a < 3
print("is_under_3:", is_under_3)
print("not is_under_3:", not is_under_3)

number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다.")
if number < 0:
    print("음수입니다.")
if number == 0:
    print("0입니다.")


import datetime


now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")

x = 10
y = 2

if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)

import turtle

swidth, sheight = 500, 500

turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0,-sheight/2)
turtle.pendown()
turtle.speed(10)

for radius in range(1, 250):
    if radius % 6 == 0:
        turtle.pencolor('red')
    elif radius % 5 == 0:
        turtle.pencolor('orange')
    elif radius % 4 == 0:
        turtle.pencolor('yellow')
    elif radius % 3 == 0:
        turtle.pencolor('green')
    elif radius % 2 == 0:
        turtle.pencolor('blue')
    elif radius % 1 == 0:
        turtle.pencolor('navyblue')
    else:
        turtle.pencolor('purple')
    

    turtle.circle(radius)
turtle.done()
#fdkmkfd

