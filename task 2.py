
numbers = [1, 5, 8, 12, 16, 3, 9, 4]

threshold = float(input("Enter the threshold: "))
print(f"Numbers greater than {threshold}:")
for number in numbers:
    if number > threshold:
        print(number)
