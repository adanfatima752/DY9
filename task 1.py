
numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break  
    
    try:
        number = float(user_input)  
        numbers.append(number)  
    except ValueError:
        print("Invalid input, please enter a number or 'done' to finish.")

if numbers:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"The sum of the numbers is: {total_sum}")
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers were entered.")
