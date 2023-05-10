import csv
import time

"""
This script contains the implementation of Part2 of the Project Brief: create “optimized.py”, 
the optimized version of the bruteforce.py script.
"""


def get_cleaned_data(csv_file):
    """ This function reads a dataset in a csv file with initially 3 columns (name, cost, and profit(%)),
    then returns a cleaned data (without negative costs) with a column of return on investment calculated and added."""
    cleaned_data = []
    with open(csv_file, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            name = row[0]
            # With the costs that float-points with 2 decimal values in the two old datasets:
            # dataset1_Python+P7.csv and dataset2_Python+P7.csv
            # i/ using them as such will return a TypeError on the evaluation of the remaining cost (in line 73).
            # Ex: If Costs = [1.01, 2.04], then Costs[2 - Costs[1]] will raise a TypeError.
            # ii/ and rounding them up or down will lead to inaccurate results.
            # To get accurate results and prevent TypeErrors, we multiply the costs by 100 to convert them into integers,
            # then we divide the results by 100.
            cost = int(float(row[1]) * 100)
            profit = float(row[2]) / 100
            return_on_investment = profit * cost
            if cost > 0 and profit > 0:
                cleaned_data.append({"name": name, "cost": cost, "profit": profit, "value": return_on_investment})
    return cleaned_data


def get_sienna_solution_values(text_file):
    """ Reads and returns the Sienna-solution-text-files in data/ folder."""
    with open(text_file, 'r', encoding='UTF-8') as file:
        lines = [line.strip() for line in file]
        shares = [line[:10] for line in lines if line.startswith('Share')]
        total_cost = [line[12:] for line in lines if line.startswith('Total cost: ')]
        total_return = [line[8:] for line in lines if line.startswith('Profit: ')] or \
                       [line[14:] for line in lines if line.startswith('Total return: ')]
    return shares, total_cost, total_return


def optimized_dynamic(max_cost, dataset):
    """Function that returns the best combination of shares and their total cost and profits for a budget of 'max_cost'
    using dynamic programing.
    This function has time and space complexity = max_cost * len(dataset).
    """

    # We create a matrix (table) where the rows are the shares,
    # and the columns are the max_weight amounts.
    # Then we initialize the table with zeros.
    items = len(dataset)
    table = [[0 for x in range(max_cost + 1)] for y in range(items + 1)]

    # 1st: iterate over rows = dataset --> height
    for index in range(1, len(dataset) + 1):
        # 2nd: iterate over columns = max_costs --> width
        for max_cost_i in range(1, max_cost + 1):
            # check whether the item at row[index]
            # costs more than the cost at column[max_cost_i]
            if dataset[index - 1]['cost'] > max_cost_i:
                # if so, table[index] value in that column is the value above = table[index - 1]
                table[index][max_cost_i] = table[index - 1][max_cost_i]
                # continue
            # else, if item at row[index] costs less than or equal to the cost at column[max_weight_i]
            # Choose the option that gives the maximum value
            else:
                # ==> prior_value = value above
                prior_value = table[index - 1][max_cost_i]
                # ==> new_option_best is value of current item + val of remaining weight
                new_best = dataset[index - 1]['value'] + table[index - 1][max_cost_i - dataset[index - 1]['cost']]
                # table[index] value = max between prior_value and new_option_best
                table[index][max_cost_i] = max(prior_value, new_best)

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
    MAX_COST = 500 * 100
    DATASETS = {'Initial dataset': ['data/initial_dataset.csv'],
                'Sienna dataset 1': ['data/dataset1_Python+P7.csv', 'data/solution1_Python+P7.txt'],
                'Sienna dataset 2': ['data/dataset2_Python+P7.csv', 'data/solution2_Python+P7.txt']
                }
    for k, v in DATASETS.items():

        # extract the data
        cleaned_dataset = get_cleaned_data(v[0])

        # compile results & calculate execution time
        start_time = time.time()
        best_return_value, best_total_cost, best_shares = optimized_dynamic(MAX_COST, cleaned_dataset)
        end_time = time.time()

        # display results
        print("")
        print(f'***** Optimized solution results - {k} *****')
        # we divide the results by 100 to get the accurate values
        print(f'Budget: {MAX_COST / 100}€')
        print(f'Best combination of shares: {best_shares}')
        print(f'Total cost: {round(best_total_cost / 100, 2)}€')
        print(f'Total return: {round(best_return_value / 100, 2)}€')
        print("")
        print(f'Execution time: {end_time - start_time:.4f} seconds')

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
