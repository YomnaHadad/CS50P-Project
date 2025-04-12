def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))

def convert(fraction):
    while True:
        try:
            X ,Y = fraction.split('/')
            x = int(X) ; y = int(Y)
            if x<=y and y != 0:
                return (x/y)*100
        except (ValueError , ZeroDivisionError):
            raise

def gauge(percentage):
    if  percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()
