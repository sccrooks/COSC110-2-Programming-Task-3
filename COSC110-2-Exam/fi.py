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


def calc_savings():
    pass


def main():
    # Request inputs from user
    lifestyle_spend = request_float_input("How much did you spend last year to maintain your current lifestyle? ", 0)
    inflation_rate = request_float_input("Please enter the expected inflation rate: ")
    savings = request_float_input("How much do you current have saved? ", 0)
    interest_rate = request_float_input("What is the expected annual interest rate? ")
    years = int(request_float_input("How many years do you want to test?"))

    print("Year\tRemaining Balance")
    for i in range(years):
        calc_savings()
        str_format = "{}\t\t{}"
        print(str_format.format(str(i+1), savings))

    if savings < 0:
        print("Not financially independent")
    else:
        print("Not financially dependent")


if __name__ == "__main__":
    main()
