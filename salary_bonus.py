"""
Student Name:Kim Kha Nguyen
Student ID:s8199557

"""

# Price of a brick
BRICK_PRICE = 1.0

# Thresholds
THRESHOLD_1 = 1000
THRESHOLD_2 = 3000
THRESHOLD_3 = 7000

# Rates
RATE_2 = 0.05
RATE_3 = 0.10
RATE_4 = 0.15

# Base deductions
BASE_2 = 0
BASE_3 = 100
BASE_4 = 500

# Input
number_bricks_purchased = int(input("Enter number of bricks purchased: "))

# Check valid input
if number_bricks_purchased < 1:
    print("The number of bricks purchased cannot be smaller than 1")
    exit()

bricks_price = number_bricks_purchased * BRICK_PRICE

# Calculate discount
if number_bricks_purchased <= THRESHOLD_1:
    discount = 0
elif number_bricks_purchased <= THRESHOLD_2:
    # apply 5% for bricks above 1000
    discount = (number_bricks_purchased - THRESHOLD_1) * BRICK_PRICE * RATE_2 + BASE_2
elif number_bricks_purchased <= THRESHOLD_3:
    # apply 10% for bricks above 3000 + $100 deduction
    discount = (number_bricks_purchased - THRESHOLD_2) * BRICK_PRICE * RATE_3 + BASE_3
else:
    # apply 15% for bricks above 7000 + $500 deduction
    discount = (number_bricks_purchased - THRESHOLD_3) * BRICK_PRICE * RATE_4 + BASE_4

# Final price
total_price = bricks_price - discount

# Output
print(f"Number of bricks purchased: {number_bricks_purchased}")
print(f"Your discount: ${discount:,.2f}")
print(f"Final cost: ${total_price:,.2f}")
