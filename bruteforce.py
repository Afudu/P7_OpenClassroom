from tabulate import tabulate
# import timeit

# We want the program to try out all the different combinations of shares that fit our constraints,
# and choose the best result because we want to be as transparent as possible.
# Again, the program needs to read a file containing information about shares,
# explore all the possible combinations, and display the best investment.
# list of limitations:
#    Each share can only be bought once.
#    We cannot buy a fraction of a share.
#    We can spend at most 500 euros per client.
# # Start developing a brute force solution and send the Python code to Robin in a file (“bruteforce.py”)
# data = data/initial_data.csv


SHARES = [
    {"name": "Share-1", "cost": 20, "profit": 0.05},
    {"name": "Share-2", "cost": 30, "profit": 0.1},
    {"name": "Share-3", "cost": 50, "profit": 0.15},
    {"name": "Share-4", "cost": 70, "profit": 0.2},
    {"name": "Share-5", "cost": 60, "profit": 0.17},
    {"name": "Share-6", "cost": 80, "profit": 0.25},
    {"name": "Share-7", "cost": 22, "profit": 0.07},
    {"name": "Share-8", "cost": 26, "profit": 0.11},
    {"name": "Share-9", "cost": 48, "profit": 0.13},
    {"name": "Share-10", "cost": 34, "profit": 0.27},
    {"name": "Share-11", "cost": 42, "profit": 0.17},
    {"name": "Share-12", "cost": 110, "profit": 0.09},
    {"name": "Share-13", "cost": 38, "profit": 0.23},
    {"name": "Share-14", "cost": 14, "profit": 0.01},
    {"name": "Share-15", "cost": 18, "profit": 0.03},
    {"name": "Share-16", "cost": 8, "profit": 0.08},
    {"name": "Share-17", "cost": 4, "profit": 0.12},
    {"name": "Share-18", "cost": 10, "profit": 0.14},
    {"name": "Share-19", "cost": 24, "profit": 0.21},
    {"name": "Share-20", "cost": 114, "profit": 0.18}
]

MAX_COST = 500
TABLE_LINES = []


def display_table(list_to_display, headers):
    print(tabulate(list_to_display, headers, tablefmt="simple_grid"))


def calculate_total_cost(share_list):
    cost = sum(s["cost"] for s in share_list)
    return cost


def calculate_total_return(share_list):
    profit = sum(s["cost"] * s["profit"] for s in share_list)
    return profit


# def get_selected_shares(share_list):
#     for i in range(2 ** len(share_list)):  # Generate all possible combinations of shares
#         # Convert the index to binary and pad with zeros
#         binary = bin(i)[2:].zfill(len(share_list))
#         # Create a list of potential shares to buy
#
#         for j in range(len(share_list)):
#             if binary[j] == "1":
#                 selected_shares.append(share_list[j])
#     return selected_shares


def brute_force(share_list, budget):
    best_profit = 0
    best_shares = []
    for i in range(2 ** len(share_list)):  # Generate all possible combinations of shares
        # Convert the index to binary and pad with zeros
        binary = bin(i)[2:].zfill(len(share_list))
        # Create a list of potential shares to buy
        selected_shares = []
        for j in range(len(share_list)):
            # gain = share_list[j]['cost'] * share_list[j]["profit"]
            # share_list[j]['gain'] = gain
            if binary[j] == "1":
                selected_shares.append(share_list[j])
        # Calculate the cost and profit of the selected shares
        cost = calculate_total_cost(selected_shares)
        profit = calculate_total_return(selected_shares)
        # Check if the cost is within the budget and the profit is better than the current best
        if cost <= budget and profit > best_profit:
            best_profit = profit
            best_shares = selected_shares
    return best_profit, best_shares


max_profit, shares_to_buy = brute_force(SHARES, MAX_COST)

print("+++Best combination of shares+++")
for share in shares_to_buy:
    line = share["name"], share["cost"], share["profit"]
    TABLE_LINES.append(line)
# total_line = "Total", calculate_cost(shares_to_buy), round(max_profit, 2)
# TABLE_LINES.append(total_line)
display_table(TABLE_LINES, ['Name', 'Cost', 'Profit'])
print("")
print("Total cost:", calculate_total_cost(shares_to_buy), "eur")
print("Total profit:", round(max_profit, 2), "eur")
