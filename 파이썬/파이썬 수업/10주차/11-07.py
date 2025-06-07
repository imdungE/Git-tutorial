outFp = None
outStr = ""

outFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "w", encoding = "utf-8")
while True : 
    outStr = input("내용 입력 : ")
    if outStr != "" : 
        outFp.writelines(outStr + "\n")
    else : 
        break

outFp.close()
print("---정상적으로 파일에 씀---")