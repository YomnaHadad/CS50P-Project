import re

def main():
    print(count(input("Text: ")))

def count(s):
    match = re.findall( r"\bum[^A-z*]|um$" , s , re.IGNORECASE)
    return len(match)

if __name__ == "__main__":
    main()

