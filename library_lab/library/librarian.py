library={}
def add_book(library:dict, title:str, author:str, isbn:str):

    if isbn in library:
        print(f"Book {isbn} : is exists")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }


def remove_book(library:dict, isbn:str):
    if isbn not in library:
        print(f"The book {isbn} : Not found")
        return

    del library[isbn]


def check_out_book(library:dict, isbn:str):
    if isbn not in library:
        print(f"The book {isbn} : Not found")
        return

    if library[isbn]["available"] is False:
        print(f"The book {isbn} : already checked out.")
        return

    library[isbn]["available"] = False


def return_book(library:dict, isbn:str):
    if isbn not in library:
        print(f"The book {isbn} : Not found")
        return

    library[isbn]["available"] = True


def display_books(library:dict):
    if not library:
        print("The library is empty")
        return

    for isbn, book in library.items():
        status = "Available" if book["available"] else "Checked Out"
        print(f'{book["title"]} by {book["author"]} (ISBN: {book["isbn"]}) - {status}')