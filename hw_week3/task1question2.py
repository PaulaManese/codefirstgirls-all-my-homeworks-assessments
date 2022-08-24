#Paula Manese
#CFG-FULL STACK
#Task 1
#Question 2

# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

while True:
    try:
        my_money = input("How much money do you have? (Enter numerical value or X to exit): ")
        if my_money == 'X' or my_money == 'x' :
            print("Exiting program!")
            break
        else:
            my_money = float(my_money)
        refundable_cost = 5
        boat_cost = 20 + refundable_cost

        if my_money >= boat_cost:
            print("You can afford the boat hire")
        else:
            print("You cannot afford the boat hire")
        break
    except ValueError:
        print("Please only enter numerical values!")
        continue

