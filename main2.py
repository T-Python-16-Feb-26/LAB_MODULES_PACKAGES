from library.librarian import (
    add_book,
    remove_book,
    check_out_book,
    return_book,
    display_books
)

library = {
    "978-0134685991": {
        "title": "Python Basics",
        "author": "John Smith",
        "isbn": "978-0134685991",
        "available": True
    },
    "978-1491912058": {
        "title": "Data Science Handbook",
        "author": "Jake VanderPlas",
        "isbn": "978-1491912058",
        "available": False
    },
    "9780316769174": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "isbn": "9780316769174",
        "available": True
    },
    "9780446310789": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780446310789",
        "available": True
    },
    "9780451524935": {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "available": True
    }
}

menu = """
1- Add Book
2- Remove Book
3- Check Out Book
4- Return Book
5- Display Books
6- Exit
"""
def show_books():
    success, books = display_books(library)
    if not success:
        print("Library is empty.")
        return

    for book in books:
        print(book)

while True:
    choice = input(menu).strip() # Used .strip() to avoid errors from extra spaces

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        success, message = add_book(library, title, author, isbn)
        print(message)

    elif choice == "2":
        isbn = input("Enter ISBN: ").strip()
        success, message = remove_book(library, isbn)
        print(message)

    elif choice == "3":
        isbn = input("Enter ISBN: ").strip()
        success, message = check_out_book(library, isbn)
        print(message)

    elif choice == "4":
        isbn = input("Enter ISBN: ").strip()
        success, message = return_book(library, isbn)
        print(message)

    elif choice == "5":
        show_books()

    elif choice == "6":
        print("Goodbye, come again.")
        break

    else:
        print("Invalid choice. Please try again.")