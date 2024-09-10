
import hashlib

# Function to hash a given password using SHA1
def sha1_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Function to crack the hashed password
def crack_sha1_password(hashed_password, password_list):
    for password in password_list:
        # Hash the password from the list and compare it
        if sha1_hash(password) == hashed_password:
            print(f"[+] Password found: {password}")
            return password
    print("[-] Password not found.")
    return None

# Input: Get the hashed password from the user
hashed_password = input("Enter the SHA1 hashed password to crack: ")

# Input: Get the list of possible passwords from the user (comma-separated)
passwords_input = input("Enter the list of possible passwords (comma-separated): ")

# Convert the user input into a list by splitting by commas
password_list = [password.strip() for password in passwords_input.split(',')]

# Run the cracking function
crack_sha1_password(hashed_password, password_list)
