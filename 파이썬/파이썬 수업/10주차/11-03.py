inFp = None 
inList = ""

inFp = open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\파이썬\\문찬주.txt", "r", encoding = "utf-8")

inList = inFp.readlines()
print(inList)

inFp.close()