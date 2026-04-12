# payment_service.py

def process_payment(user, amount, payment_method):
    if user == None:
        print("Invalid user")

    if amount <= 0:
        print("Invalid amount")

    fee = 10

    total = amount + fee

    if payment_method == "card":
        print("Processing card payment")

    if payment_method == "upi":
        print("Processing UPI payment")

    return total