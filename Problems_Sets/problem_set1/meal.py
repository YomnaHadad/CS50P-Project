def main():
    f_number = convert(input("What time is it? "))
    if  7<= f_number <= 8:
        print("breakfast time")
    elif 12 <= f_number <= 13:
        print("lunch time")
    elif 18 <= f_number <= 19 :
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()



