def add_book(library:dict, title:str, author:str, isbn:str): # لاضافه كتب 
    if isbn in library:
        print("Book already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }


def remove_book(library:dict, isbn:str): #لحذف كتب
    if isbn not in library:
        print("Book not found.")
        return

    del library[isbn]


def check_out_book(library:dict, isbn:str): # تشييك على الكتب
    if isbn not in library:
        print("Book not found.")
        return

    if not library[isbn]["available"]:
        print("Book is not available.")
        return

    library[isbn]["available"] = False


def return_book(library:dict, isbn:str): #لاعاده كتب
    if isbn not in library:
        print("Book not found.")
        return

    library[isbn]["available"] = True


def display_books(library:dict): #لعرض كتب
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")