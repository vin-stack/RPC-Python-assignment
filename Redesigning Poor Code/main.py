# main.py
import book
import user
import check
import storage

def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Check Out Book")
    print("4. Check In Book")
    print("5. List Checked Out Books")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = book.BookManager()
    user_manager = user.UserManager()
    checkout_manager = check.CheckoutManager()

    # Load existing data from files
    books = storage.load_data('books.json')
    users = storage.load_data('users.json')
    checkouts = storage.load_data('checkouts.json')

    for book_data in books:
        book_manager.add_book(book_data['title'], book_data['author'], book_data['isbn'], book_data['available'])
    for user_data in users:
        user_manager.add_user(user_data['name'], user_data['user_id'])
    for checkout_data in checkouts:
        checkout_manager.check_out_book(checkout_data['user_id'], checkout_data['isbn'])

    while True:
        try:
            choice = main_menu()
            if choice == '1':
                manage_books(book_manager)
            elif choice == '2':
                manage_users(user_manager)
            elif choice == '3':
                check_out_book(book_manager, checkout_manager)
            elif choice == '4':
                check_in_book(book_manager, checkout_manager)
            elif choice == '5':
                checkout_manager.list_checked_out_books()
            elif choice == '6':
                print("Saving data...")
                # Save data to files
                storage.save_data([vars(book) for book in book_manager.books], 'books.json')
                storage.save_data([vars(user) for user in user_manager.users], 'users.json')
                storage.save_data(checkout_manager.checkouts, 'checkouts.json')
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

def manage_books(book_manager):
    while True:
        try:
            print("\nManage Books")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Books")
            print("6. Back to Main Menu")
            choice = input("Enter choice: ")
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave empty to keep existing): ")
                author = input("Enter new author (leave empty to keep existing): ")
                if book_manager.update_book(isbn, title, author):
                    print("Book updated.")
                else:
                    print("Book not found.")
            elif choice == '3':
                isbn = input("Enter ISBN of the book to delete: ")
                if book_manager.delete_book(isbn):
                    print("Book deleted.")
                else:
                    print("Book not found.")
            elif choice == '4':
                book_manager.list_books()
            elif choice == '5':
                search_books(book_manager)
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

def manage_users(user_manager):
    while True:
        try:
            print("\nManage Users")
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. List Users")
            print("5. Search Users")
            print("6. Back to Main Menu")
            choice = input("Enter choice: ")
            if choice == '1':
                name = input("Enter name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '2':
                user_id = input("Enter user ID of the user to update: ")
                name = input("Enter new name (leave empty to keep existing): ")
                if user_manager.update_user(user_id, name):
                    print("User updated.")
                else:
                    print("User not found.")
            elif choice == '3':
                user_id = input("Enter user ID of the user to delete: ")
                if user_manager.delete_user(user_id):
                    print("User deleted.")
                else:
                    print("User not found.")
            elif choice == '4':
                user_manager.list_users()
            elif choice == '5':
                search_users(user_manager)
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print("An error occurred:", str(e))

def search_books(book_manager):
    print("\nSearch Books")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by ISBN")
    choice = input("Enter search criteria: ")
    if choice == '1':
        title = input("Enter title: ")
        found_books = book_manager.search_book_by_title(title)
    elif choice == '2':
        author = input("Enter author: ")
        found_books = book_manager.search_book_by_author(author)
    elif choice == '3':
        isbn = input("Enter ISBN: ")
        found_books = book_manager.search_book_by_isbn(isbn)
    else:
        print("Invalid choice.")
        return

    if not found_books:
        print("No books found.")
    else:
        print("Found books:")
        for book in found_books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

def search_users(user_manager):
    print("\nSearch Users")
    print("1. Search by Name")
    print("2. Search by User ID")
    choice = input("Enter search criteria: ")
    if choice == '1':
        name = input("Enter name: ")
        found_users = user_manager.search_user_by_name(name)
    elif choice == '2':
        user_id = input("Enter user ID: ")
        found_users = user_manager.search_user_by_id(user_id)
    else:
        print("Invalid choice.")
        return

    if not found_users:
        print("No users found.")
    else:
        print("Found users:")
        for user in found_users:
            print(f"Name: {user.name}, User ID: {user.user_id}")

def check_out_book(book_manager, checkout_manager):
    print("\nCheck Out Book")
    isbn = input("Enter ISBN of the book to check out: ")
    if book_manager.check_out_book(isbn):
        user_id = input("Enter user ID: ")
        checkout_manager.check_out_book(user_id, isbn)
        print("Book checked out.")
    else:
        print("Book not available or not found.")

def check_in_book(book_manager, checkout_manager):
    print("\nCheck In Book")
    isbn = input("Enter ISBN of the book to check in: ")
    if book_manager.check_in_book(isbn):
        checkout_manager.check_in_book(isbn)
        print("Book checked in.")
    else:
        print("Book not checked out or not found.")

if __name__ == "__main__":
    main()
