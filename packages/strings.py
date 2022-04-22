import turtle


def palindrome(string, strict=False):
    if strict == False:
        string = string.replace(' ', '').lower()
    temp_string = string[::-1]
    if string == temp_string:
        return True
    return False


def twin_chars(string):
    str_len = len(string)
    i = 0
    while i != str_len:
        if i == str_len - 1 or string[i] != string[i + 1]:
            return False
        i += 2
    return True


def chars_case_rotation(string):
    str_len = len(string)
    i = 0
    if str_len == 0 or str_len == 1:
        return False
    while i != str_len - 1:
        if string[i].isupper() == string[i + 1].isupper():
            return False
        i += 1
    return True


def chars_replace(org_string, string_to_rep1, string_to_rep2):
    temp_str = string_to_rep1
    string_to_rep1 += string_to_rep2
    string_to_rep2 += temp_str
    replacement_rules = org_string.maketrans(string_to_rep1, string_to_rep2)
    return org_string.translate(replacement_rules)


def dragon_curve(number):
    string = ""
    if number == 0:
        return "R"
    replacement_rules = str.maketrans("RL", "LR")
    for i in range(0, number + 1):
        string += "R" + string[::-1].translate(replacement_rules)
        i += 1
    return string


def turtle_lib(number):
    movement = dragon_curve(number)
    movement_duration = len(movement)
    for i in range(0, movement_duration):
        if movement[i] == "R":
            turtle.right(90)
        else:
            turtle.left(120)
        turtle.forward(100)
        i += 1
    turtle.done()
    return 0
