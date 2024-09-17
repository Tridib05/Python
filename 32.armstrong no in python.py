num=int(input("Enter a number:"))
New_num = num
sum = 0
while(num>0):
    digit=num % 10
    sum+=digit ** 3
    num=num // 10
if(sum==New_num):
    print("The given number is Armsstrong no")
else:
    print("The given number is not Armsstrong no")

#Output:
Enter a number:153
The given number is Armsstrong no
