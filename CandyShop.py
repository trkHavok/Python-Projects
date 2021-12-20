candy_prices = {'M&M': (1.99, 4),
                'Butterfinger': (1.25, 3),
                'Skittles': (2.99, 5),
                'Snickers': (1.30, 1)}
candy1 = input('What is your first item:' )
amount1 = int(input('How many bags of '+candy1+"'s:"))
candy2 = input('What is your second item:')
candy_cost = candy_prices[candy1] + candy_prices[candy2]
print('To pruchase',candy1, 'and', candy2, 'the cost will be:',candy_cost)