#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator :)")

total = float(input("What was your total?\n"))

tip = float( (input ("What percent of your total would you like to tip?\n") ) )

actual_tip = (tip / 100 + 1)

group_amount = int( input( "Amongst how many people are you splitting the bill?\n") )

each_person = ((total / group_amount) * actual_tip)

print("Each person pays $",format(each_person, ".2f"))