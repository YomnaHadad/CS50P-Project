import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        cnt = 0
        with open(sys.argv[1]) as file:
            for row in file.readlines():
                if not (row.isspace() or row.lstrip().startswith('#')):
                    cnt += 1
        print(cnt)
    except FileNotFoundError:
        sys.exit("File does not exist")
