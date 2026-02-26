def add_book(library: dict, title: str, author: str, isbn: str) -> dict:
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists in the library.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

def remove_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist.")
        return

    del library[isbn]

def check_out_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist.")
        return

    if not library[isbn]["available"]:
        print(f"Book with ISBN {isbn} is already checked out.")
        return

    library[isbn]["available"] = False

def return_book(library: dict, isbn: str):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist.")
        return

    library[isbn]["available"] = True

def display_books(library: dict):
    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(f"{book['title']} by {book['author']} "
              f"(ISBN: {book['isbn']}) - {status}")