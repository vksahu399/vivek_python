'''
# imutable
x=10
print (id(x))
x=100
print (id(x))

# mutable
list1=[1,2,3,4,5,6,7]
print (id(list1))
# reassign
list1[3]=12
print (id(list1))

# dictionary
mydic = dict(
    name="Rajiv",age=22,salary=1000.35
)
print (mydic)
#datatype
print (type(mydic))


# get value by key

print (mydic["age"])
print (mydic["name"])

# delete value from dictionary
del(mydic["age"])
print (mydic)

# update value by key
mydic["name"]="kuldeep"
print (mydic)

print ("tuple example")
# tuple
k=(1,2,3,4)
print (k)
print (type(k))

# print value from tople
print(k[1])

# reassign

#k[1]=12 # this is mutable so can not assign value
#print (k)

# add value in tuple
#k.add(5)       # not happend in tuple
#k.add(0.1)
#print(k)

# set
l=set()
print (l)
l.add(5)
l.add(0.1)
print (l)
l.add(5)
print (l)
'''
color=['r','g','b','y','r','g','y']
print (color)
# smart conveersion
xcolor=set(color) 
print (xcolor)

