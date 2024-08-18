
N = int(input("Enter the value of N: "))

sum_of_squares = 0

for i in range(1, N + 1):
    sum_of_squares += i ** 2

print(f"The sum of the squares of the first {N} natural numbers is: {sum_of_squares}")
