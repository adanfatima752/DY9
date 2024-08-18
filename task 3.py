
user_input = input("Enter a list of integers separated by spaces: ")

numbers = list(map(int, user_input.split()))

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

for number in numbers:
    if number < smallest:
        smallest = number

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
