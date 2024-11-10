import re

def get_reg_data():
    patterns = {
        "name": r"^[a-zA-Zа-яА-ЯёЁ]+$",
        "surname": r"^[a-zA-Zа-яА-ЯёЁ]+$",
        "telephone": r"^\+\d{1,3}\(\d{2}\)\d{7}$",
        "mail": r"^[a-zA-z-0-9]+@yandex\.ru$"
    }
    return patterns

def check_unique_data(user_data, data_to_check):
    for user in data_to_check:
        if user_data == user:
            return False
    return True

def reg_check(user_data, reg_pattern, data_to_check=None):
    if not re.match(reg_pattern, user_data):
        return None

    if data_to_check is not None:
        if not check_unique_data(user_data, data_to_check):
            return None
    return user_data