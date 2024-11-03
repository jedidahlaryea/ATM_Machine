#balance = 700000
#pin = 2259

def confirm_pin():
    user_pin = "2259"  
    attempts = 3

    while attempts > 0:
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == user_pin:
            print("Access granted!")
            return
        else:
            attempts -= 1
            print(f"You have entered an incorrect PIN.{attempts} attempts left.")

    print("Too many incorrect attempts. Access blocked.")

if __name__ == "__main__":
    confirm_pin()


            




