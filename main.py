bill = float(input("What was the total amount of bill? $"))
tip = float(input("How much tip would you like to give? %"))
people = float(input("How many people to split the bill? "))
costoftip = bill / 100 * tip
totalcost = (bill + costoftip) / people
finalperperson = round(totalcost, 2)
finalamount = "{:.2f}".format(finalperperson)
print(f"Each person should pay: ${finalamount}")