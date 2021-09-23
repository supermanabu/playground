import json

filename = 'username.json'
with open(filename, 'r') as f:
    a = json.load(f)
print(type(a))
exit()
try:
    with open(filename, 'r') as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
