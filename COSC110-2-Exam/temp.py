def get_number(prompt, error="Please enter a valid number"):
    """
      Presents the given prompt to the user and reads in a number.
      If an invalid value is entered the given error message
      is displayed and the process repeats.

      Arguments:
      prompt -- The prompt to display to the user
      error -- The error to display if an invalid value is entered
               Defaults to "Please enter a valid number"

      Returns the number entered by the user (as a float)
    """
    while True:
        value_string = input(prompt)
        try:
            return float(value_string)
        except ValueError:
            print(error)
