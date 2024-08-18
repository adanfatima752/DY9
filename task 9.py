
N = int(input("Enter the number of Fibonacci numbers to display: "))

a, b = 0, 1

print(f"The first {N} numbers in the Fibonacci sequence are:")

for _ in range(N):
    print(a, end=" ") 
    a, b = b, a + b  

print() 
