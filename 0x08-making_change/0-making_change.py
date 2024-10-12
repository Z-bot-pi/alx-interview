#!/usr/bin/python3
"""
Module that defines the makeChange function.
"""

def makeChange(coins, total):
    """
    Determines the minimum number of coins required to meet a given total.

    Parameters:
    coins (list): A list of coin denominations.
    total (int): The total amount to be made with coins.

    Returns:
    int: The fewest number of coins needed to meet the total, or -1 if it can't be met.
    """
    if total <= 0:
        return 0

    # Initialize the dp array to store the minimum number of coins for each amount up to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make a total of 0

    # Update the dp array for each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total cannot be made, return -1
    return dp[total] if dp[total] != float('inf') else -1

