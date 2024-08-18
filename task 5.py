
while True:
    
    line = input("Enter a line of text (or 'done' to finish): ")
    
    if line.lower() == 'done':
        break
    
    if line.startswith('#'):
        continue
    
    print(line)
