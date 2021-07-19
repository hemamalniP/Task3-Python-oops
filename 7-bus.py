class bus:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        
    def detail(self):
        print(self.name)
        print(self.max_speed)
        print(self.mileage)
        
        
e1=bus("volvo","120","4")
e1.detail()
