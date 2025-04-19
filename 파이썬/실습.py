a = int(input("입력> "))
for i  in range(a):
    for j in range(i+1):
        print("*", end="")
    print()

니엄마 = {'사과': 1, '배': 2, '귤': 3}
for a, b in 니엄마.items():
    print("{} {}".format(a, b))