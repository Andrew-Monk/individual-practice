# Make your own calculator using the terminal and inputs and have it calculate for you
# similar to when asking AI to do math for you.
num_of_int = 0
reply = None
operator = None
total = 0

while True:
    while True:
        try:
            # Opening questions
            print("Hello, I am your personal calculator, how many numbers would you like to enter?")
            num = int(input())
            # using isinstance() to check if num is interger
            if not isinstance(num, int):
                raise ValueError
            # adding num to num_of_int to access later
            else:
                num_of_int += num

            break

        except ValueError as e:
            print('Error:', e)
            print('Please enter a valid number.')

    while True:
        try:
            print('I see you entered', num_of_int, 'is this correct? Please reply with Y or N' )
            reply = str(input()).lower()
            if reply not in ["y", "n"]:
                raise ValueError

            break

        except ValueError as e:
            print('Error:', e)
            print("Please enter Y or N")

    while True:
        # Begin mathematical functions
        try:
            print('What would you like to do with these numbers? add, subract, multiply or divide?')
            operator = str(input()).lower()
            if operator not in ["add", "subtract", "multiply", "divide"]:
                raise ValueError

            break

        except ValueError as e:
            print("Error:", e)
            print('Please enter the value add, subtract, multiply, or divide')
    break
    # while True:
        # Get numbers
        # find a way to prompt for the amount of nums to be entered, then add them to the list
        # use for loop to loop through list and check values to see if theyre intergers
        # try:
        #     print





# def calculate(response):
#     if response != type(int()):
#         try:
#             print(response, 'is not a valid answer.. please input a valid answer')
