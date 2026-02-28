def add_book(library: dict, title: str, author: str, isbn: str):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists in the library.")
        return
    library[isbn] = {"title": title, "author": author, "isbn": isbn, "available": True}


def remove_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist in the library.")
        return
    library.pop(isbn)


def check_out_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist in the library.")
        return
    if not library[isbn]["available"]:
        print(f"Book with ISBN {isbn} is not available.")
        return
    library[isbn]["available"] = False


def return_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist in the library.")
        return
    library[isbn]["available"] = True


def display_books(library: dict):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()
