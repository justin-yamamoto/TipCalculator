print("Welcome to the Tip Calculator\n")

bill_amount = input("How much is the total bill?\n ")
new_bill_amount = float(bill_amount)

tip20_amount = float(new_bill_amount * .20)
tip18_amount = float(new_bill_amount * .18)
tip15_amount = float(new_bill_amount * .15)

total_people = input("How many people to split the bill? \n")
new_total_people = int(total_people)

print("Tip Amount Per Person: \n")
print("20%: " + "$" + str(tip20_amount/new_total_people))
print("18% " + "$" + str(tip18_amount/new_total_people))
print("15% " + "$" + str(tip15_amount/new_total_people))

