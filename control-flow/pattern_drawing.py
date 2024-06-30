size = int(input("Enter the size of the pattern: "))
 # Initialize the row counter
row = 0
    
    # Use a while loop to iterate through each row
while row < size:
        # Use a for loop to print asterisks side by side
     for _ in range(size):
            print("*", end="")
        # Print a newline character after completing each row
     print()
        # Increment the row counter
     row += 1