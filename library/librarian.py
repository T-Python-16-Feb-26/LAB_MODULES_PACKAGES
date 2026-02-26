books=[]

def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print("This book already exists")
    else:
        library[isbn]={
       "title": title,
       "author": author,
       "isbn": isbn,
       "available": True
   }
   

def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print("This book not found")


def check_out_book(library: dict, isbn: str):
    if isbn not in library:
        print("This book not found")
    elif not library[isbn]["available"]:
        print("Book is already checked out")
    else:
        library[isbn]["available"] = False

def return_book(library:dict, isbn:str):
    if isbn in library:
        library[isbn]["available"]= True
    else:
         print("This book not found")
        

def display_books(library):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f'{book["title"]} by {book["author"]} '
              f'(ISBN: {book["isbn"]}) - {status}')
    




