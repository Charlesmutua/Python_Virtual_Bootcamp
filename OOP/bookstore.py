class Store:
    #create constructor
    def __init__(self, no_of_books, total_sales, books_borrowed):
        self.no_of_books = no_of_books
        self.total_sales = total_sales
        self.books_borrowed = books_borrowed
    
    def books(self, books):
        self.no_of_books+=books
        return no_of_books

    


#books_borrowed = input("Enter the number of books borrowed: ")

print(Store.books(5))
