# assining in list

list=[1,2,3,4,5,6]
list1=['a','b','c']
list2=["ram","dev","nitin"]
list3=['a',"raj",'b',"vivek",5]
list4=[100,20,30,60,50,40,70,80,90]
# How to print list

print (list,list1,list2,list3)
#          OR
#print (list1)
#print (list2)
#print (list3)
print ("*********************************************************************************************************")
# print lenth

print (len(list))
print ("*********************************************************************************************************")
# Print single element of list
# List item by index 

print (list[2]) 
print (list1[2])
print (list2[2])
print (list3[2])
print ("*********************************************************************************************************")
# Reassign item to list
list3[3]='c'
print (list3)
print ("*********************************************************************************************************")
# append list

list3.append(list1)
print (list3)
print ("*********************************************************************************************************")
# one element append
print ("*********************************************************************************************************")
list3.append(list[2])
print (list3)
print ("*********************************************************************************************************")
# extend list

list2.extend(list)
print (list2)
print ("*********************************************************************************************************")
# remove element from list

item=list2.pop()
print (list2)
print (item)
print ("*********************************************************************************************************")
# Reverse

list3.reverse()
print (list3)
print ("*********************************************************************************************************")
# Sorting
list4.sort()
print (list4)
print ("*********************************************************************************************************")
#  2D array print // Access of list item within list

print (list3[1][1])
print ("*********************************************************************************************************")
# Matrix

matrix=[[1,2,3],[10,5,6],[1,2,10]]

first_col= [row[0] for row in matrix]
print (first_col)
second_col= [row[1] for row in matrix]
print (second_col)
third_col=[row[2] for row in matrix]
print (third_col)
print ("*********************************************************************************************************")