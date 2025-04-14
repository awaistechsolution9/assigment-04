import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

password_db = {}

def add_password(website, password):
    password_db[website] = hash_password(password)

def check_password(website, password):
    if website in password_db and password_db[website] == hash_password(password):
        print("Password is correct!")
    else:
        print("Incorrect password!")

# Test
add_password('example.com', 'mySecurePassword123')
check_password('example.com', 'mySecurePassword123')  
check_password('example.com', 'wrongPassword')       
