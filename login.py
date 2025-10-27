# Simple Login System

# Sample username and password
username = "admin"
password = "12345"

# Ask user to enter credentials
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

# Check credentials
if user_input == username and pass_input == password:
    print("✅ Login successful! Welcome,", username)
else:
    print("❌ Invalid username or password. Try again.")

