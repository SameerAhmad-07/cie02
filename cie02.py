import sys


if len(sys.argv) != 5:
    print("Usage: python login.py <website> <url> <username> <password>")
    sys.exit(1)

website  = sys.argv[1]
url      = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

print("Login Details:")
print(f"Website : {website}")
print(f"URL     : {url}")
print(f"Username: {username}")
print(f"Password: {password}")
