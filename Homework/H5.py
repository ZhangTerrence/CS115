#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 5
#########################################

memo_lucas = {}
def fast_lucas(n):
    """Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]"""
    if n in memo_lucas:
        return memo_lucas[n]
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        memo_lucas[n] = fast_lucas(n-1) + fast_lucas(n-2)
        return memo_lucas[n]

memo_change = {}
def fast_change(amount, coins):
    """Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Uses memoization to improve performance."""
    if (amount, tuple(coins)) in memo_change:
        return memo_change[(amount, tuple(coins))]
    elif amount == 0:
        memo_change[(amount, tuple(coins))] = 0
        return 0
    elif amount > 0 and coins == []:
        memo_change[(amount, tuple(coins))] = float("inf")
        return float("inf")
    elif amount < 0:
        memo_change[(amount, tuple(coins))] = -1 + fast_change(amount + coins[-1], coins[:-1])
        return memo_change[(amount, tuple(coins))]
    else:
        use = 1 + fast_change(amount - coins[-1], coins)
        lose = fast_change(amount, coins[:-1])
        memo_change[(amount, tuple(coins))] = min(use, lose)
        return memo_change[(amount, tuple(coins))]


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


