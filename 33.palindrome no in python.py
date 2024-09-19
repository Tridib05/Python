num=int(input("Enter the number:"))
p=num
sum=0
while(num>0):
    d=num%10
    sum=sum*10+d
    num=num//10
if(p==sum):
  print("Palindrome no")
else:
   print("not Palindrome no")

#Output:
Enter the number:121
Palindrome no
