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
class My(Calc):
    def __init__(self):
        Calc.__init__(self)

    def perc(self,x,y):
        self.n7=x
        self.n8=y
        self.p=self.n7*self.n8/100
        print (self.p)


c=My()
c.sum(2,2)
c.sub(4,2)
c.mul(4,2)
c.div(4,2)
c.perc(448,18)
