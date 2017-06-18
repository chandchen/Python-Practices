import random
import string


def build_code(number, length):
    """
    Generate activation codes none repetitive.
    :param number: totally numbers of code
    :param length: length of each code
    :return: a list with codes we need
    """
    result = []
    # source = list(string.ascii_uppercase)
    # source.extend(str(x) for x in range(0, 10))
    source = list(string.ascii_uppercase + string.digits)

    while len(result) < number:
        code = ''
        for i in range(length):
            code += random.choice(source)
        if code in result:
            pass
        else:
            result.append(code)

    return result

active_code = build_code(10, 18)
for each in active_code:
    print(each)
