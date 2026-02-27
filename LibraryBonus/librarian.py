
def add_book(library:dict,title:str,author:str,isbn:str):
    if isbn in library:
        print("The book is available")
        
    library[isbn]={
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "available":True
    }
def remove_book(library:dict,isbn:str):
    if isbn not in library:
       print("The book is not found in the library.")
       
    del library[isbn]

def check_out_book(library:dict,isbn:str):
    if isbn not in library:
        print("The book is not found in the library.")
        
    if not library[isbn]["available"]:
        print("The book is not available.")
        
    library[isbn]["available"]= False

def return_book(library:dict,isbn:str):
    if isbn not in library:
        print("The book is not found in the library.")
    
    library[isbn]["available"]= True

def display_book(library:dict):
    for book in library.values():
        if book['available']==True:
            status = "Available"
        else:
            status = "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN:{book['isbn']}) - {status}")
    return library