
def floatExceptionHandle(string_question,mode):
    #Make sure a proper float value is entered
    while True:
        try:
            x = float(input(string_question))
            if mode == 0 and x > 0.1:
                print("Enter a value of 0.1 or less.")
                continue
            break
        except ValueError:
            print("You didn't enter a valid value. Try again.")
    
    return x