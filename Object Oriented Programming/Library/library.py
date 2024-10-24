import random

class Books:

    def __init__(self, title, author, category, status, due_date):
        self.__title = title
        self.__author = author
        self.__category = category
        self.__status = status
        self.__due_date = due_date

    def borrow_book(book_ID):
        print(f"{book_ID} is being borrowed.")

    def return_book(book_ID):
        print(f"{book_ID} is being returned.")

    def check_overdue(book_ID):
        overdue = random.choice([True, False])
        if overdue:
            print(f"{book_ID} is overdue.")
        else:
            print(f"{book_ID} is not overdue.")

class Category:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_book():
        print("Added book to category.")

    def remove_book():
        print("Removed book from category.")

    def list_books():
        print("List of books in category.")

    def list_borrowed_books():
        print("List of borrowed books in category.")

class Borrower:

    def __init__(self, name, borrower_type, borrowing_history):
        self.__name = name
        self.__borrower_type = borrower_type
        self.__borrowing_history = borrowing_history

    def borrow_book(borrower_id):
        print(f"{borrower_id} is borrowing a book.")

    def return_book(borrower_id):
        print(f"{borrower_id} is returning a book.")

    def list_borrowed_books():
        print("List of borrowed books.")


class Library:

    def add_book(title, author, category):
        print("Added book to library.")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Category: {category}")

    def remove_book():
        print("Removed book from library.")

    def add_borrower(name, borrower_type):
        print("Added borrower to library.")
        print(f"Name: {name}")
        print(f"Borrower Type: {borrower_type}")

    def remove_borrower():
        print("Removing borrower.")

    def Search_book():
        print("Found book in library.")


class LibraryFacade:

    def borrow_book(self, borrower_id, book_id):
        Books.borrow_book(book_id)
        Borrower.borrow_book(borrower_id)

    def return_book(self, borrower_id, book_id):
        Books.return_book(book_id)
        Borrower.return_book(borrower_id)

    def add_book(self, title, author, category):
        Library.add_book(title, author, category)

    def add_borrower(self, name, borrower_type):
        Library.add_borrower(name, borrower_type)

    def remove_borrower(self, borrower_id):
        Library.remove_borrower(borrower_id)

    def check_overdue(self, book_id):
        Books.check_overdue(book_id)


# main program

facade = LibraryFacade()   # creates a facade object

print()
# add some books ...
facade.add_book("1984", "George Orwell", "Fiction")
print()
facade.add_book("A Brief History of Time", "Stephen Hawking", "Non-Fiction")
print()

# ... and a user
facade.add_borrower("Yuan", "Student")
print()

# borrow a book
facade.borrow_book("BR002","BK004")
print()

# and return one
facade.return_book("BR001","BK002")
print()

# check if a book is overdue
facade.check_overdue("BK001")
print()