chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}
item = input('Please input an item from this choices (white, milk, dark, vegan) :')

keys_list = list(chocolates)
if item in keys_list:
    print(chocolates[item])
else:
    print('Your choice is not available')