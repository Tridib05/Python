def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = 10
print("Fibonacci series with {n} elements:", end=" ")
fibonacci_series(n)

#Output:
print("Fibonacci series with {n} elements:", end=" ")


#Another process........

def fibonacci_series():
    num = 8 
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(0,num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
print(fibonacci_series())

#Output:
Fibonacci Series: 0 1 1 2 3 5 8 13 21 34
