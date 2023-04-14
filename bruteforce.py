from tabulate import tabulate
import csv
import time

"""
Project brief
Part 1:“bruteforce.py” - the program needs to read a file containing information about shares,
explore all the possible combinations, and display the best investment.
list of limitations:
   Each share can only be bought once.
   We cannot buy a fraction of a share.
   We can spend at most 500 euros per client.
==>Start developing a brute force solution and send the Python code to Robin in a file (“bruteforce.py”)
"""

MAX_COST = 500
INITIAL_DATA = 'data/initial_data.csv'


def convert_csv_to_list(csv_file):
    """ reads a csv file and converts its data into a list"""
    shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            shares.append((row[0], float(row[1]), float(row[2])))
    return shares


def calculate_total_cost(share_list):
    """calculates the sum of the costs - 2nd column of the list"""
    total_cost = sum(s[1] for s in share_list)
    return total_cost


def calculate_total_return(share_list):
    """calculates the sum of returns of the list = cost by profit"""
    total_return_on_investment = sum(s[1] * s[2] for s in share_list)
    return total_return_on_investment


def brute_force(csv_file, budget):
    """Function reading the shares from a csv file, generate all possible combinations of shares
    then extract the combinations of shares that fit the client constraints.
    Algorithm time complexity: O(2**n) - slow for large values of n but guarantees optimal solution."""

    # initialize variables
    best_return = 0
    best_shares = []

    # get csv file
    share_list = convert_csv_to_list(csv_file)

    # Generate all possible combinations of shares - 2^n
    for i in range(2 ** len(share_list)):
        # Convert the index to binary and pad with zeros
        binary = bin(i)[2:].zfill(len(share_list))
        # Create a list of potential shares to buy
        selected_shares = []
        for j in range(len(share_list)):
            # select shares
            if binary[j] == "1":
                selected_shares.append(share_list[j])
        # Calculate the cost and profit of the selected shares
        total_cost = calculate_total_cost(selected_shares)
        total_return = calculate_total_return(selected_shares)
        # Check if the cost is within the budget and the profit is better than the current best
        if total_cost <= budget and total_return > best_return:
            best_return = total_return
            best_shares = selected_shares
    return share_list, best_return, best_shares


def display_results(initial_list, return_amount, list_to_display):
    """ displays a list using tabulate module"""
    print("Best combination of shares to buy")
    print(tabulate(list_to_display, ['Shares', 'Cost', 'Profit'], tablefmt="simple_grid"))
    print("")
    print("++++++++++Summary+++++++++")
    print("Initial number of shares:", len(initial_list))
    print("Max spending:", MAX_COST, "eur")
    print("Number of shares to buy:", len(list_to_display))
    print("Total cost:", calculate_total_cost(list_to_display), "eur")
    print("Total return:", round(return_amount, 2), "eur")


# display execution time & results
start_time = time.process_time()
shares_list, max_return, shares_to_buy = brute_force(INITIAL_DATA, MAX_COST)
display_results(shares_list, max_return, shares_to_buy)
time_elapsed = (time.process_time() - start_time)
print("")
print('Program Executed in {} seconds'.format(time_elapsed))
# Program Executed in 4.28125 seconds
