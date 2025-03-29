import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class BookManager:
    def __init__(self):
        self.library = []

    def add_book(self):
        self.clear_screen()
        print("\n📖 ADD NEW BOOK 📖")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        self.library.append(Book(title, author))
        print("\n✅ Book added successfully!\n")
        input("Press Enter to continue...")

    def display_books(self):
        self.clear_screen()
        print("\n📚 LIBRARY CATALOG 📚")
        if self.library:
            print("-" * 40)
            for index, book in enumerate(self.library, start=1):
                print(f"{index}. {book}")
            print("-" * 40)
        else:
            print("\n🚫 The library is empty.\n")
        input("Press Enter to continue...")

    def update_book(self):
        self.clear_screen()
        print("\n✏️ UPDATE BOOK ✏️")
        self.display_books()
        if self.library:
            try:
                index = int(input("\nEnter the book number to update: ")) - 1
                if 0 <= index < len(self.library):
                    new_title = input("Enter new title: ")
                    new_author = input("Enter new author: ")
                    self.library[index].title = new_title
                    self.library[index].author = new_author
                    print("\n✅ Book updated successfully!\n")
                else:
                    print("\n❌ Invalid book number.\n")
            except ValueError:
                print("\n❌ Please enter a valid number.\n")
        input("Press Enter to continue...")

    def delete_book(self):
        self.clear_screen()
        print("\n🗑️ DELETE BOOK 🗑️")
        self.display_books()
        if self.library:
            try:
                index = int(input("\nEnter the book number to delete: ")) - 1
                if 0 <= index < len(self.library):
                    removed_book = self.library.pop(index)
                    print(f"\n✅ Book '{removed_book.title}' deleted successfully!\n")
                else:
                    print("\n❌ Invalid book number.\n")
            except ValueError:
                print("\n❌ Please enter a valid number.\n")
        input("Press Enter to continue...")

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def main():
    manager = BookManager()
    while True:
        manager.clear_screen()
        print("\n" + "=" * 40)
        print(" 📚 WELCOME TO SIMPLE LIBRARY SYSTEM 📚 ")
        print("=" * 40)
        print("  1️⃣  Add Book")
        print("  2️⃣  Display Library")
        print("  3️⃣  Update Book")
        print("  4️⃣  Delete Book")
        print("  5️⃣  Exit")
        print("=" * 40)

        choice = input("🔹 Enter your choice: ")

        if choice == '1':
            manager.add_book()
        elif choice == '2':
            manager.display_books()
        elif choice == '3':
            manager.update_book()
        elif choice == '4':
            manager.delete_book()
        elif choice == '5':
            print("\n👋 Exiting program... Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
