#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
# Lab 3
#########################################

def change(amount, coins):
    """Returns the minimum amount of coins needed to make up an amount of money. If there are no possible solutions,
    return infinity"""
    if amount == 0:
        return 0
    elif amount > 0 and coins == []:
        return float("inf")
    elif amount < 0:
        return -1 + change(amount + coins[-1], coins[:-1])
    else:
        use = 1 + change(amount - coins[-1], coins)
        lose = change(amount, coins[:-1])
        return min(use, lose)
