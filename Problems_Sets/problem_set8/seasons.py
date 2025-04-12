from datetime import date
import sys , re , inflect
p = inflect.engine()

def main():
    birth = input("Date of Birth: ")
    print(f"{calculate(birth)} minutes")

def calculate(birth):
    match = re.fullmatch( r"\d{4}-\d{1,2}-\d{1,2}" , birth)
    if not match:
        sys.exit("Invalid date")
    year , month , day = birth.split('-')
    days = (date.today() - date(int(year), int(month), int(day) )).days
    return p.number_to_words(days*24*60 , andword="").capitalize()

if __name__ == "__main__":
    main()
