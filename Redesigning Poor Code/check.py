# checkout.py

class CheckoutManager:
    def __init__(self):
        self.checkouts = []

    def check_out_book(self, user_id, isbn):
        self.checkouts.append({"user_id": user_id, "isbn": isbn})

    def check_in_book(self, isbn):
        for checkout in self.checkouts:
            if checkout['isbn'] == isbn:
                self.checkouts.remove(checkout)
                return True
        return False

    def list_checked_out_books(self):
        if not self.checkouts:
            print("No books checked out.")
        else:
            for checkout in self.checkouts:
                print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}")
