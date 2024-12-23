def total_price(cart):
    if not cart:
        return "The cart is empty. Total Price: 0"
    total = sum(cart.values())
    if len(cart) > 5:
        total *= 0.9 
    return total

cart={'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print("Total Price:",total_price(cart))
