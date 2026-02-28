
library={}

def add_book(library:dict, title:str, author:str, isbn:str):
   if isbn in library:
    print(f"the isbn {isbn}  exists") 
   else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }

def remove_book(library:dict, isbn:str):
      if isbn in library:
        del library[isbn]
      else:
          print(f"the isbn {isbn}  exists")
          
def check_out_book(library:dict, isbn:str):
    if isbn not in library:
       print(f"the isbn {isbn} does not exists")
    elif not library[isbn]["available"]:
        print("book is not available")
    else:
        library[isbn]["available"] = False

def return_book(library:dict, isbn:str): 
   if isbn in library:
    library[isbn]["available"]=True
   else:
    print(f"The isbn {isbn} does not exists")

def display_books(library: dict):
    for isbn, book in library.items():
        state= "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {state}")