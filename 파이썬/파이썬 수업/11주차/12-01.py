class Car : 
    color = ""
    speed = 0
    
    def upSpeed(self, value) : 
        self.speed += value
        
    def downSpeed(self, value) : 
        self.speed -= value
        
    def printMessage() : 
        print("시험 출력이다.") #필드사용 X >> self 생략
        
myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

myCar1.color = "빨강"
myCar1.speed = 0
myCar2.color = "파랑"
myCar2.speed = 0
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
myCar2.downSpeed(60)