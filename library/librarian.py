def add_book(library, title:str, author:str, isbn:str):
    if isbn in library:
        print("Book with this ISBN already exists")
    else:
        library[isbn] = {
            "title" : title,
            "author" : author,
            "isbn" : isbn,
            "available" : True
        }

def remove_book(library:str, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print("Book with this ISBN does not exist")

def check_out_book(library:str, isbn:str):
    if isbn not in library:
        print("Book with this ISBN does not exist")
    elif not library[isbn]["available"]:
        print("Book is already checked out")
    else:
        library[isbn]["available"] = False

def return_book(library:str, isbn:str):
    if isbn not in library:
        print("Book with this ISBN does not exist")
    else:
        library[isbn]["available"] = True

def display_book(library:str):
    for book in library.values():
        status = "Available" if book["available"] else "Checked out"
        print(f'{book["title"]} by {book["author"]} (ISBN: {book["isbn"]}) - {status}')

        print()