def calculate_total(price, tax, discount):
    total = price + tax

    # applying discount
    if discount:
        total = total - discount

    # adding fixed platform fee (BAD PRACTICE)
    total = total + 50

    return total


def place_order(user, items):
    if not items:
        return "No items"

    total_price = 0

    for item in items:
        total_price += item["price"]

    # missing tax calculation (BUG)
    final_amount = calculate_total(total_price, 0, None)

    return {
        "user": user,
        "amount": final_amount
    }