def max(a, b, c): 
    if (a >= b) and (a >= c): 
        print("The maximum number is:",a)
    elif (b >= a) and (b >= c): 
        print("The maximum number is:",b)
    else:
        print("The maximum number is:",c)
    return max  
a = 5
b = 7
c = 6
print(max(a, b, c)) 

#Output:
The maximum number is: 7
<function max at 0x000001D8FA10A2A0>
