
user_input = input("Enter a list of integers separated by spaces: ")

numbers = list(map(int, user_input.split()))

unique_numbers = set()

for number in numbers:
    unique_numbers.add(number)

unique_list = list(unique_numbers)

print("List after removing duplicates:", unique_list)
