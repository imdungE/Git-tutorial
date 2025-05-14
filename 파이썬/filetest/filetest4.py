inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0

secuYN = input("1. 암호화 2. 암호 해석 : ")
inFname = input("입력 파일명 : ")
outFname = input("출력 파일명 : ")

if secuYN == "1" :
    secu = 100
elif secuYN == "2" :
    secu = -100

inFp = open(inFname, "r", encoding = "utf-8")
outFp = open(outFname, "w", encoding = "utf-8")

while True :
    inStr = inFp.readline()
    if not inStr :
        break

    outStr = ""
    for i in range(0, len(inStr)) :
        ch = inStr[i]
        chNum = ord(ch)
        chNum += secu
        ch2 = chr(chNum)
        outStr += ch2
    outFp.write(outStr)

inFp.close()
outFp.close()
print("%s --> %s 변환 완료" % (inFname, outFname))