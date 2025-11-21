import sys


if len(sys.argv) != 5:
    print("Usage: python login.py <website> <url> <username> <password>")
    sys.exit(1)

website = sys.argv[1]
url = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

if website == "":
    print("Error: Website name is missing!")
elif url == "":
    print("Error: URL is missing!")
elif username == ""
    print("Error: Username is missing!")
elif password == "":
    print("Error: Password is missing!")
else:
    print("Login Details:")
    print(f"Website : {website}")
    print(f"URL     : {url}")
    print(f"Username: {username}")
    print(f"Password: {password}")
