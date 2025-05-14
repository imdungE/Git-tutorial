outFp = None
outStr = ""

outFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "w", encoding = "utf-8")

while True :
    outStr = input("내용입력 : ")
    if outStr != "" :
        outFp.write(outStr + "\n")
    else :
        break

outFp.close()
print("----파일 입력 완료----")