#Python Program to find the area of triangle
a = 5
b = 6
c = 7

#Calculate the semi-perimeter
s = (a + b + c) / 2

#Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is :" ,area)

#Output:-
The area of the triangle is : 14.696938456699069
