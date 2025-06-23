import os

# --- Configuration ---
user = "root"
host = "192.168.182.132"

def show_menu():
    print("\n--- Linux Command Menu ---")
    print("1. Show Current Date and Time (date)")
    print("2. Show Calendar (cal)")
    print("3. List Directory Files (ls)")
    print("4. Show Network Configuration (ifconfig)")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        os.system(f'ssh {user}@{host} "date"')
    elif choice == '2':
        os.system(f'ssh {user}@{host} "cal"')
    elif choice == '3':
        os.system(f'ssh {user}@{host} "ls -l"')
    elif choice == '4':
        os.system(f'ssh {user}@{host} "ifconfig"')
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1-5.")
