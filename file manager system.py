import os

def create_file(filename):
    """Creates a new file if it doesn't already exist"""
    try:
        with open(filename, 'x') as f:
            print(f"✅ File '{filename}' created successfully.")
    except FileExistsError:
        print("🔴 File already exists!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def read_file(filename):
    """Reads and prints the content of the file"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("\n📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"🔴 File '{filename}' not found!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def write_file(filename):
    """Writes user input to a file (overwrites existing content)"""
    try:
        with open(filename, 'w') as f:
            data = input("✏️ Write your content: ")
            f.write(data)
            print(f"✅ Data written successfully to '{filename}'.")
    except IOError:
        print(f"❌ Unable to write to '{filename}'.")

def delete_file(filename):
    """Deletes the specified file"""
    try:
        os.remove(filename)
        print(f"✅ File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"🔴 File '{filename}' not found!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def edit_info(filename):
    """Appends user input to an existing file"""
    try:
        with open(filename, 'a') as f:
            info = input("✏️ Add additional content: ")
            f.write("\n" + info)
            print("✅ Info added successfully.")
    except IOError:
        print("❌ Unable to append data!")

if __name__ == '__main__':
    while True:
        print("\n🧐 Welcome to the File Manager System")
        print("1️⃣ Create a file")
        print("2️⃣ Read file content")
        print("3️⃣ Write new content (overwrite)")
        print("4️⃣ Delete a file")
        print("5️⃣ Append content")
        print("6️⃣ Exit")

        try:
            choice = int(input("🔢 Enter your choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1-6.")
            continue

        if choice in [1, 2, 3, 4, 5]:
            filename = input("📂 Enter file name: ")

        if choice == 1:
            create_file(filename)
        elif choice == 2:
            read_file(filename)
        elif choice == 3:
            write_file(filename)
        elif choice == 4:
            delete_file(filename)
        elif choice == 5:
            edit_info(filename)
        elif choice == 6:
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-6.")
