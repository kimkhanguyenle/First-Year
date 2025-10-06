"""
Student Name: Kim Kha Nguyen
Student ID:s8199557

"""

# Constants - book prices
NEW_BOOK_PRICE = 10.0
OLD_BOOK_PRICE = 4.50
RENT_RATE = 2.0

# The number of books that customers purchase
new_books = int(input("How many new books: "))
old_books = int(input("How many old books: "))
# The total price for each type of books
new_books_price = new_books * NEW_BOOK_PRICE
old_books_price = old_books * OLD_BOOK_PRICE
# The number of days that customer lend books
days_to_rent = int(input("How many days to rent: "))
# The number of books that customen rent
rent_books = int(input("How many books to rent: "))
# Total rent books price
rent_books_price = rent_books * RENT_RATE * days_to_rent


#The final price
total_final_price = new_books_price + old_books_price + rent_books_price
# Print final price
print(f"The final total: ${total_final_price:.2f}")

