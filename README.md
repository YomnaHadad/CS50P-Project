# Bookstore System
#### Video Demo:  https://youtu.be/FsKH8JmYTZk?feature=shared

#### Description:
What is the "Bookstore System" designed for?
- **User usage** :
  - Book ordering
  - Email validation
  - Book recommendation
- **Manager Features**: receive the returning data:
  - Ordered books
  - Unavilable books
  - Number of users in the system

#### Installation
To run this project, you need Python 3.0 or later (Python 3.6 or later is recommended).

#### Features
- **ordering Function** :
  - Asks for the quantity of books they wish to order, one per line, and tells
   them Whether it's available or not according to reading from "books.txt",
   then append this book to a list,
  - if it's available prints:
  ``` print("The book is available")``` and append it to "ordered"

  - if it's not:
  ``` print(f"Sorry, '{book}' isn't available , we will provide it very soon.")```
    and append it to "book_in_demand"

  - raise FileNotFoundError if "books.txt" is not found:
  ```bash
    except FileNotFoundError:
    return "File does not exist"
  ```
- **suggest Function** :
  - suggest a book by randomly choosing a book from "books.txt" ,
   if the user decide to order it they will have to entre 1
   if not the function will suggest another one
  ```
  book = random.choice(books).title()
  print(f"our recommendation is: {book}")
  choice = input(''' press 1 : if you will order it.
  press 2 : if you need another recommendation ''' ).
  ```
   - raise FileNotFoundError if "books.txt" is not found:
   ``` except FileNotFoundError:    return "File does not exist"  ```

- **check_email Function** :
  - this functions called after calling ( ordering or suggest )
    so it can check if the user typed a valid email ,
    through meeting its expectation by using 're'
    regular expression library.
  - if the user typed a wrong email , it will prompt the user for a
    valid email again
    ``` em = input("Invalid email format, please try again: ").strip  ()
    ```
    so it eventually returns True to enable the system to contact   the user.

- **main Function**
  - prompts the user to choose if they want to ask for a specific book
    or want to get a suggestion
  - informs the user after receiving a valid email :
  ```print("We will contact you via your email.")  ```
  - creates a csv file to store the data for the manager , open the file if
    it's already exist
    - check if the file is empty or not exist , so not to duplicate
      printing the header of the csv file
      ```if not rfile.read(1):
            writer.writeheader()
      ```
    - storing the data each time the program is run
      ```
        writer.writerow(
            {
                "name":name ,
                "ordered":  ordered ,
                "unavailable" : book_in_demand
            }
        ) ```
    - returns the stored data to manager :
      - Ordered books
      - Unavilable books
      - Number of users in the system
    ```
    print("Returning data:")
    print(f"We have {len(user)} members in the system.")
    if len(to_provide) >= 1:
        print(f"Books we need to provide: {to_provide}")
    print(f"Ordered Books: {ordered_set}")
    ```
#### books.txt file
through its included data , the ordering function can check the availability of books , and the suggest function can get a random choice,
and therefore store and return the final data to the developer of the system

#### Testing file
  - testing the 3 main functions in the program other than main function
  - handling the prompting via 'mock'

#### Acknowledgements:
  - [csv module](docs.python.org/3/library/csv.html)
  - [check regular expression](https://regex101.com/)
  - [testing a function with an input call](https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call)

#### Navigate to the project directory:
```cd Final_Project ```

#### Run the project:
run the following command
```python project.py```
> [!WARNING]
> Make sure that "books.txt" is included in the project directory.

#### Run the test of the project:
run the following command
```pytest test_project.py```

#### Author
Yomna Abdelhalim Elhadad - CS50P Project

