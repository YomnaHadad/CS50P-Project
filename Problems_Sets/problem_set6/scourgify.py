import sys , csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as rfile , open(sys.argv[2] , "w") as wfile:
            writer = csv.DictWriter(wfile , fieldnames =["first","last","house"])
            writer.writeheader()
            for line in csv.DictReader(rfile):
                l , f = line['name'].rstrip().split(',')
                writer.writerow(
                    {
                        "first":f.strip() ,
                        "last": l ,
                         "house" : line['house']
                    }
                )

    except FileNotFoundError:
        sys.exit("File does not exist")
