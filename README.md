## SHA1 Password Cracker

### Description

The SHA1 Password Cracker is a simple Python script designed to demonstrate how a dictionary-based attack can be used to find a plaintext password that matches a given SHA1 hash. The script accepts a SHA1 hashed password and a list of possible plaintext passwords (entered by the user), hashes each potential password using SHA1, and compares it against the hashed input to find a match.

This project illustrates how insecure SHA1 is for password hashing due to its susceptibility to brute force and dictionary attacks, thus reinforcing the importance of using modern hashing algorithms like bcrypt, Argon2, or PBKDF2 for password storage.

### Features
- Accepts user input for the hashed password and a list of potential passwords.
- Uses SHA1 hashing to compare the input password hash with the possible passwords.
- Outputs the matching plaintext password if found.

---

### Requirements

Make sure you have Python installed on your machine. If not, you can download it [here](https://www.python.org/downloads/).

- Python 3.x
- No additional libraries are required.

---

### How to Use

1. **Clone the Repository**: 
   Clone this repository to your local machine or download the `sha1_cracker.py` script directly.

2. **Run the Script**:
   Open a terminal or command prompt, navigate to the directory where the script is saved, and run the following command:
   

   python sha1_cracker.py


   If using `python3`, run:
   

   python3 sha1_cracker.py


3. **Input the Required Information**:
   - **SHA1 Hashed Password**: When prompted, enter the SHA1 hashed password that you want to crack.
   - **Possible Passwords**: Enter a list of potential passwords (comma-separated).

   Example:
   ```
   Enter the SHA1 hashed password to crack: cbfdac6008f9cab4083784cbd1874f76618d2a97
   Enter the list of possible passwords (comma-separated): 123456, password, admin, password123, qwerty
   ```

4. **View the Results**:
   The script will try each password and print the matching password if found. If no password matches the given hash, it will output "Password not found."

---

### Example Run


$ python sha1_cracker.py
Enter the SHA1 hashed password to crack: cbfdac6008f9cab4083784cbd1874f76618d2a97
Enter the list of possible passwords (comma-separated): 123456, password, admin, password123, qwerty
[+] Password found: password123

### How it Works

1. The user provides a SHA1 hashed password and a list of possible passwords.
2. The script iterates over the list of possible passwords and hashes each one using the SHA1 algorithm.
3. If the hash of one of the passwords matches the provided hash, the script outputs the password.
4. If none of the passwords match, the script informs the user that no password was found.

### Limitations

- This script is designed for demonstration purposes and works only with small dictionaries.
- For larger password lists or more complex password cracking techniques, more sophisticated tools like Hashcat should be used.
- **Important**: SHA1 is no longer secure for hashing passwords and should not be used in production systems.

---

### Security Note
This script is for educational purposes only. It should be used to understand the weaknesses of older hashing algorithms like SHA1 and the importance of using strong password hashing techniques. Do not use this script for illegal or unethical activities.
