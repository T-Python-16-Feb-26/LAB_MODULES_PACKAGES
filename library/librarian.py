def isbn_in_library(library:dict, isbn:str) -> bool:
    """Search the library for the isbn return true if found"""
    if isbn in library.keys():
        return True
    return False

def add_book(library:dict, title:str, author:str, isbn:str):
    """Adds book to the library if the isbn does not used"""
    if isbn_in_library(library, isbn):
        print("Couldn\'t add book, ISBN already exists in the library.")
    else:
        book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "available" : True
    }
        library[isbn] = book
        print("Book added")
def remove_book(library:dict, isbn:str):
    """Removes book from library if the isbn exist"""
    if isbn_in_library(library, isbn):
        del library[isbn]
        print("Book removed")
    else:
        print("Couldn\'t remove book, ISBN does not exist in the library.")

def check_out_book(library:dict, isbn:str):
    """Checking out books from library if the isbn exsit in the library and the book is available"""
    if isbn_in_library(library, isbn):
        if library[isbn]["available"] == True:
            library[isbn]["available"] = False
            print("Book checked out")
        else:
            print("Book not available right now, we\'ll let you know when its returned")
    else:
        print("Couldn\'t check out book, ISBN does not exist in the library.")

def return_book(library:dict, isbn:str):
    """Return book to library if the isbn exist"""
    if isbn_in_library(library, isbn):
        if library[isbn]["available"] == False:
            library[isbn]["available"] = True
            print("Book returned")
        else:
            print("Book was not checked out or already returned")
    else:
        print("Couldn\'t return book, ISBN does not exist in the library.")
def display_books(library:dict):
    """Display all books that exist in the library in an alphabetical order, with each books info"""
    print("+" * 15)
    print("Library Books: ")
    if not library:
        print("Library is empty :(")
    else:
        books = list(library.values())
        books = sorted(books, key=lambda book: book["title"])
        for book in books:
            title = book["title"]
            author = book["author"]
            isbn = book["isbn"]
            available = "Available" if book["available"] else "Checked Out"
            print(f"{title} by {author} (ISBN: {isbn}) - {available}")
    print("+" * 15)