import csv
from itertools import combinations as comb
import time

"""
Project brief - Part 1: create “bruteforce.py” 
- the program needs to read a file containing information about shares,
explore all the possible combinations, and display the best investment.
list of limitations:
   Each share can only be bought once.
   We cannot buy a fraction of a share.
   We can spend at most 500 euros per client.
"""

MAX_COST = 500
INITIAL_DATASET = 'data/initial_data.csv'


def convert_csv_to_list(csv_file):
    shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            shares.append((
                row[0],
                float(row[1]),
                float(row[2])
            ))
    return shares


def calculate_total_cost(share_list):
    """calculates the sum of the costs in column of the list"""
    total_cost = sum(s[1] for s in share_list)
    return total_cost


def calculate_total_return(share_list):
    """calculates the sum of returns of the list = cost by profit"""
    total_return_on_investment = sum(s[1] * s[2] for s in share_list)
    return total_return_on_investment


def bruteforce_shares(csv_file, max_cost):
    """
    The function reads in a CSV file containing share data, loops over the list, uses
    itertools.combinations to generate all possible combinations of shares costing less or equal to max_cost,
    then calculates the best cost, return and shares.
    Algorithm time complexity: O(n*n!)
    """
    best_cost = 0
    best_return = 0
    best_shares = []

    # convert csv_file to list of tuples
    share_list = convert_csv_to_list(csv_file)

    # Try out all possible i combinations of shares
    for i in range(1, len(share_list) + 1):
        for combination in comb(share_list, i):
            total_cost = calculate_total_cost(combination)
            if total_cost <= max_cost:
                total_return = calculate_total_return(combination)
                if total_return > best_return:
                    best_return = total_return
                    best_shares = combination
                    best_cost = total_cost
    # Return the best cost, return, and combination of shares
    return best_cost, best_return, best_shares


# compile results & calculate execution time
start_time = time.time()
best_c, best_r, best_s = bruteforce_shares(INITIAL_DATASET, MAX_COST)
end_time = time.time()

# display results
print("")
print("*********Results - Initial Dataset***********")
print("Budget:", "€", MAX_COST)
print(f'Best combination of shares({len(best_s)}): {[best[0] for best in best_s]}')
print("Total cost:", "€", best_c)
print("Total return value:", "€", round(best_r, 2))
print("")
print(f'Execution time: {end_time - start_time:.4f} seconds')
# Execution time: ~ 2.2 seconds - above requirement.
