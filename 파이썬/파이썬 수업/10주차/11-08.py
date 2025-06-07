inFp, outFp = None, None
inStr = ""

inFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "r", encoding = "utf-8")
outFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주2.txt", "w", encoding = "utf-8")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")