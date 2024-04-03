import re

def calculate_total_price(check):
    total_price = 0
    
    pattern = r'([a-z]+)(\d+\.*\d*)'
    matches = re.findall(pattern, check)
    
    for match in matches:
        price = float(match[1])
        total_price += price
    
    return total_price

check = "apple2.5banana1.75orange3tomato5"
total_price = calculate_total_price(check)
print(f"Total price: {total_price}")
