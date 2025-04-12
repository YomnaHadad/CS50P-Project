import sys , requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif not float(sys.argv[1]) :
    sys.exit("Command-line argument is not a number")
else:
    try:

        info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rsp = info.json()
        coin = rsp["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
        print(f"${coin:,.4f}")
    except requests.RequestException:
        sys.exit()
