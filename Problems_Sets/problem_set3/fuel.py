def main():
    result = Get_Frac()
    if  result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{round(result)}%")

def Get_Frac():
    while True:
        try:
            fraction = input("Fraction: ")
            X ,Y = fraction.split('/')
            x = int(X) ; y = int(Y)
            if x<=y and y != 0:
                return (x/y)*100
        except (ValueError, ZeroDivisionError):
            pass
main()





