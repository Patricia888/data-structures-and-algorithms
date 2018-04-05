def multi_bracket_validation(stringInput):
    """returns boolean, True for balanced brackets, false for not"""
    if type(stringInput) is not str:
        raise ValueError('Input a string!!')

    sharkTooth_counter = 0
    square_counter = 0
    parenthese_counter = 0

    for letter in stringInput:
        if letter is '(':
            parenthese_counter += 1
        elif letter is ')':
            parenthese_counter -= 1
        elif letter is '[':
            square_counter += 1
        elif letter is ']':
            square_counter -= 1
        elif letter is '{':
            sharkTooth_counter += 1
        elif letter is '}':
            sharkTooth_counter -= 1
        else:
            break

    final_counter = parenthese_counter + sharkTooth_counter + square_counter

    if final_counter == 0:
        return True
    else:
        return False
