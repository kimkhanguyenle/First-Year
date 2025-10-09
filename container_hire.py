"""
Student Name: Kim Kha Nguyen
Student ID: s8199557

"""

SMALL_CONTAINER_MAX_VOLUME = 12.25
MEDIUM_CONTAINER_MAX_VOLUME = 15.84
LARGE_CONTAINER_MAX_VOLUME = 33.2

BASE_PRICE_PER_CUBIC_METER = 156.6

SMALL_CONTAINER_DISCOUNT = 0
MEDIUM_CONTAINER_DISCOUNT = 0.10  # 10% cheaper per cubic meter then small container
LARGE_CONTAINER_DISCOUNT = 0.25  # 25% cheaper per cubic meter then small container


def get_crate_volume(length, width, height):    
    return length * width * height

def calculate_shipping_cost(volume):
    if volume <= 0:
        return 0.0
    elif volume <= SMALL_CONTAINER_MAX_VOLUME:
        return BASE_PRICE_PER_CUBIC_METER * 12.25
    elif volume <= MEDIUM_CONTAINER_MAX_VOLUME:
        return BASE_PRICE_PER_CUBIC_METER * 15.84 * (1 - 0.10)
    elif volume <= LARGE_CONTAINER_MAX_VOLUME:
        return BASE_PRICE_PER_CUBIC_METER * 33.2 * (1 - 0.25)
    else:
        return 0.0       
    

def main():
    print("Welcome to the Shipping Cost Estimation Program")
    length = float(input("Enter the length of the goods (in meters): "))
    width = float(input("Enter the width of the goods (in meters): "))
    height = float(input("Enter the height of the goods (in meters): "))

    volume = get_crate_volume(length, width, height)
    cost = calculate_shipping_cost(volume)
   

    print(f"\nThe estimated shipping cost for the provided dimensions is:")
    print(f"Shipping cost: ${cost:,.2f}")

if __name__ == "__main__":
    main()
