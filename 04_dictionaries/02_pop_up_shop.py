def fruit_shop():
    fruit_prices = {
        "apple": 2,
        "banana": 1,
        "orange": 1.5,
        "pear": 2.5,
        "grape": 3
    }
    
    total_cost = 0
    
    print("Available fruits and their prices:")
    for fruit, price in fruit_prices.items():
        print(f"{fruit.capitalize()}: ${price} per unit")
    
    print("\nEnter the quantity for each fruit you want to buy:")
    
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many {fruit}s would you like to buy? "))
        total_cost += quantity * price
    
    print(f"\nThe total cost for all the fruits is: ${total_cost:.2f}")

fruit_shop()
