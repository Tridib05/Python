for i in range(0,6):
    for j in range(0,7):
        if(i==0 and j%3!=0)or(i==1 and j%3==0)or(i-j==2)or(i+j==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
