class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

library = Library("PCE Library")

book1= Book("Let Us C","Yashwant Kanetkar")
book2=Book("Maths","B.S.Grewal")

library.add_book(book1)
library.add_book(book2)

for i in library.list_books():
    print(i)


        