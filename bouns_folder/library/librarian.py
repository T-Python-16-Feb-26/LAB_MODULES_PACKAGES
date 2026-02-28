def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "available": True
        }


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Book not found.")


def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
        else:
            print("Book already checked out.")
    else:
        print("Book not found.")


def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
    else:
        print("Book not found.")


def display_books(library):
    for isbn, book in library.items():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
        
