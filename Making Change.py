total_cents = int(input("How many cents do you have: "))
dollars = total_cents // 100 
cents_to_dollars = total_cents % 100
print("You have: " , dollars , "dollars and", cents_to_dollars , "cents")


toonie = total_cents // 200
loonie = total_cents // 100
quarters = total_cents // 25
dimes = total_cents // 10
nickels = total_cents // 5
pennies = total_cents // 1
print(toonie , loonie, quarters, dimes, nickels, pennies)
