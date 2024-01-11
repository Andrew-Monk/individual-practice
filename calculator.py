# Make your own calculator using the terminal and inputs and have it calculate for you
# similar to when asking AI to do math for you.

while True:
    # opening questions

    print("Hello, I am your personal calculator, how many numbers would you like to enter?")
    num_of_int = int(input())

    while True:
        try:
            print('I see you entered', num_of_int, 'is this correct? Please reply with Y or N' )
            reply = str(input()).lower()
            if reply not in ["y", "n"]:
                raise ValueError("Please enter Y or N")

            break

        except ValueError:
            print("Error:", ValueError)

    while True:
        # Begin mathematical functions
        try:
            print('What would you like to do with these numbers? add, subract, multiply or divide?')
            operator = str(input()).lower()
            if operator not in ["add", "subtract", "multiply", "divide"]:
                raise ValueError('Please enter the value add, subtract, multiply, or divide')

            break

        except ValueError:
            print("Error:", ValueError)

# def calculate(response):
#     if response != type(int()):
#         try:
#             print(response, 'is not a valid answer.. please input a valid answer')
