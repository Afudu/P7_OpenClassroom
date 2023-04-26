# The knapsack_01_recursive_dp code is contributed by Prosun Kumar Sarkar
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

import csv
import time

MAX_COST = 500
INITIAL_DATA = 'data/initial_data.csv'


# This is the memoization approach of 0 / 1 Knapsack in Python in simple we can say recursion + memoization = DP

def convert_csv_to_list(csv_file):
    """ reads a csv file and converts its data into a list"""
    list_of_shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            list_of_shares.append((row[0], int(row[1]), float(row[2]), float(int(row[1]) * float(row[2]))))
    return list_of_shares


def knapsack_01_recursive_dp(capacity, weights, values, n):
    """
    Recursive function that returns the maximum value that can be put in a knapsack
    of capacity 'capacity', the items with weights 'weights', and values 'values' up to index 'n'.
    This function has exponential time complexity, as it considers all possible combinations of items.
    weights = costs
    values = return
    """
    # base conditions
    if n == 0 or capacity == 0:
        return 0, []

    # memoization
    if table[n][capacity] != -1:
        return table[n][capacity]

    # if weight of the nth item is more than Knapsack capacity,
    # then this item cannot be included in the optimal solution
    if weights[n - 1] > capacity:
        result = knapsack_01_recursive_dp(capacity, weights, values, n - 1)
        table[n][capacity] = result
        return result

    # else, consider two cases: 1) nth item included  or 2) nth item not included
    else:
        # (1) item included: the fn recurses on the n-1 items with the remaining capacity reduced
        #     by the weight of the nth item
        included_value, included_items = knapsack_01_recursive_dp(capacity - weights[n - 1], weights, values, n - 1)
        # value_included += values[n - 1]
        # (2) not included : the function recurses on the n-1 items with the original capacity
        excluded_value, excluded_items = knapsack_01_recursive_dp(capacity, weights, values, n - 1)

        # Choose the option that gives the maximum value
        if included_value + values[n - 1] > excluded_value:
            result = included_value + values[n - 1], included_items + [n - 1]
        else:
            result = excluded_value, excluded_items
        table[n][capacity] = result
        return result


# Driver code
if __name__ == '__main__':

    # extract the data
    share_list = convert_csv_to_list(INITIAL_DATA)

    # calculate the function parameters:
    share_weights = [s[1] for s in share_list]
    share_profits = [s[2] for s in share_list]
    share_values = [s[3] for s in share_list]
    Wmax = MAX_COST
    items = len(share_values)

    # We create a matrix where the share_values are the rows, and the max weights are the columns,
    # then initialize it with -1 at first.
    table = [[-1 for i in range(Wmax + 1)] for j in range(items + 1)]

    # compile results & calculate execution time
    start_time = time.time()
    best_return_value, best_combination_indices = knapsack_01_recursive_dp(Wmax, share_weights, share_values, items)
    end_time = time.time()

    # display results
    print("")
    print("*********Results - Initial Dataset***********")
    print("Budget:", "€", Wmax)
    print("Best combination of shares:", [share_list[i][0] for i in sorted(best_combination_indices)])
    print("Total cost:", "€", (sum(share_weights[i] for i in best_combination_indices)))
    print("Total return:", "€", round(best_return_value, 2))
    print("")
    print(f'Execution time: {end_time - start_time:.4f} seconds')
