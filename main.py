import dateOP
import library
from library.librarian import *

#main function
books = {
    
}
if __name__ == "__main__":
    print("calling the date module")
    print(dateOP.getCurrentTime())
    
    #library bonus lab
    print("="*10,"Library bonus lab","="*10)
    add_book(books, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    add_book(books, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    add_book(books, "1984", "George Orwell", "9780451524935")
    display_books(books)

    check_out_book(books, "9780316769174")
    display_books(books)

    return_book(books, "9780316769174")
    display_books(books)
    
    remove_book(books, "9780451524935")
    display_books(books)