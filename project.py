import re , random , csv

ordered = []  ; book_in_demand = []

def main():
    print("---Welcome to our Bookstore---")
    name = input("What's your name? ")
    print(f"Hello, {name}")
    while True:
        try:
            need = input(
                ''' press 1 : if you're looking for a sepcific book.
 press 2 : if you need a suggestion.
'''
           )
            if need == "1":
                ordering(need)
            elif need == "2":
                suggest(need)
            break
        except:
            pass

    email = input("Enter your email address, please. ").strip()
    if check_email(email):
        print("We will contact you via your email.")

    print("📚"*25)

    with open("data.csv" , 'a') as wfile , open("data.csv" , 'r') as rfile:
        writer = csv.DictWriter(wfile , fieldnames =["name","ordered","unavailable"])
        if not rfile.read(1):
            writer.writeheader()
        writer.writerow(
            {
                "name":name ,
                "ordered":  ordered ,
                "unavailable" : book_in_demand
            }
        )
        rfile.seek(0)

        user =[] ; ordered_set = set() ; to_provide = set()
        for row in csv.DictReader(rfile):
            user.append(row["name"])
            ordered_set.add(row["ordered"])
            if len(row["unavailable"])>3:
                to_provide.add(row["unavailable"])

    print("Returning data:")
    print(f"We have {len(user)} members in the system.")
    if len(to_provide) >= 1:
        print(f"Books we need to provide: {to_provide}")
    print(f"Ordered Books: {ordered_set}")


def check_email(em):
    while True:
        try:
            if re.search(r"^\w+@\w+\.(com|edu|yahoo)$" , em):
                return True
            else:
                 em = input("Invalid email format, please try again: ").strip()
        except:
            pass

def ordering(need):
    try:
        with open("books.txt", "r") as books_file:
            bookslist = books_file.read().splitlines()
            if need == "1":
                no_of_books = input("Please enter the quantity of books you wish to order: ")

                for _ in range(int(no_of_books)):
                    book = input("Please enter the book's title: ").lower().strip()
                    if book in bookslist:
                        ordered.append(book)
                        print("The book is available")
                    else:
                        book_in_demand.append(book)
                        print(f"Sorry, '{book}' isn't available , we will provide it very soon.")
                return True

    except FileNotFoundError:
        return "File does not exist"

def suggest(need):
    try:
        with open("books.txt") as books_file:
            books = books_file.read().splitlines()
            if need == "2":
                while True:
                    try:
                        book = random.choice(books).title()
                        print(f"our suggestion is: {book}")
                        choice = input( ''' press 1 : if you will order it.
 press 2 : if you need another suggestion.
'''
             )
                        if choice == "1" :
                            ordered.append(book)
                            break
                    except:
                        pass
            return True

    except FileNotFoundError:
        return "File does not exist"

if __name__ == "__main__":
    main()
