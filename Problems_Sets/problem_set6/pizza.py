import sys , csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file ")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        l = []
        with open(sys.argv[1]) as csvfile:
            for row in csv.reader(csvfile):
                l.append(row)
            print(tabulate( l[1:], l[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")
