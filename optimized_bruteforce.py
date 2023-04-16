import csv
import itertools
import time

"""
Part 2: Algorithm Optimization of “optimized.py” + slide deck
Execution time should be less than a 1 second.
"""


def convert_csv_to_list(csv_file):
    shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            shares.append((row[0], float(row[1]), float(row[2])))
    return shares


def calculate_total_cost(share_list):
    """calculates the sum of the costs in column of the list"""
    total_cost = sum(s[1] for s in share_list)
    return total_cost


def calculate_total_return(share_list):
    """calculates the sum of returns of the list = cost by profit"""
    total_return_on_investment = sum(s[1] * s[2] for s in share_list)
    return total_return_on_investment


def optimize_shares(csv_file, max_cost):
    """
    The function reads in a CSV file containing share data, loops over the list, uses
    itertools.combinations to generate all possible combinations of shares, then calculates
    the best costs, returns and shares.
    Algorithm time complexity: O(n*n!)
    """
    # max_cost = 500
    best_shares = []
    best_return = 0

    # convert csv_file to list of tuples
    shares = convert_csv_to_list(csv_file)

    # Try out all possible combinations of shares
    for i in range(1, len(shares) + 1):
        for combination in itertools.combinations(shares, i):
            total_cost = calculate_total_cost(combination)
            if total_cost <= max_cost:
                total_return = calculate_total_return(combination)
                if total_return > best_return:
                    best_return = total_return
                    best_shares = combination
    # Return the best combination
    return best_return, best_shares


start_time = time.time()
print(optimize_shares('data/initial_data.csv', 500))
end_time = time.time()
print("")
print(f'Execution time: {end_time - start_time:.4f} seconds')
# Execution time: 1.9236 seconds - well above requirement.
