inFp, outFp = None, None
inStr = ""

inFp = open("C:\\Users\\titic\\OneDrive\\사진\\스크린샷\\스크린샷 2025-06-07 235517.png", "rb")
outFp = open("C:\\Users\\titic\\OneDrive\\사진\\스크린샷\\b - 복사본.png", "wb")

while True : 
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")