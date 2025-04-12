import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.fullmatch(r"(\d\d?):?(\d\d)? (?P<start>AM|PM) to (\d\d?):?(\d\d)? (?P<end>AM|PM)" , s)
    if not match:
        raise ValueError

    if (time_validation(match.group(1) , match.group(2)) and time_validation(match.group(4) , match.group(5))):
        starting = edit_time(match.group(1) , match.group(2) , match.group("start"))
        ending = edit_time(match.group(4) , match.group(5) , match.group("end"))
        return starting + " to " + ending
    else:
        raise ValueError

def edit_time(hour , minute , time):
    minute = minute if minute else "00"
    if time == "AM":
        if hour == "12":
            return "00:" + minute
        else:
            return f"{int(hour):02}:" + minute
    else:
        if hour == "12":
            return "12:" + minute
        else:
            return str(int(hour)+12)+ ':' + minute

def time_validation(hour , minute):
    return ((minute == None or int(minute) <=59 ) and ( int(hour) <= 12))

if __name__ == "__main__":
    main()
