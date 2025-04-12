def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6 >= len(s) >= 2:
        if s.isdecimal():     # only numbers
            return False
        for char in s:
            if char in ['!' , '?' , ' ' , '.' ]:
                return False
        return check(s)
    return False

def check(s):
    if s.isalpha():
        return True
    i = 0
    while i<len(s) and s[i].isalpha() :
        i+=1
    if s[i] == '0':
        return False
    for j in range(i , len(s)):
        if s[j].isalpha():
            return False
    return True
main()
