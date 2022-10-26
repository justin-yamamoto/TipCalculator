print("Welcome to the Tip Calculator\n")

bill_amount = input("How much is the bill?\n ")
new_bill_amount = float(bill_amount)

tip20_amount = float(new_bill_amount * .20)
tip18_amount = float(new_bill_amount * .18)
tip15_amount = float(new_bill_amount * .15)

print("Tip Amounts: \n")
print("20%: " + "$" + str(tip20_amount))
print("18% " + "$" + str(tip18_amount))
print("15%" + "$" + str(tip15_amount))

