#Paula Manese
#CFG-FULL STACK
#Task 2
#Question 3

# Write a program that simulates a lottery. The program should have a list of seven
# numbers that represent a lottery ticket. It should then generate seven random
# numbers. After comparing the two sets of numbers, the program should output a
# prize based on the number of matches:


import random
my_number = [1,2,7,8,39,44, 45]
winning_number =[]
price = ['£20','£40','£100','£10,000','£1,000,000']

price_index =[3,4,5,6,7]
winning_number=random.sample(range(1, 45), 7)
winning_number.sort()
new_list = list(set(my_number).intersection(winning_number))

i = len(new_list)
print('You got ',i,' number/s')

if i > 2:
    index1 =price_index.index(i)
    print('You won ',price[index1])
else:
    print('Your price is £0')
