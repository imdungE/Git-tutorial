inFp = None 
inList, inStr = [], ""

inFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "r", encoding = "utf-8")

inList = inFp.readlines()
for inStr in inList : 
    print(inStr, end = "")

inFp.close()