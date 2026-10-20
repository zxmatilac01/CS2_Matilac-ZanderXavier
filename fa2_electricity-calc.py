# Electricity Bill Calculator
RATE = 12.90

#Validation of User's Name
while True:
    name = input("Enter customer name: ")
    if name == "":
        print("Invalid Name. Please try again.")
    else:
        break

#Validation of previous meter reading
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if previous < 0:
        print("Invalid previous meter reading. Must be no less than 0.")
    else: 
        break

#Validation of current meter reading
while True:
    current = float(input("Enter current meter reading: "))
    
    if current < previous:
        print("Invalid current meter reading. Must be no less than previous meter reading.")
    else:
        break

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
