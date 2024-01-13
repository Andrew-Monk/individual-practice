# Make your own calculator using the terminal and inputs and have it calculate for you.

num_of_int = 0
answer = ''
method = ''
nums_list = []
total = 0

while True:
    while True:
        try:
            # Opening questions
            # when revising eliminate this to where the user can just enter numbers seperated by commas
            # then add the numbers to a list and iterate in the mathematical portion
            print("Hello, I am your personal calculator, how many numbers would you like to enter?")
            num = int(input())

            # using isinstance() to check if num is interger
            if not isinstance(num, int):
                raise ValueError
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
            answer += reply

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
            method += operator

            break

        except ValueError as e:
            print("Error:", e)
            print('Please enter the value: add, subtract, multiply, or divide')
        break

    while True:
        try:
            for i in range(num_of_int):
                print("Please enter your number")
                num = int(input())
                nums_list.append(num)

            if method == 'add':
                total += sum(nums_list)
                print("The sum of your numbers is", total)

            if method == 'subtract':
                for i in nums_list:
                    total -= i
                    print("The difference of your numbers is", total)

            if method == 'multiply':
                for i in nums_list:
                    total *= i
                    print("The product of your numbers is", total)

            if method == 'divide':
                for i in nums_list:
                    total /= i
                    print("The quotient of your numbers is", total)

            break

        except ValueError:
            raise ValueError
    break
