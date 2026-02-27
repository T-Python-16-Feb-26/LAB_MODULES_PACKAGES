from librarian import add_book,display_book,check_out_book,return_book,remove_book
library={}

# Add Book
add_book(library,"The Catcher in the Rye","J.D. Salinger","9780316769174")
add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
add_book(library,"1984","George Orwell","9780451524935")
display_book(library)
print()

# Check out Book
check_out_book(library,"9780316769174")
display_book(library)
print()

# Return Book
return_book(library,"9780316769174")
display_book(library)
print()

# Remove Book
remove_book(library,"9780451524935")
display_book(library)





