

def type_card_and_account_number(type_and_number):
    split_number = type_and_number.split()
    if "счет" in split_number:
        number = split_number[-1]
        masks_number = account_number(number)
        name_and_masks = split_number[0], masks_number
        return " ".join(name_and_masks)
    else:
        number = split_number[-1]
        masks_number = card_number(number)
        name_and_masks = split_number[0], masks_number
        return " ".join(name_and_masks)


user_type_and_number = str(input())
print(type_card_and_account_number(user_type_and_number))
