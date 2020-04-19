#Exercise 9 (Compound Interest)
money = float(input("How much are you depositing? "))
#Year 1
interest_1 = money * 0.04
final_money_1 = interest_1 + money
#Year 2
interest_2 = final_money_1 * 0.04
final_money_2 = final_money_1 + interest_2
#Year 3
interest_3 = final_money_2 *0.04
final_money_3 = final_money_2 + interest_3

print("Total money after one year: $",round (final_money_1,2))
print("Total money after two years: $", round (final_money_2,2))
print("Total money after three years: $", round (final_money_3,2))
