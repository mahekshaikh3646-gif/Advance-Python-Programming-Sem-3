# Experiment No. 6

# Title: 0/1 Knapsack Problem using Dynamic Programming
#
# Aim:
# To find the maximum profit that can be obtained
# without exceeding the given weight capacity.
#
# In 0/1 Knapsack, each item can either be:
# 0 -> Not selected
# 1 -> Selected completely
# We cannot take a part of an item.

#
# BOTTOM-UP APPROACH
#

# Function to solve the Knapsack problem using Bottom-Up DP
def knapsack_bottom_up(weights, profits, capacity):

    # Find the number of items
    n = len(weights)

    # Create a DP table with:
    # Rows number of items
    # Columns different bag capacities
    # Initially, all values are 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Go through each item one by one
    for i in range(1, n + 1):

        # Check every possible capacity from 1 to given capacity
        for w in range(1, capacity + 1):

            # Check if the current item's weight fits in the bag
            if weights[i - 1] <= w:

                # Case 1: Include the current item
                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                # Case 2: Do not include the current item
                exclude = dp[i - 1][w]

                # Select the option which gives more profit
                dp[i][w] = max(include, exclude)

            else:

                # If the item is too heavy, we cannot include it
                # So we use the answer from the previous item
                dp[i][w] = dp[i - 1][w]

    # The last cell contains the maximum possible profit
    return dp[n][capacity]


#
# TOP-DOWN APPROACH
#

# Function to solve the Knapsack problem using Top-Down DP
def knapsack_top_down(weights, profits, n, capacity, memo):

    # Base condition:
    # If there are no items or capacity is 0,
    # the maximum profit is 0
    if n == 0 or capacity == 0:
        return 0

    # Check if this problem has already been solved
    if memo[n][capacity] != -1:

        # Return the already stored answer
        return memo[n][capacity]

    # Check if the current item can fit in the bag
    if weights[n - 1] <= capacity:

        # Case 1: Include the current item
        include = profits[n - 1] + knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        # Case 2: Do not include the current item
        exclude = knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity,
            memo
        )

        # Store the maximum of the two choices
        memo[n][capacity] = max(include, exclude)

    else:

        # If the item is too heavy, we cannot include it
        # So we solve the problem without this item
        memo[n][capacity] = knapsack_top_down(
            weights,
            profits,
            n - 1,
            capacity,
            memo
        )

    # Return the stored answer
    return memo[n][capacity]


#
# MAIN PROGRAM
#

# List of weights of the items
weights = [2, 3, 4, 5]

# List of profits of the items
profits = [3, 4, 5, 6]

# Maximum capacity of the bag
capacity = 5

# Find the number of items
n = len(weights)


#
# Call Bottom-Up function
#

# Find maximum profit using Bottom-Up approach
bottom_up_result = knapsack_bottom_up(weights, profits, capacity)

# Display the result
print("Maximum Profit using Bottom-Up:", bottom_up_result)


#
# Call Top-Down function
#

# Create a memoization table.
# -1 means the subproblem has not been calculated yet.
memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Find maximum profit using Top-Down approach
top_down_result = knapsack_top_down(
    weights,
    profits,
    n,
    capacity,
    memo
)

# Display the result
print("Maximum Profit using Top-Down:", top_down_result)


#
# Time and Space Complexity
#

# Time Complexity:
# O(n x capacity)
# Because the DP table contains n x capacity states
# and each state is calculated only once.

# Space Complexity:
# O(n x capacity)
# Because a 2D DP table is used to store the results.
