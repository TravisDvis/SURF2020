
def floatExceptionHandle(string_question):
    while True:
        try:
            x = float(input(string_question))
            break
        except ValueError:
            print("You didn't enter a valid value. Try again.")
    return x