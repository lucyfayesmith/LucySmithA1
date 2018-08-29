"""
Lucy Smith
22.08.2018
BRIEF PROGRAM DETAILS:
Link to program on Github
"""

MENU = """Menu:
    L - List all books
    A - Add new book
    M - Mark a books as completed
    Q - Quit"""


def main():
    print("Reading Tracker 1.0 - by Lucy Smith")
    book_file = open("books.csv", "r")
    books = []

    '''counts total number of books'''
    book_count = 0

    for i in book_file:
        book_count = book_count + 1
    print("{} books loaded from books.csv".format(book_count))

    menu_choice = "B"
    while menu_choice != "Q":

        print(MENU)
        menu_choice = input(">>>").upper()

        if menu_choice == "L":
            page_count = list_books()
            print("You need to read {} pages in {} books.".format(page_count, book_count))
            print("{} books.".format(book_count))

        elif menu_choice == "A":
            add_book()

        elif menu_choice == "M":
            mark_completed(book_count)
            print("{} completed!")

        elif menu_choice != "Q":
            print("Invalid menu choice")

        elif menu_choice == "Q":
            print("{} books saved to books.csv".format(book_count))
            print("Have a nice day!")


def mark_completed(book_count):

    list_books()

    print("Enter the number of a book to mark as completed")
    book_number = input(">>> ")

    while book_number.isdigit() is False:
        print("Invalid input; enter a valid number")
        book_number = input(">>>")

    try:
        while int(book_number) <= 0 or int(book_number) > int(book_count):
            print("Number must be > 0")
            book_number = input(">>>")

    except ValueError:
        print("Number must be > 0")
        book_number = input(">>>")

    return book_number


def list_books():
    books = []
    book_file = open("books.csv", "r")

    page_count = 0

    for line in book_file:
        book = line.strip()
        books.append(book)
        print(book)

        """counts number of pages """
        fields = line.split(',')
        page_count += int(fields[-2])

    book_file.close()

    return page_count, books


def add_book():
    book_file = open("books.csv", "a+")
    error_message = "Input can not be blank"

    book_title = input("Title: ").title()
    while len(book_title) == 0:
        print(error_message)
        book_title = input("Title: ").title()

    book_author = input("Author: ").title()
    while len(book_author) == 0:
        print(error_message)
        book_author = input("Author: ").title()

    page_number = input("Pages: ")
    while page_number == "" or page_number.isalpha() is True:
        print("Invalid input; enter a valid number")
        page_number = input("Pages: ")

    try:
        while int(page_number) <= 0:
            print("Number must be > 0")
            page_number = input("Pages: ")

    except ValueError:
        print("Number must be > 0")

        page_number = input("Pages: ")

    book_file.write("\n{}, {}, {}, r".format(book_author, book_title, page_number))
    print("{} by {}, ({} pages) added to Reading Tracker".format(book_title, book_author, page_number))

    book_file.close()


main()
