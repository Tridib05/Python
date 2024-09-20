#Nested a list
li1=[1,'A',"abc",[2,3,4,5],8,9]
i=0
while i<(len(li1)):
    print("li1[",i,"]=",li1[i])
    i+=1

#Output:
li1[ 0 ]= 1
li1[ 1 ]= A
li1[ 2 ]= abc
li1[ 3 ]= [2, 3, 4, 5]
li1[ 4 ]= 8
li1[ 5 ]= 9



#length a list
li = [10, 20, 30, 40, 50]
length = len(li)
print(length)                # Output: 5



#slicing a list
li = [10, 20, 30, 40, 50]
print(li[1:4])              # Output: [20, 30, 40]
print(li[:3])               # Output: [10, 20, 30]
print(li[2:])               # Output: [30, 40, 50]
print(li[::2])              # Output: [10, 30, 50]
print(li[::-1])             # Output: [50, 40, 30, 20, 10]


#Traversing a list
li=[4,9,2,6,14,11]
for num in li:
    print(num)

#Output:
4
9
2
6
14
11



#Joining a list
li1=[4,9,2,14,11]
li2=[1,2,4,6,9,11]
li3=li1+li2
print(li3)            #Output: [4, 9, 2, 14, 11, 1, 2, 4, 6, 9, 11]



#Compare a list
li1=[4,9,2,6,14,11]
li2=[1,2,4,6,9,11]
li3=[]
for num in li1:
    if num not in li3:
        li3.append(num)
for num in li2:
    if num not in li3:
        li3.append(num)
print(li3)               #Output: [4, 9, 2, 6, 14, 11, 1]



#Replication of list
li=[4,9,2,6,14,11]
li3=li1.copy()
print(li3)              #Output: [4, 9, 2, 6, 14, 11]
