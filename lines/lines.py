
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]
ext_point_ind = file_name.rfind(".")
ext = file_name[ext_point_ind + 1:]
if ext_point_ind == -1 or ext != "py":
    sys.exit("Not a Python file")

try:
    loc = 0
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            if line != "" and not line.startswith("#"):
                loc += 1
    print(loc)
except FileNotFoundError:
    #print(type(e))
    sys.exit("File does not exist")

