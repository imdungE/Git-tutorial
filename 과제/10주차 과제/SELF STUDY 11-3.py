inFp = None
fName, inStr = "", ""

fName = input("파일명을 입력하세요 : ")
inFp = open(fName, "w", encoding = "utf-8")

while True:
    inStr = input("내용 입력 : ")
    if inStr != "" :
        inFp.writelines (inStr + "\n")
    else:
        break

inFp.close()
print("---정상적으로 파일에 씀---")