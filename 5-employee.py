class employee:
    def __init__(self,name,salary,doj):
        self.name=name
        self.salary=salary
        self.doj=doj
        
    def emp(self):
        print(self.name)
        print(self.salary)
        print(self.doj)
        
        
e1=employee("Hema","40000","14-Jul-2021")
e1.emp()
