# =========================
# COMMENTING IN EXIXTING PR TO TEST WEBHOOKS!!!! TEST 6
# =========================



def get_user_name(user):
    if not user:
        return None
    return user.name


def calculate_total(amount, tax):
    final_amount = amount + tax
    return final_amount


def is_valid(age):
    return age >= 18


def login(password):
    if password == "admin123":
        print("Logged in")  # added behavior
        return True
    return False


def process(data):
    if not data:
        return []
    return data


def fetch_user(user):
    if user is None:
        return None
    return user