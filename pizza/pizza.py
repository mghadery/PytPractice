import sys
import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
ext_point_ind = file_name.rfind(".")
ext = file_name[ext_point_ind + 1:]
if ext_point_ind == -1 or ext != "csv":
    sys.exit("Not a CSV file")

try:
    with open(file_name) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        table = []
        for row in reader:
            pizza = row[headers[0]]
            small_price = row[headers[1]]
            large_price = row[headers[2]]
            #print (pizza, small_price, large_price)
            table.append([pizza, small_price, large_price])
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")

