#add import
import question_a

sales = float(input("Enter your total sales amount: ")) #Write code to prompt the user for their total sales amount

bonus = question_a.get_bonus_pay_amount(sales)

print("Your bonus pay is: ")
print(bonus)