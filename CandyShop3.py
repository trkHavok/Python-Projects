candy_prices = {'M&M': (1.99),
                'Butterfinger': (1.25),
                'Skittles': (2.99),
                'Snickers': (1.30)}
candy1 = input("What is your first item:")
if candy1 not in candy_prices:
    candy_prices[candy1] = 0
    print("Sorry we do not carry that item")
    
candy2 = input("What is your second item:")
if candy2 not in candy_prices:
    candy_prices[candy2] = 0
    print("Sorry we do not carry that item")
price1 = candy_prices.get(candy1)
if price1 == None:
    price1 = 0
price2 = candy_prices.get(candy2)
if price2 == None:
    price2 = 0
candy_cost = price1 + price2
print('To pruchase',candy1, 'and', candy2, 'the cost will be:',float(candy_cost)) 
if price1 + price2 < 2:
    print("Great you stayed in budget!!")
elif 2 < price1 + price2 < 3:
    print("You're almost over budegt!!")
else:
    print("You're over budget buddy!!")