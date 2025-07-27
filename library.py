class Library:
    def __init__(self):
        self.books = {}  # title -> status ("available" or "issued")

    def add_book(self, title):
        if title in self.books:
            print(f"'{title}' already exists.")
        else:
            self.books[title] = "available"
            print(f"Added '{title}'.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Removed '{title}'.")
        else:
            print("Book not found.")

    def issue_book(self, title):
        if title in self.books:
            if self.books[title] == "available":
                self.books[title] = "issued"
                print(f"Issued '{title}'.")
            else:
                print(f"'{title}' is already issued.")
        else:
            print("Book not found.")

    def return_book(self, title):
        if title in self.books and self.books[title] == "issued":
            self.books[title] = "available"
            print(f"Returned '{title}'.")
        else:
            print("Invalid return operation.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for title, status in self.books.items():
                print(f"{title} - {status}")


# Menu
lib = Library()
while True:
    print("\n1. Add Book\n2. Remove Book\n3. Issue Book\n4. Return Book\n5. Show Books\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        lib.add_book(input("Enter title: "))
    elif choice == '2':
        lib.remove_book(input("Enter title: "))
    elif choice == '3':
        lib.issue_book(input("Enter title: "))
    elif choice == '4':
        lib.return_book(input("Enter title: "))
    elif choice == '5':
        lib.show_books()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")  