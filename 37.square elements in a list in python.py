#using for loop
li=[1,2,3,4,5]
li=[i**2 for i in li]
print(li)

#Output:
[1, 4, 9, 16, 25]


#using append
li1=[1,2,3,4,5]
li2=[]
for num in li1:
    x=num*num
    li2.append(x)
print(li2)

#Output:
[1, 4, 9, 16, 25]



#using enumerate
li=[1,2,3,4,5]
for i,v in enumerate(li):
    li[i]=v**2
print(li)    

#Output:
[1, 4, 9, 16, 25]


#using map function
l1=[1,2,3,4,5]
print(list(map(lambda a:a*a,l1)))

#Output:
[1, 4, 9, 16, 25]
