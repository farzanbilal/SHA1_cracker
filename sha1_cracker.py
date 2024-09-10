# import hashlib

# # The hashed password to crack (example SHA1 hash of "password123")
# hashed_password = 'cbfdac6008f9cab4083784cbd1874f76618d2a97'

# # Dictionary of possible passwords
# password_list = ['123456', 'password', 'admin', 'password123', 'qwerty']

# # Function to hash a given password
# def sha1_hash(password):
#     return hashlib.sha1(password.encode()).hexdigest()

# # Function to crack the hashed password
# def crack_sha1_password(hashed_password, password_list):
#     for password in password_list:
#         # Hash the password from the list and compare it
#         if sha1_hash(password) == hashed_password:
#             print(f"[+] Password found: {password}")
#             return password
#     print("[-] Password not found.")
#     return None

# # Run the cracking function
# crack_sha1_password(hashed_password, password_list)
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
