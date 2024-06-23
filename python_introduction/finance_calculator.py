monthly_income = float(input( "Enter your monthly income: "))
monthly_expense = float(input( "Enter your total monthly expenses: "))
Monthly_Savings = monthly_income - monthly_expense
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Your monthly savings are ${Monthly_Savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")
