#Initial Setup
balance = 700000
user_pin = "2259"
#User Authentication
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

#Main Menu
def display_menu():
    while True:
        print(f"\nMenu:")
        print(f"1. Check Balance")
        print(f"2. Deposit Funds")
        print(f"3. Withdraw Funds")
        print(f"4. CHange PIN")
        print(f"5. Exit")

prompt = "Main Menu\n Select an option\n 1. Check Balance\n 2. Deposit Funds\n 3. Withdraw Funds\n 4. Change PIN\n 5. Exit: "
#Functionality
while True:
    choice = input(prompt)
    if choice == '1':
       print(f"Your current balance is ${balance}: ")   #Check Balance
    elif choice == '2':
        deposit = int(input("Enter amount you want to deposit: $"))
        if deposit > 0:
            balance += deposit
            print(f"deposit of ${deposit}")      #Deposit Funds
        print(f"Your current balance is ${balance}")
    elif choice == '3':
        withdrawal = int(input("How much do you wish to withdraw: "))
        if 0 < withdrawal <= balance:
            balance -= withdrawal
            print(f"Your new balance is ${balance} ")   #Withdraw Funds
        else:
         print(f"You have insufficient funds ")
    elif choice == '4':
        current_pin = input(f'Enter your current PIN: ')
        if user_pin == current_pin:
         new_pin = int(input(f'Set your new PIN: '))
         confirm = int(input(f'Enter your new PIN again to confirm: '))    #Change PIN

        if new_pin == confirm:
           user_pin == new_pin
           print("Your PIN has been changed successfully. ")
        else:
            print("PIN confirmation does not match ")   
    if choice == '5':
        print(f"Thank you for trusting our Bank")
        break         
         
