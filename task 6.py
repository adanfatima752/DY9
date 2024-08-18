
predefined_number = 7

max_attempts = 10

attempts = 0

while attempts < max_attempts:
    
    guess = int(input("Guess the number (between 1 and 10): "))
 
    if guess == predefined_number:
        print("Congratulations! You've guessed the number correctly.")
        break  
    else:
        
        attempts += 1
        
        if attempts < max_attempts:
            print(f"Incorrect. You have {max_attempts - attempts} attempts left.")
        else:
            print("Sorry, you've reached the maximum number of attempts.")

if attempts == max_attempts and guess != predefined_number:
    print(f"The correct number was {predefined_number}. Better luck next time!")
