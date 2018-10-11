class Calc():
    def __init__(self):
        print ("Class object created")
    def sum(self,a,b):
        self.n=a
        self.n=b
        self.s=a+b
        print (self.s)        
    def sub(self,a,b):
        self.n1=a
        self.n2=b
        self.su=a-b
        print (self.su)
    def mul(self,a,b):
        self.n3=a
        self.n4=b
        self.m=a*b
        print (self.m)
    def div(self,a,b):
        self.n5=a
        self.n6=b
        self.d=a-b
        print (self.d)
c=Calc()
c.sum(2,2)
c.sub(4,2)
c.mul(4,2)
c.div(4,2)
