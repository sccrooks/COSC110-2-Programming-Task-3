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
            # Get input from user.
            input_num = float(input(message))

            # Ensure entered value is within bounds.
            if minimum is not None and input_num < minimum:
                print("Invalid input. Please enter a float of at least " + str(minimum) + ".")
            elif maximum is not None and input_num > maximum:
                print("Invalid input. Please enter a float of at least " + str(maximum) + ".")
            else:
                # If everything is valid return inputted value
                return input_num
        except:
            print("Invalid input. Please enter an integer")


def request_int_input(message: str, minimum: int = None, maximum: int = None) -> int:
    """
    get_int_input requests an integer input from the
    user of a minimum value, specified by minimum. And a maximum value
    which is specified by maximum.

    :param message: The message presented to the user
    :param minimum: Minimum allowed input
    :param maximum: Maximum allowed input
    :return: int
    """
    while True:
        try:
            # Get input from user.
            input_num = int(input(message))

            # Ensure entered value is within bounds.
            if minimum is not None and input_num < minimum:
                print("Invalid input. Please enter an integer of at least " + str(minimum) + ".")
            elif maximum is not None and input_num > maximum:
                print("Invalid input. Please enter an integer of at least " + str(maximum) + ".")
            else:
                # If everything is valid return inputted value
                return input_num
        except:
            print("Invalid input. Please enter an integer")


def main():
    # Request inputs from user
    lifestyle_spend = request_int_input("How much did you spend last year to maintain your current lifestyle? ", 0)
    inflation_rate = request_float_input("Please enter the expected inflation rate: ")
    savings = request_int_input("How much do you currently have saved? ", 0)
    interest_rate = request_float_input("What is the expected annual interest rate? ")
    years = request_int_input("How many years do you want to test?", 1)

    print("Year\tRemaining Balance")
    for i in range(years):
        # Calc lifestyle spending rate:
        lifestyle_spend += lifestyle_spend * inflation_rate

        # Calculate savings
        savings -= lifestyle_spend

        # Calc interest on savings:
        savings += savings * interest_rate

        str_format = "{}     \t{}"
        print(str_format.format(str(i + 1), round(savings, 2)))

        # If the savings are negative, notify user and exit.
        if savings < 0:
            print("Not financially independent")
            return

    if savings < 0:
        print("Not financially independent")
    else:
        print("Financially dependent")


if __name__ == "__main__":
    main()
