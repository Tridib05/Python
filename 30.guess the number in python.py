Num=15
for i in range(1,4):
    guess= int(input("Enter a number:"))  
    if(Num==guess):
        print("Well done")
        break
    elif(Num>guess):
        print("You have enter smaller no")
    else:
        print("You have enter bigger no")
else:
    print("You lost!")

#Output:
Enter a number:14
You have enter smaller no
Enter a number:16
You have enter bigger no
Enter a number:12
You have enter smaller no
You lost!

