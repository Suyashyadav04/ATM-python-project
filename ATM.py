class ATM:
    def __init__(self):
        # Initialize with a default balance
        self.balance = 1000.0  # Default balance for the example
        self.pin = "1234"  # Default PIN for simplicity

    def validate_pin(self):
        """Validate the user's PIN."""
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("PIN validated successfully!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        
        print("Too many incorrect attempts. Exiting.")
        return False

    def display_menu(self):
        """Display the ATM menu."""
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        """Display the current balance."""
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit_money(self):
        """Deposit money into the account."""
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully!")
                self.check_balance()
            else:
                print("Enter a valid amount greater than $0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw_money(self):
        """Withdraw money from the account."""
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"${amount:.2f} withdrawn successfully!")
                    self.check_balance()
                else:
                    print("Insufficient funds!")
            else:
                print("Enter a valid amount greater than $0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def run(self):
        """Main method to run the ATM interface."""
        print("Welcome to the ATM!")
        if not self.validate_pin():
            return
        
        while True:
            self.display_menu()
            try:
                choice = int(input("Choose an option (1-4): "))
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.deposit_money()
                elif choice == 3:
                    self.withdraw_money()
                elif choice == 4:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select an option from 1 to 4.")
            except ValueError:
                print("Invalid input. Please enter a numeric choice.")

# Run the ATM interface
if __name__ == "__main__":
    atm = ATM()
    atm.run()
