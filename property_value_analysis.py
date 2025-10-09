""""
Student Name:Kim Kha Nguyen
Student ID:s8199557


***SAMPLE RUN***
Enter the current value of the property ($): 500000
Enter the distance to the city (km): 21
Enter the number of years to estimate future value: 3
  Year        Value($)
======================
     1     505,000.00
     2     510,050.00
     3     515,150.50
Value of the property after 3 years: $515,150.50

***SAMPLE RUN***
Enter the current value of the property ($): 500000
Enter the distance to the city (km): 19
Enter the number of years to estimate future value: 3
  Year        Value($)
======================
     1     510,000.00
     2     520,200.00
     3     530,604.00
Value of the property after 3 years: $530,604.00


"""

CITY_BORDER_THRESHOLD = 20.0
APPRECIATION_RATE_CLOSE = 0.02
APPRECIATION_RATE_FAR = 0.01
LINE_LENGTH = 22

property_value = float(input("Enter the current value of the property ($): "))
distance = float(input("Enter the distance to the city (km): "))
number_of_years = int(input("Enter the number of years to estimate future value: "))

print("\nYear\tValue($)")
print("=" * LINE_LENGTH)

current_value = property_value

for year in range(1, number_of_years + 1):
    if distance <= CITY_BORDER_THRESHOLD:
        current_value *=  (1 + APPRECIATION_RATE_CLOSE)
    else:
        current_value *=  (1 + APPRECIATION_RATE_FAR)
    print(f"{year}\t{current_value:,.2f}")


print(f"Value of the property after {number_of_years} years: ${current_value:,.2f}")
    

