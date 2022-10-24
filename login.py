username = input("Enter your username: ")
password = input("Please enter your password: ")

if (username == "Admin" and password == "1234@admin"):
    print(f"Hello you're logged in as {username}")
else:
    print("Invalid username/password")