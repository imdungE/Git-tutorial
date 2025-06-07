inFp, outFp = None, None
inStr = ""
#exe파일로 해야함
inFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "rb", encoding = "utf-8")
outFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주2.txt", "wb", encoding = "utf-8")

while True : 
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")