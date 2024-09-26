#creating single element tuple:
a1=(2,)
a=("Hello World",)
print(type(a1))
print(type(a))

#Output:
<class 'tuple'>


#creating empty tuple:
a=()
print(type(a))

#Output:
<class 'tuple'>


#creating tuple without parentheses (tuple packing):
aa= 1, 2, 3
print(type(aa))

#Output:
<class 'tuple'>


#nested tuple:
b = ((1, 2, 3), ("a", "b", "c"), (True, False))
print(b)

#Output:
((1, 2, 3), ('a', 'b', 'c'), (True, False))


#accessing of tuple:
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])         
print(my_tuple[2])          

# Output: 
10
30


#traverse of tuple:
c = (23,15,6,9,4)
for num in c:
    print(num)

#Output:
23
15
6
9
4


