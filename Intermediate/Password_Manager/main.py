from cryptography.fernet import Fernet

'''
Uncomment and run this function once to create your encryption key file.
After the key is created, keep it safe and never share it!
'''
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#     print("🔑 Key generated and saved as 'key.key'!")

def load_key():
    """Loads the encryption key from file."""
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("❌ Key file not found! Please run write_key() first to generate one.")
        exit()

key = load_key()
fer = Fernet(key)

def view():
    """Decrypt and show saved passwords."""
    try:
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()

            if not lines:
                print("\n📂 No passwords saved yet. Try adding some!\n")
                return

            print("\n🔐 Saved Accounts:")
            print("-" * 30)
            for line in lines:
                user, passw = line.rstrip().split("|")
                decrypted = fer.decrypt(passw.encode()).decode()
                print(f"👤 {user:<15} | 🔑 {decrypted}")
            print("-" * 30)
    except FileNotFoundError:
        print("\n⚠️ No password file found. Add a password first!\n")

def add():
    """Add a new encrypted password."""
    name = input("\nEnter account name: ").strip()
    pwd = input("Enter password: ").strip()

    if not name or not pwd:
        print("⚠️ Account name and password cannot be empty!")
        return

    with open('passwords.txt', 'a') as f:
        encrypted = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted + "\n")

    print(f"✅ Password for '{name}' added successfully!\n")

print("======================================")
print(" 🔒 Welcome to Simple Password Manager")
print("======================================")

while True:
    print("\nChoose an option:")
    print(" [1] View saved passwords")
    print(" [2] Add a new password")
    print(" [q] Quit")
    mode = input("👉 Enter your choice: ").lower()

    if mode == "q":
        print("\n👋 Goodbye! Keep your key.key file safe.\n")
        break
    elif mode == "1" or mode == "view":
        view()
    elif mode == "2" or mode == "add":
        add()
    else:
        print("❌ Invalid option. Please choose again.")
