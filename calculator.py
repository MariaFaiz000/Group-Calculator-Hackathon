def calculation():
  """
  Calculates the sum of two numbers, using addition, subtraction, 
  multiplication or division.
  """

  while (True):
    """A while loop that continously runs the calculation function"""
    num1 = input("Please enter a number: ")
    """User input"""
    if not num1.isnumeric():
      """Checks the user's input is numeric, if not it will loop back to the start"""
      print("you did not enter a number")

      if input(
          "would you like to perform another calculation? y for yes n for no:  "
      ) == "y":

        print("great. remember to enter a number next time")
        continue
      else:
        print("ok bye")
        break

    operator = input(
        "Please enter  operation you wish to perform +, -, *, /: ")
    """User input"""
    if operator != "+" and operator != "/" and operator != "*" and operator != "-":
      """Checks if the operated inputted is one of four, if not it will loop back to the start"""
      print("invalid operator ")
      if input("would you like to try again. y for yes n for no:  ") == "y":
        """User input, asking if the user wishes to restart the program"""

        print("great. remember to enter a valid operator next time")
        continue
        """Continue simply returns the user to the beginning of the program"""
      else:
        print("ok bye")
        """Prints string and breaks the while loop ending the program"""
        break

    num2 = input("Please enter your second number: ")
    """User input"""
    if not num2.isnumeric():
      """Checks the user's input is numeric, if not it will loop back to the start"""
      print("you did not enter a number")

      if input(
          "would youlike to perform another calculation? y for yes n for no:  "
      ) == "y":

        print("great. remember to enter a number next time")
        continue
      else:
        print("ok bye")
        break

    if operator == "+":
      """If the user inputs + sign the print the following result"""
      print("your answer is ", int(num1) + int(num2))
      if input(
          "would you like to perform another calculation? y for yes n for no:   "
      ) == "y":
        print("great")
      else:
        print("goodbye")
        break

    elif operator == "-":
      """If the user inputs - sign the print the following result"""
      print("Your answer is ", int(num1) - int(num2))
      if input(
          "would you like to perform another calculation? y for yes n for no:  "
      ) == "y":
        print("great")

      else:
        print("goodbye")
      break

    elif operator == "*":
      """If the user inputs * sign the print the following result"""
      print("your answer is ", int(num1) * int(num2))
      if input(
          "would you like to perform another calculation? y for yes; n for no:   "
      ) == "y":
        print("great")
      else:
        print("goodbye")
        break

    elif operator == "/":
      """If the user inputs / sign the print the following result"""
      if num2 == "0":
        """If the number inputted is a 0 then it'll tell them they cannot divide by 0"""
        print("cannot divide by zero")
        if input(
            "would you like to perform another calculation? y for yes n for no:   "
        ) == "y":
          print("great. remember next time dont try to divide by zero")
        else:
          print("ok goodbye")
          break
      else:
        print("your answer is ", float(num1) / float(num2))
        if input(
            "would you like to perform another calculation? y for yes n for no:  "
        ) == "y":
          """User input, asking if the user wishes to restart the program"""
          print("great")
        else:
          print("ok goodbye")
          break

    else:
      print("you entered an invalid operator")
      if input(
          "would you like to perform another calculation? y for yes; n for no:   "
      ) == "y":

        print("great. this time make sure you enter a valid operator.")
      else:
        print("then goodbye")


"""Calls the calculate function"""
calculation()
