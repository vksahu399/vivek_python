class Area():
        pi=3.14
        def __init__(self,r):
            self.myarea=Area.pi*r*r  #Area.py  inside class

#myzone=Area(r=5)
#print (myzone.myarea)
#print (myzone.pi)

        def msg (self,mymsg):
            print (mymsg)

myzone=Area(5)
myzone.msg("hi")           

