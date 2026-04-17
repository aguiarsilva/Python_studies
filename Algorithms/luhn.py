#Practicing Algorithms in FreeCodeCamp. Assignement: Make Luhn algorithm to validadte Credit Cards
def verify_card_number(digits: str):
    clean_digits = digits.replace("-", "").replace(" ", "")
    if not clean_digits.isdigit():
        return "INVALID!"

    total_sum = 0
    for i, digit_char in enumerate(reversed(clean_digits)):
        digit = int(digit_char)
        if i % 2 == 1:
            double = digit * 2
            if doubled > 9:
                doubled = doubled - 9
            total_sum += doubled
        else:
            total_sum += digit

    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

