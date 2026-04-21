
credentials = {'Nyasha': 'mao123', 'Royce': 'dumba'} 

def login():
    print("        Login      ")

user_name = input("Username: ")
password = input("Password: ")

if user_name in credentials and credentials[user_name] == password:
    print(f"Login successful. Welcome, {user_name}!")
else:
    print("Login failed: incorrect username or password.")

login()