def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Enter non negative int")
            continue

        if value <= 0:
            print("Enter value which is greater than 0")
            continue
        else:
            break
    return value


def get_nwd(x, y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y

    return get_nwd(y, x % y)


def ask_for_integer_input(number_of_parameters = 2):
    prompt = "Enter argument no."
    values = []
    i = 0
    while i < number_of_parameters:
        values.append(get_non_negative_int(prompt + str(i + 1) + ": "))
        i = i + 1

    return values


def handler(parameters=2):
    values = ask_for_integer_input(parameters)
    if len(values) == parameters:
        print(get_nwd(*values))
    else:
        raise ValueError


handler()
