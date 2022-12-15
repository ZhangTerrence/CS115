###########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 4
###########################################

def knapsack(capacity, itemList):
    """Given a capacity and a list of items each having their own weight and value, returns the maximum value that can
    be taken from the items without their weight exceeding the capacity while also returning the list of items that
    make up that value"""
    if capacity <= 0 or itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        if use[0] + itemList[0][1] > lose[0]:
            return [use[0] + itemList[0][1], [itemList[0]] + use[1]]
        return lose
