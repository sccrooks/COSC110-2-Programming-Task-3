def request_float_input(message: str, minimum: float = None, maximum: float = None) -> float:
    """
    get_float_input requests a float input from the
    user of a minimum value, specified by minimum. And a maximum value
    which is specified by maximum.

    :param message: The message presented to the user
    :param minimum: Minimum allowed input
    :param maximum: Maximum allowed input
    :return: Valid float
    """
    while True:
        try:
            input_num = float(input(message))

            if minimum is not None and input_num < minimum:
                print("Invalid input. Please enter a float of at least " + str(minimum) + ".")
            elif maximum is not None and input_num > maximum:
                print("Invalid input. Please enter a float of at least " + str(maximum) + ".")
            else:
                return input_num
        except:
            print("Invalid input. Please enter an integer")


def main():
    pass


if __name__ == "__main__":
    main()
