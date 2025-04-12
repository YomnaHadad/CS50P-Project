all_paid = 0
print("Amount Due: 50")
while all_paid < 50:
    income = int(input("Insert Coin: "))
    if income in [25 , 10 , 5]:
        all_paid += income
        if  all_paid < 50:
            print("Amount Due:" , abs(50-all_paid) )
    else:
        print("Amount Due: 50")

print("Change Owed:", all_paid-50)

