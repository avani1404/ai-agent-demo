# =========================
# BEFORE VERSION (MAIN)
# =========================

def get_user_name(user):
    if user is None:
        return None
    return user.name


def calculate_total(price, tax):
    total = price + tax
    return total


def is_valid(age):
    if age >= 18:
        return True
    return False


def login(password):
    if password == "admin123":
        return True
    return False


def process(data):
    if data is None:
        return []
    return data


def fetch_user(user):
    if user == None:
        return None
    return user