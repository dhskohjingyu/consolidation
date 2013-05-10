def generate_check_digit(nric):
    if (nric.isdigit() and len(nric) == 7) or (len(nric) == 8 and nric[1::].isdigit()):
        weight = [2, 7, 6, 5, 4, 3, 2]
        alphabet = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'Z', 11:'J'}

        total_sum = 0
        nric_formatted = nric

        if len(nric) == 8:
            nric_formatted = nric[1::]

        for i in range(0, len(nric_formatted)):
            value = int(nric_formatted[i])

            total_sum += value * weight[i]

        check_digit = 11 - (total_sum % 11)

        return alphabet[check_digit]
    else:
        print("Invalid NRIC")

def check_nric(nric):
    check_digit = nric[-1]

    return check_digit == generate_check_digit(nric[0:-1])

print(check_nric('S9500129G'))
print(check_nric('S9500129E'))
