allItems = []
finished = 0
order = []
pluralSubstring = ['', 'has']
menu = [
    ['Wings', 'Cookies', 'Spring Rolls'],
    ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    ['Ice Cream', 'Cake', 'Pie'],
    ['Coffee', 'Tea', 'Unicorn Tears']
]
types = [
    'Appetizers',
    'Entrees',
    'Desserts',
    'Drinks'
]


print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
''')

i = 0
for category in types:
    print(category)
    print(len(category) * '_')
    for item in menu[i]:
        print(item)
        allItems.append(item)
    print()
    i += 1

print('''
***********************************
** What would you like to order? **
***********************************
''')

while finished == 0:
    response = input('> ')
    if response == 'quit' or response == 'QUIT' or response == 'q' or response == 'Q':
        finished = 1
    elif response in order:
        order[order.index(response) + 1] += 1

    else:
        order.append(response)
        order.append(1)

    # Switch this out with the else statement immediately above to disable custom orders:
    # elif response in allItems:
    #     order.append(response)
    #     order.append(1)
    # else:
    #     print("Please enter a valid menu item (case sensitive)")

    for item in order:
        if order.index(item) % 2 == 0:
            if order[order.index(item) + 1] > 1:
                pluralSubstring = ['s', 'have']
            if item in allItems:
                print(f'** {order[order.index(item) + 1]} order{pluralSubstring[0]} of {order[order.index(item)]} '
                      f'{pluralSubstring[1]} been added to your meal **')
            else:
                print(f'** Special order{pluralSubstring[0]}: {order[order.index(item)]} '
                      f'x{order[order.index(item) + 1]} {pluralSubstring[1]} been added to your meal **')
            pluralSubstring = ['', 'has']
