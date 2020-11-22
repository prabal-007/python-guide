from tabulate import tabulate

def print_formate():
    data = {"Name" : ["Jonh","Shreya","Aj","Riti"],
    "Age" : [21,18,18,22],
    "Gender" : ["M","F","M","F"]}
    return tabulate(data, headers="keys", tablefmt="github")

print(print_formate())
