def add_book(library ,title,author,isbn):
    if isbn in library:
        print("Book with this ISBN already exists")
    else:
        library[isbn] = {
            "title":title,
            "author":author,
            "isbn":isbn,
            "available":True
        }
def remove_book(library,isbn):
    if isbn in library:
         del library[isbn]
    else:
       print("book not found")

def check_out_book(library,isbn):
    if isbn not in library:
        print("book not found")
    elif not library[isbn]["available"]:
             print("book is already checked out")
    else:
            library [isbn]["available"] = False
def return_book(library,isbn):
    if isbn not in library:
        print("book not found")
    else:
        library[isbn]["available"] = True
def display_book(library):
    for book in library.values():
        status ="available" if book["available"]else "checked out"
        print(f"{book['title']} by {book ['author']}(ISBN:{book['isbn']}) - {status}")
print()
