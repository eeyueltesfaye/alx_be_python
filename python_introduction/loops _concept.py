eyu_age = 24
school_age = 19
if eyu_age<school_age:
    print('you are under age')
else:
    print('well done')    

print('under gone')

def full_name (text):
    text = 'eyuel'
    print (text)
    print (text)
    print (text)
full_name ("eyuel")
full_name ("eyuel")

# foor loop
# Purpose: The for loop is typically used when the number of iterations is known or when iterating over a sequence (like a list, tuple, string, or range). 
# Iterating over a fixed number of elements.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop  
# Purpose: The while loop is used when the number of iterations is not known beforehand and depends on a condition being true.
# Running a loop until a specific condition is met.

'''i = 1
while i <= 5:
    print(i)
    i += 1
'''

# do while loop  in python there is no do while loop but instead we can use while loop with break statement.
while True:
    user_input = input("Enter a number (enter '0' to exit): ")
    
    # Process the input
    print(f"You entered: {user_input}")
    
    # Check the condition to exit the loop
    if user_input == '0':
        break

# break and continue statemeny