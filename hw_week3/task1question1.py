#Paula Manese
#CFG-FULL STACK
#Task 1
#Question 1


# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

while True:
    try:
        user_input = input("Is it raining? Please type Y for Yes, N for No or X for Exit (Y/N/X): ")
        user_input = user_input.upper()
        if user_input == 'Y':
            print("Take an umbrella")
        elif user_input == 'N':
            print("You don't need an umbrella")
        else:
            raise ValueError
        break
    except ValueError:
        print("Please only Enter Y, N or X; Which represents Yes, No, and Exit in respective order")