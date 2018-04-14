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
# the return value should be [3, 2, 0, 4].

# Wen Jiang

from machine import CoinDispenser

# Ensure the machine knows all coin denominations
assert [25, 10, 5, 1] == CoinDispenser.possible_coins

# Ensure the machine knows how to make change
dispenser = CoinDispenser()

assert [0,0,0,1] == dispenser.make_change(1)
assert [0,0,0,2] == dispenser.make_change(2)
assert [0,0,0,3] == dispenser.make_change(3)
assert [0,0,0,4] == dispenser.make_change(4)
assert [0,0,1,0] == dispenser.make_change(5)
assert [0,0,1,1] == dispenser.make_change(6)
assert [0,1,0,0] == dispenser.make_change(10)
assert [0,1,0,1] == dispenser.make_change(11)
assert [0,1,1,0] == dispenser.make_change(15)
assert [0,1,1,1] == dispenser.make_change(16)
assert [1,0,0,0] == dispenser.make_change(25)
assert [2,0,0,1] == dispenser.make_change(51)
assert [3,2,0,4] == dispenser.make_change(99)

print("Congratulations!  Your change machine works!")
