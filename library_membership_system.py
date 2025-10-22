class member:
    def __init__(self, name, member_id):
        if not name.strip():
            raise ValueError("member name cannot be empty")
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not new_name.strip():
            raise ValueError("member name cannot be empty")
        self.__name = new_name

    def borrow_book(self, book_name):
        if not book_name.strip():
            raise ValueError("book name cannot be empty")
        if book_name in self.__borrowed_books:
            print(f"{self.__name} already borrowed '{book_name}'")
        else:
            self.__borrowed_books.append(book_name)
            print(f"{self.__name} borrowed '{book_name}'")

    def return_book(self, book_name):
        if not book_name.strip():
            raise ValueError("book name cannot be empty")
        if book_name in self.__borrowed_books:
            self.__borrowed_books.remove(book_name)
            print(f"{self.__name} returned '{book_name}'")
        else:
            print(f"{self.__name} did not borrow '{book_name}'")

    def show_info(self):
        print(f"member name: {self.__name}")
        print(f"member ID: {self.__member_id}")
        if self.__borrowed_books:
            print("borrowed books:")
            for book in self.__borrowed_books:
                print(f"- {book}")
        else:
            print("no books currently borrowed.")

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()


if __name__ == "__main__":
    member1 = member("Ryan", 101)

    member1.borrow_book("The Hobbit")
    member1.borrow_book("Twilight")
    member1.borrow_book("The Hobbit")  
    member1.show_info()
    member1.return_book("Twilight")
    member1.show_info()