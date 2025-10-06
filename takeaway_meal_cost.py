"""
Student Name:Kim Kha Nguyen
Student ID:s8199557

"""

VEGETARIAN = 11.80
MEAT = 12.80
SEAFOOD = 14.00

# Get user input for number of meals of each type
vegeterian_meals = int(input("Enter the nummber of vegetarian meals: "))
meat_meals = int(input("Enter the number of vegetarian meals: "))
seafood_meals = int(input("Enter the number of seafood meals: "))
# Calculate total cost for each meal type
cost_vegetarians_meals = vegeterian_meals * VEGETARIAN
cost_meat_meals = meat_meals * MEAT
cost_seafood_meals = seafood_meals * SEAFOOD
# Calculate overall total cost
total_cost = cost_meat_meals + cost_seafood_meals + cost_vegetarians_meals
# Print the order details and total cost
print(f"Total cost for the order is: ${total_cost:.2f}")


