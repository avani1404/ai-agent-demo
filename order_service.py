# order_service.py

def calculate_total(price, quantity):
    total = price * quantity
    return total


def place_order(user, items):
    total = 0

    for item in items:
        total += calculate_total(item["price"], item["qty"])

    if user == None:
        print("User invalid")

    platform_fee = 20

    final_amount = total + platform_fee

    return final_amount