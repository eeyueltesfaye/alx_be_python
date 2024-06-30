'''age = int(input("enter ur age: "))
if age >= 18 :
    print("u are eligible to vote.")
else:
    print("u are not eligible to vote yet.")'''

'''purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount >= 1000:
  discount = 0.1  # 10% discount
elif purchase_amount >= 500:
  discount = 0.05  # 5% discount
else:
  discount = 0  # No discount

final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))'''

'''score = int(input("enter ur score: "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = "F"
print("Your grade is:", grade)'''

# Ternary operator 

'''age = 19
message = "Eligible "if age >= 18  else "not Eligible"
print(message)'''

'''age = 22 
if 18 <= age < 65:
    print('Eligible')'''

'''if 10 == '10':
    print('a')
elif "bag"> "apple" and  "bag"> "cat":
    print('b')
else:
    print('c')'''

# Match case 
'''day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")'''


secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
  guess_count += 1
  guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")




