import sys

def main():
    
    if len(sys.argv) != 5:
        print("Usage: python script.py <website> <url> <username> <password>")
        sys.exit(1)

    website = sys.argv[1]
    url = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

    
    if website and url and username and password:
        print("Login Details:")
        print(f"Website: {website}")
        print(f"URL: {url}")
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("Error: One or more login details are missing!")

if __name__ == "__main__":
    main()
