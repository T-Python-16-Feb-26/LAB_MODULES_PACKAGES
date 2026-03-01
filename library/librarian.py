def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }


def remove_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    del library[isbn]


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    if library[isbn]["available"] == False:
        print("Book is not available.")
        return

    library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    library[isbn]["available"] = True


def display_books(library):
    for isbn, book in library.items():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")