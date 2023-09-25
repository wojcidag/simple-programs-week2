guests = input("Enter number of guests attending -> ")
pizza_slices = input("How many slices does the pizza have? -> ")

guest_allowance = int(guests) * 3
pizza_division = int(guest_allowance) / int(pizza_slices)
pizza_purchase = float(pizza_division) + bool(pizza_division%1)
 
print("Here is how many pizzas you need to purchase -> " ,int(pizza_purchase))