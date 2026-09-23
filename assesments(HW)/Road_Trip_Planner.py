#gather data for trip
#• User’s name
#• Destination
#• One-way distance in miles
#• Vehicle miles per gallon
#• Gas price per gallon
#• Number of travelers
name = input("Enter your name: ")
destination = input("Enter your destination: ")
distance = float(input("Enter the one-way distance in miles: "))
mpg = float(input("Enter your vehicle's miles per gallon: "))
gas_price = float(input("Enter the gas price per gallon: "))
travelers = int(input("Enter the number of travelers: "))

#Your program should calculate:
#• Total miles for the round trip
#• Gallons of gas needed
#• Estimated gas cost
#• Estimated cost per traveler


total_miles = distance * 2

gallons_needed = total_miles / mpg

estimated_gas_cost = gallons_needed * gas_price

cost_per_traveler = estimated_gas_cost / int(travelers)

#Print a trip summary that includes info calculated above
print ("Road Trip Summary")
print ("------------")
print (f"traveler name: {name}")
print (f"destination: {destination}")
print (f"estimated gas cost: ${estimated_gas_cost}")
print (f"estimated cost per traveler: ${cost_per_traveler}")
print("------------")
print ("Have a safe trip!")