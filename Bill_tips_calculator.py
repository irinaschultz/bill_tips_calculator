print("Wecome to the bill and tip calculator!")
#If the bill was $150.00, split between 5 people, with 12% tip. 
bill=float(input("What was the total bil? $"))
tip=int(input("How much percent of tip would you like to give? 10, 12 or 15? Please add the number only  "))
people = int(input("How many people to split the bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")


