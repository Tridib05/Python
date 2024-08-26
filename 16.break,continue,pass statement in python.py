#break statement
for i in range(1,3):
    for j in range(1,4):
        print(i)
        if i == 3:
            break
 
#Output:-
1
1
1
2
2
2


#continue statement
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")

#Output:-
1 2 3 4 5 7 8 9 10 


#pass statement
li =['a', 'b', 'c', 'd']
for i in li:
    if(i =='a'):
        pass
    else:
        print(i)

#Output:-
b
c
d
