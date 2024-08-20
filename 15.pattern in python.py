//square pattern using "*"
a = 4
for i in range(a):
    for j in range(a):
        print('*', end = ' ')
    print()

#Ouput:- 
* * * * 
* * * * 
* * * * 
* * * * 

//print horizontal line 1-4
a=5
for i in range(1,a):
    for j in range(1,a):
        print(i, end=" ")        
    print()

#Output:-
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 

//print vertical line 1-4
a=5
for i in range(1,a):
    for j in range(1,a):
        print(j, end=" ")        
    print()

#Output:-
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

//print pyramid pattern using number
for i in range(1,5):
   for k in range(1,i+1):
        print(i,end="")
   print(" ")

#Output:-
1 
22 
333 
4444

//print pyramid pattern using "*"
for i in range(0,5):
    for j in range(0,i+1):
        print("*", end=" ")
    print()
  
#Output:-
* 
* * 
* * * 
* * * * 
* * * * * 

//print a pyramid whose second line is double printed using number
for i in range(1,5):
   for k in range(1,i*2):
        print(i,end="")
   print()

#Output:-
1
222
33333
4444444

//print a pyramid whose second line is double printed using "*"
k=1
for i in range(0,3):
    for j in range(1,k+1):
        print("*", end=" ")  
    print()    
    k=k+2
  
#Output:-
* 
* * * 
* * * * * 

//print a right angled triangle pattern using "*"
for i in range(1,5):
    for j in range(1,5-i):
        print(end=" ")
    for k in range(1,i+1):
        print("*", end="")
    print()

#Output:-
   *
  **
 ***
****

//full pyramid patterns using "*"
for i in range(1,5):
    for j in range(1,5-i):
        print(end=" ")
    for k in range(1,i+1):
        print("*", end=" ")
    print()

#Output:- 
   * 
  * * 
 * * * 
* * * * 

//reverse pyramid using "*"
for i in range(1,5):
    for j in range(1,i):
        print(end=" ")
    for k in range(1,6-i):
        print("*",end="")
    print() 

#Output:-
****
 ***
  **
   *

//print "X" pattern
for i in range(1,6):
    for j in range(1,6):
        if(i==j or j==6-i):
            print("*",end="")
        else:
            print(end=" ")
    print()            

#Output:-
*   *
 * * 
  *  
 * * 
*   *

//print "M" pattern
for i in range(1,5):
    for j in range(1,8):
        if(i==j or j==1 or j==7 or i+j==8):
            print("*",end="")
        else:
            print(end=" ")    
    print()

#Output:-
*     *
**   **
* * * *
*  *  *

//print 1 to 8 but skipped 5
for i in range(1,9):
    if i==5:
        continue
    print(i)

#Output:-
1
2
3
4
6
7
8
     
    



