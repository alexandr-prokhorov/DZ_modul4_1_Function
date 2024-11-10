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
    return user_data not in data_to_check

def reg_check(user_data, reg_pattern, users_list, field_index=None):
    if not re.match(reg_pattern, user_data):
        return None

    if field_index is not None:
        data_to_check = [user[field_index] for user in users_list]
        if not check_unique_data(user_data, data_to_check):
            return None
    return user_data