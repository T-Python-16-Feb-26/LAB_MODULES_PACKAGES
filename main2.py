'''The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Checked Out
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available

The Catcher in the Rye by J.D. Salinger (ISBN: 9780316769174) - Available
To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789) - Available
1984 by George Orwell (ISBN: 9780451524935) - Available'''

from library import librarian

my_library = {}
#to add books
librarian.add_book(my_library , "The Catcher in the Rye",'J.D. Salinger','9780316769174')
librarian.add_book(my_library , "To Kill a Mockingbird",'Harper Lee','9780446310789')
librarian.add_book(my_library , "1984",'George Orwell','9780451524935')
#to display library
librarian.display_books(my_library)
print() 

#to borrow books
librarian.check_out_book(my_library, "9780316769174")
# to display library
librarian.display_books(my_library)
print() 
#to return books
librarian.return_book(my_library,'9780316769174')
#to display library
librarian.display_books(my_library)
print() 