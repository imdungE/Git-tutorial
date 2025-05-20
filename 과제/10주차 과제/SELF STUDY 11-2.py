inFp = None
inList, inStr, n = [], "", 1

inFp= open("C:\\Users\\titic\\OneDrive\\바탕 화면\\Github\\Git-tutorial\\과제\\10주차 과제\\제목 없음.txt", "r", encoding = "utf-8")

inList = inFp.readlines()
for inStr in inList :
    print("%d: " % n, end = "")
    n += 1
    print(inStr, end = "")

inFp.close()