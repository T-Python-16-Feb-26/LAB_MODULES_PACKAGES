library = {
    
}


def add_book(library,title, author, isbn):
    if isbn not in library:
        library[isbn] = {
        "title": title,
        "author": author,
        "available": True
        }
        print("Added")
    else:
        print("Book is already in the library")
    
        

def remove_book(library,isbn:str):
    
    if isbn in library:
        del library[isbn]
        print("Done")
    else:
        print("the book is not available")

def check_out_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = False
        print("Done")
    else:
        print("not available")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        print("Done")
    else:
        print("not available")

def display_books(library):
    for num,book in enumerate(library,start=1):
        if library[book]["available"] == True:
            msg = "Yes"
        elif library[book]["available"] == False:
            msg = "No"
        print(f"{num}- {library[book]["title"]} | Author: {library[book]["author"]} | ISBN: {book} | Available Online: {msg}")
