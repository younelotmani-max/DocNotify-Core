import re


def validate_phone(phone):
    check = re.search(r"^(06|07)\d{8}$", phone)
    
    if check:
        return True
    else:
        return False