# setup the list and dictionary for programming
menu = ["coffee", "cake", "tea", "cookie"]

stock = {
    "coffee": 23,
    "cake": 56,
    "tea": 78,
    "cookie": 12
}

price = {
    "coffee": 2,
    "cake": 4,
    "tea": 9,
    "cookie": 3
}

total_stock = 0

# loop through the 'stock' and 'price' dictionary, and perform calculation.
# Match items by using menu list as the key in each dictionary.
for i in range(0, len(menu)):
    total_stock += stock[menu[i]] * price[menu[i]]

print("Total stock worth =", total_stock)
