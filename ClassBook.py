import os
import time
import sys  # Missing import fixed

class Colors:
    RESET = "\033[0m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"

class Book:
    def __init__(self, title: str, author: str):
        self.title = title.strip().title()
        self.author = author.strip().title()

    def __str__(self):
        return f"📚 {self.title} by {self.author}"

class BookManager:
    def __init__(self):
        self.library = []

    def loading_effect(self, message="Processing"):
        print(f"{Colors.YELLOW}{message}{Colors.RESET}", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")

    def add_book(self):
        self.clear_screen()
        self.display_header("ADD NEW BOOK")
        title = self.get_input(f"{Colors.YELLOW}Enter book title: {Colors.RESET}")
        author = self.get_input(f"{Colors.YELLOW}Enter author: {Colors.RESET}")

        if title and author:
            if self.get_existing_book(title, author):
                self.display_message(f"{Colors.RED}⚠️ The book already exists!{Colors.RESET}")
            else:
                self.library.append(Book(title, author))
                self.loading_effect("Adding book")
                self.display_message(f"{Colors.GREEN}✅ Book '{title}' added successfully!{Colors.RESET}")
        else:
            self.display_message(f"{Colors.RED}⚠️ Book title and author cannot be empty!{Colors.RESET}")

    def display_books(self):
        self.clear_screen()
        self.display_header("LIBRARY CATALOG")
        self.loading_effect("Fetching books")

        if self.library:
            print(Colors.BLUE + "-" * 50 + Colors.RESET)
            for index, book in enumerate(self.library, start=1):
                print(f"{Colors.YELLOW}{index}.{Colors.RESET} {book}")
            print(Colors.BLUE + "-" * 50 + Colors.RESET)
        else:
            print(f"{Colors.RED}🚫 The library is empty.{Colors.RESET}\n")
        input(f"{Colors.YELLOW}Press Enter to return to menu...{Colors.RESET}")

    def update_book(self):
        self.clear_screen()
        self.display_header("UPDATE BOOK")
        if not self.library:
            self.display_message(f"{Colors.RED}🚫 No books available to update.{Colors.RESET}")
            return

        self.display_books()
        index = self.get_book_index(f"{Colors.YELLOW}Enter the book number to update: {Colors.RESET}")
        if index is not None:
            new_title = self.get_input("Enter new title (leave blank to keep current): ", True)
            new_author = self.get_input("Enter new author (leave blank to keep current): ", True)
            if new_title or new_author:
                if new_title:
                    self.library[index].title = new_title.strip().title()
                if new_author:
                    self.library[index].author = new_author.strip().title()
                self.loading_effect("Updating book")
                self.display_message(f"{Colors.GREEN}✅ Book updated successfully!{Colors.RESET}")
            else:
                self.display_message(f"{Colors.RED}⚠️ No changes made.{Colors.RESET}")

    def delete_book(self):
        self.clear_screen()
        self.display_header("DELETE BOOK")
        if not self.library:
            self.display_message(f"{Colors.RED}🚫 No books available to delete.{Colors.RESET}")
            return

        self.display_books()
        index = self.get_book_index(f"{Colors.YELLOW}Enter the book number to delete: {Colors.RESET}")
        if index is not None:
            removed_book = self.library.pop(index)
            self.loading_effect("Deleting book")
            self.display_message(f"{Colors.GREEN}✅ Book '{removed_book.title}' deleted successfully!{Colors.RESET}")

    def get_existing_book(self, title: str, author: str):
        for book in self.library:
            if book.title == title.title() and book.author == author.title():
                return book
        return None

    def get_book_index(self, prompt: str):
        """Fix infinite loop: Allow exit if the user inputs nothing."""
        while True:
            user_input = self.get_input(prompt, allow_empty=True)
            if not user_input:
                return None  # Return if the user enters nothing
            
            try:
                index = int(user_input) - 1
                if 0 <= index < len(self.library):
                    return index
                else:
                    self.display_message(f"{Colors.RED}❌ Invalid book number.{Colors.RESET}")
            except ValueError:
                self.display_message(f"{Colors.RED}❌ Please enter a valid number.{Colors.RESET}")

    @staticmethod
    def get_input(prompt: str, allow_empty=False) -> str:
        while True:
            value = input(prompt).strip()
            if value or allow_empty:
                return value
            print(f"{Colors.RED}⚠️ Input cannot be empty.{Colors.RESET}")

    @staticmethod
    def display_header(title: str):
        print("\n" + Colors.BLUE + "=" * 50 + Colors.RESET)
        print(f"{Colors.BLUE}📚 {title.center(40)} 📚{Colors.RESET}")
        print(Colors.BLUE + "=" * 50 + Colors.RESET)

    @staticmethod
    def display_message(message: str):
        print(f"\n{message}\n")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


# ✅ Fix the misplaced function
def exit_program():
    print(f"\n{Colors.GREEN}👋 Exiting program... Goodbye!{Colors.RESET}\n")
    sys.exit()


def main():
    manager = BookManager()
    while True:
        manager.clear_screen()
        manager.display_header("WELCOME TO SIMPLE LIBRARY SYSTEM")

        print(f"{Colors.YELLOW}  1️⃣  Add Book{Colors.RESET}")
        print(f"{Colors.YELLOW}  2️⃣  Display Library{Colors.RESET}")
        print(f"{Colors.YELLOW}  3️⃣  Update Book{Colors.RESET}")
        print(f"{Colors.YELLOW}  4️⃣  Delete Book{Colors.RESET}")
        print(f"{Colors.YELLOW}  5️⃣  Exit{Colors.RESET}")
        print(Colors.BLUE + "=" * 50 + Colors.RESET)

        choice = input(f"{Colors.YELLOW}🔹 Enter your choice: {Colors.RESET}")

        # ✅ Fix misplaced menu_actions
        menu_actions = {
            '1': manager.add_book,
            '2': manager.display_books,
            '3': manager.update_book,
            '4': manager.delete_book,
            '5': exit_program,  # Correctly calls exit function
        }

        action = menu_actions.get(choice)
        if action:
            action()
        else:
            manager.display_message(f"{Colors.RED}❌ Invalid choice. Please try again.{Colors.RESET}")


if __name__ == "__main__":
    main()
