import os

def new_file():
    global current_file
    current_file = None
    return ""

def open_file():
    file_path = input("Enter the filename to open: ")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        print("File not found!")
        return ""

def save_file(content):
    file_path = input("Enter the filename to save as: ")
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved as {file_path}")

def display_menu():
    print("\nSimple Command-Line Text Editor")
    print("1. New File")
    print("2. Open File")
    print("3. Save File")
    print("4. Exit")
    return input("Choose an option: ")

def main():
    content = ""
    while True:
        choice = display_menu()
        if choice == "1":
            content = new_file()
        elif choice == "2":
            content = open_file()
        elif choice == "3":
            save_file(content)
        elif choice == "4":
            print("Exiting the editor. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")
        print("\nCurrent Content:\n")
        print(content)

if __name__ == "__main__":
    main()
