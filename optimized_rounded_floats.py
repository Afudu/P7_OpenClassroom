import csv
import time
import math

"""
Note:
This script contains another version of “optimized.py”, in which the values of the costs which are floats 
with 2 decimal values are rounded down, as keeping them as such will return a TypeError 
on the evaluation of the remaining cost (in line 82). List indices must be integers or slices, not float.
Ex: If dataset = [1.01, 2.04], then dataset[2 - dataset[1]] will raise a TypeError.

To prevent this error, the values of the costs are rounded up or down with round() function.
"""


def get_initial_dataset(csv_file):
    """ This function reads a csv file with initially 3 columns (name, cost, and profit(%)),
    converts its data into a list and adds a column for the return on investment."""
    shares = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            name = row[0]
            cost = float(row[1])
            profit = float(row[2]) / 100
            roi = profit * cost
            shares.append({"name": name, "cost": cost, "profit": profit, "return_on_investment": roi})
    return shares


def get_cleaned_dataset(csv_file):
    """ This function reads a dataset in a csv file with initially 3 columns (name, cost, and profit(%)),
    then returns a cleaned data with a column of return on investment calculated and added."""
    cleaned_data = []
    with open(csv_file, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            name = row[0]
            # since the prices in the sienna files are floats with 2 decimal values, and keeping them as such
            # will return a TypeError as the evaluation of the remaining cost will be a float,
            # and list indices must be integers or slices, not float.
            # round() function rounds a number to the nearest whole number.
            cost = round(float(row[1]))
            # The math.ceil() method rounds a number up to the nearest whole number
            # cost = math.ceil(float(row[1]))
            # math.floor() method rounds a number down to the nearest whole number
            # cost = math.floor(float(row[1]))
            profit = float(row[2]) / 100
            return_on_investment = profit * cost
            if cost > 0 and profit > 0:
                cleaned_data.append({"name": name, "cost": cost, "profit": profit, "value": return_on_investment})
    return cleaned_data


def calculate_actual_total_cost(original_list, share_list):
    """calculates the actual sum of the costs of the returned share_list"""
    total_cost = sum(s['cost'] for s in original_list if s['name'] in share_list)
    return round(total_cost, 2)


def calculate_actual_total_return(original_list, share_list):
    """calculates the actual sum of returns of the returned share_list"""
    total_return_on_investment = sum(s['return_on_investment'] for s in original_list if s['name'] in share_list)
    return round(total_return_on_investment, 2)


def get_sienna_solution_values(text_file):
    """ Reads and returns the Sienna-solution-text-files data (list of shares bought, total cost and return amount)
    in order to compare them with the results of the optimized function. """
    with open(text_file, 'r', encoding='UTF-8') as file:
        lines = [line.strip() for line in file]
        shares = [line[:10] for line in lines if line.startswith('Share')]
        total_cost = [line[12:] for line in lines if line.startswith('Total cost: ')]
        total_return = [line[8:] for line in lines if line.startswith('Profit: ')] or \
                       [line[14:] for line in lines if line.startswith('Total return: ')]
    return shares, total_cost, total_return


def optimized_dynamic(max_cost, dataset):
    """Function that returns the maximum return value and best combination of share values for a budget of 'max_cost'
    using dynamic programing.
    This function has time complexity = max_cost * len(dataset).
    """

    # We create a matrix (table) where the rows are the shares,
    # and the columns are the max_weight amounts.
    # Then we initialize the table with zeros.
    items = len(dataset)
    table = [[0 for x in range(max_cost + 1)] for y in range(items + 1)]

    # 1st: iterate over rows = dataset --> height
    for i in range(1, len(dataset) + 1):
        # 2nd: iterate over columns = max_costs --> width
        for max_cost_i in range(1, max_cost + 1):
            # check whether the item at row[index]
            # costs more than the cost at column[max_cost_i]
            if dataset[i - 1]['cost'] > max_cost_i:
                # if so, table[index] value in that column is the value above = table[index - 1]
                table[i][max_cost_i] = table[i - 1][max_cost_i]
                # continue
            # else, if item at row[index] costs less than or equal to the cost at column[max_weight_i]
            # Choose the option that gives the maximum value
            else:
                # ==> prior_value = value above
                prior_value = table[i - 1][max_cost_i]
                # ==> new_option_best is value of current item + val of remaining weight
                new_best = dataset[i - 1]['value'] + table[i - 1][max_cost_i - dataset[i - 1]['cost']]
                # table[index] value = max between prior_value and new_option_best
                table[i][max_cost_i] = max(prior_value, new_best)

    # Initialize selected_shares and total_cost
    selected_shares = []
    total_cost = 0

    # After computing the entire table,the last value is the maximum returned value.
    max_return = table[items][max_cost]

    # i = rows of the table, j = columns
    i = items
    j = max_cost

    # As long as there are rows and columns to iterate over
    while i > 0 and j > 0:
        # Starting from the bottom-right corner of the table:
        # If the value at row[i] is different
        # from the value above row[i-1], then we know the [i-1]th item was selected.
        # We add the share to the list of selected shares, increment the total cost,
        # then move to previous cell in the table.
        if table[i][j] != table[i - 1][j]:
            selected_shares.append(dataset[i - 1]['name'])
            total_cost += dataset[i - 1]['cost']
            j -= dataset[i - 1]['cost']
        i -= 1
    selected_shares.reverse()
    return max_return, total_cost, selected_shares


# Driver code
if __name__ == '__main__':
    # Initialize max_cost and datasets.
    # since the costs are multiplied by 100 to convert them into integers, we multiply the max_cost also by 100
    # then we divide the results displayed by 100 to get the accurate values.
    MAX_COST = 500
    DATASETS = {'Initial dataset': ['data/initial_dataset.csv'],
                'Sienna dataset 1': ['data/dataset1_Python+P7.csv', 'data/solution1_Python+P7.txt'],
                'Sienna dataset 2': ['data/dataset2_Python+P7.csv', 'data/solution2_Python+P7.txt']
                }
    for k, v in DATASETS.items():

        # extract the data
        original_dataset = get_initial_dataset(v[0])
        cleaned_dataset = get_cleaned_dataset(v[0])

        # compile results & calculate execution time
        start_time = time.time()
        best_return_value, best_total_cost, best_shares = optimized_dynamic(MAX_COST, cleaned_dataset)
        end_time = time.time()

        # calculate actual total cost and return for selected_shares
        actual_total_cost = calculate_actual_total_cost(original_dataset, best_shares)
        actual_total_return = calculate_actual_total_return(original_dataset, best_shares)

        # display results
        print("")
        print(f'***** Optimized solution results - {k} *****')
        # we divide the results by 100 to get the accurate values
        print(f'Budget: {MAX_COST}€')
        print(f'Best combination of shares: {best_shares}')
        print(f'Total cost: {round(best_total_cost, 2)}€')
        print(f'Total return: {round(best_return_value, 2)}€')
        print(f'Execution time: {end_time - start_time:.4f} seconds')
        print("")
        print(f'   Actual total cost: {actual_total_cost}')
        print(f'   Actual total return: {actual_total_return}')

        # Display previous solutions for Sienna datasets.
        if not k == 'Initial dataset':
            sienna_shares, sienna_total_cost, sienna_total_return = get_sienna_solution_values(v[1])
            print('---------------')
            print(f"Sienna's choices: \n"
                  f"  Shares bought: {sorted(sienna_shares)}\n"
                  f"  Total cost: {sienna_total_cost[0]} \n"
                  f"  Total return: {sienna_total_return[0]} \n"
                  f"  Bought by sienna but not in Optimized: {[x for x in sienna_shares if x not in best_shares]} \n"
                  f"  In Optimized but not bought by Sienna: {[x for x in best_shares if x not in sienna_shares]}")
        print("****************************************************************")
