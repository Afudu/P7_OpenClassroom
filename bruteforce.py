import csv
import itertools
import time

"""
This script contains the implementation of Part1 of the Project Brief: create “bruteforce.py”.
Details:
    The program needs to:
     - read a file containing information about shares,
     - explore all the possible combinations, 
     - and display the best investment.
    Constraints:
       - Each share can only be bought once.
       - We cannot buy a fraction of a share.
       - We can spend at most 500 euros per client.
"""
# Constant variables
MAX_COST = 500
DATASET = 'data/initial_dataset.csv'


def convert_csv_to_list(csv_file):
    """ This function reads a csv file with initially 3 columns (name, cost, and profit(%)),
    converts its data into a list and adds a column for the return on investment."""
    shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            name = row[0]
            cost = int(row[1])
            profit = float(int(row[2]) / 100)
            roi = profit * cost
            shares.append({"name": name, "cost": cost, "profit": profit, "return_on_investment": roi})
    return shares


def calculate_total_cost(share_list):
    """calculates the sum of the costs of the share_list"""
    total_cost = sum(s['cost'] for s in share_list)
    return total_cost


def calculate_total_return(share_list):
    """calculates the sum of returns of the share_list"""
    total_return_on_investment = sum(s['return_on_investment'] for s in share_list)
    return total_return_on_investment


def get_share_names(share_list):
    """return the list of share names of the share_list."""
    names = [n['name'] for n in share_list]
    return names


def bruteforce_shares(max_cost, dataset):
    """
    The function reads in a CSV file containing share data, loops over the list, uses
    itertools.combinations to generate all possible combinations of shares less or equal to max_cost,
    then calculates the best cost, return and shares.
    """

    # convert csv_file to list of key/value pairs
    share_list = convert_csv_to_list(dataset)

    best_cost = 0
    best_return = 0
    best_shares = []

    # Try out all possible i combinations of shares
    for i in range(1, len(share_list) + 1):
        for combination in itertools.combinations(share_list, i):
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
best_cost_value, best_return_value, best_shares_list = bruteforce_shares(MAX_COST, DATASET)
end_time = time.time()

# display results
print("")
print("*********Results - Initial Dataset***********")
print(f'Budget: {MAX_COST}€')
print(f'Best combination of shares({len(best_shares_list)}): {get_share_names(best_shares_list)}')
print(f'Total cost: {best_cost_value}€')
print(f'Total return value: {round(best_return_value, 2)}€')
print("")
print(f'Execution time: {end_time - start_time:.4f} seconds')
