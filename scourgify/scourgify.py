import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
ext_point_ind = file_name.rfind(".")
ext = file_name[ext_point_ind + 1:]
if ext_point_ind == -1 or ext != "csv":
    sys.exit("Could not read", file_name)

try:
    with open(file_name) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        table = []
        for row in reader:
            name = row[headers[0]]
            last, first = name.split(",")
            house = row[headers[1]]
            #print(name, "|", house)
            table.append({"first": first.strip(), "last": last.strip(), "house": house})
except FileNotFoundError:
    sys.exit("File does not exist")

file_name = sys.argv[2]
with open(file_name, "w") as file:
    headers = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(table)


