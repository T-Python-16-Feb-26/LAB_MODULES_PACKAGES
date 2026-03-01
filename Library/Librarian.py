'''

'''

def add_book(library:dict, title:str, isbn:str, author:str):

    if title not in library:
        library[title] = {}
     
    if isbn in library[title]:
        print("the book already exists in the library")
        return False
   
    library[title][isbn] = {
        "author" : author,
        "available" : True
    }

    return True
        
    

def remove_book(library:dict, title:str, isbn:str):

    if title in library and isbn in library[title]:
        del library[title][isbn]
        if not library[title]:
            del library[title]
        return True
    else:
        print("there is no book with this isbn")


def check_out_book(library:dict, title:str, isbn:str):
    if title in library and isbn in library[title]:
        if library[title][isbn]["available"] == True:
            library[title][isbn]["available"] = False
            return True
    else:
        print("this book is not available")
        return False
        

def return_book(library:dict, title:str, isbn:str):


    if title in library and isbn in library[title]:
        if library[title][isbn]["available"] == False:
            library[title][isbn]["available"] = True
            return True
    else:
        print("this book is not in the library")
        return False


def display_books(library:dict):
    for title in library:
        for isbn in library[title]:
            print(f"Title:{title}  ISBN: {isbn}  Author: {library[title][isbn]['author']}  Available: {library[title][isbn]['available']}")