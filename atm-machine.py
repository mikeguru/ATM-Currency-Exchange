# The Coin Dispenser must determine the optimal
# coin combination for a given amount of money.
#
# For instance, if the input is: 99,
# the change should be: 3 quarters, 2 dimes, and 4 pennies.
#
# The change amount should be represented as a
# simple list of four integers, indicating the number of
# quarters, dimes, nickels, and pennies.
#
# For instance, if the input is: 99
# the return value should be [3, 2, 0, 4]

# Wen Jiang

class CoinDispenser:

    def make_change(self,amount):
        
        CoinDisp=CoinDispenser()

        possible_coins  = [0,0,0,0]
        quarters=0
        dimes=0
        cents=0
        nickels=0
        pennys=0

        if amount >= 25:
            quarters = amount / 25
            amount=amount % 25
            CoinDisp.possible_coins =[int(quarters),int(dimes),int(nickels),int(pennys)]

        if amount >= 10:
            dimes = amount/10
            amount=amount % 10 
            CoinDisp.possible_coins =[int(quarters),int(dimes),int(nickels),int(pennys)]

        if amount >= 5:
            nickels = amount /5
            amount=amount % 5
            CoinDisp.possible_coins =[int(quarters),int(dimes),int(nickels),int(pennys)]

        if amount > 0:
            pennys = amount
            CoinDisp.possible_coins =[int(quarters),int(dimes),int(nickels),int(pennys)]

        return(CoinDisp.possible_coins)

    possible_coins = [25, 10, 5, 1]
