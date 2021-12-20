candy_prices = {'M&M': (1.99, 4),
                'Butterfinger': (1.25, 3),
                'Skittles': (2.99, 5),
                'Snickers': (1.30, 1)}

candy1 = int(input("How many bags of M&M's:"))
if (candy1 > candy_prices["M&M"][1]):
    candy1 = 0
    print("sorry, I can't do that - we don't have enough")
candy2 = int(input("How many bags of Butterfinger's:"))
if (candy2 > candy_prices["Butterfinger"][1]):
    candy2 = 0
    print("sorry, I can't do that - we don't have enough")
candy3 = int(input("How many bags of Skittles's:"))
if (candy3 > candy_prices["Skittles"][1]):
    candy3 = 0
    print("sorry, I can't do that - we don't have enough")
candy4 = int(input("How many bags of Snickers's:"))
if (candy4 > candy_prices["Snickers"][1]):
    candy4 = 0
    print("sorry, I can't do that - we don't have enough")

total_amount = ((candy_prices["M&M"][0] * candy1)
+ (candy_prices["Butterfinger"][0] * candy2)
+(candy_prices["Skittles"][0] * candy3)
+(candy_prices["Snickers"][0] * candy4))
print(f"Your total bill will be: {total_amount: .2f}" )
