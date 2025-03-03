import pikepdf
from termcolor import colored

def hack(path, wordlist):
    with open(wordlist, 'r') as f:
        passwords = f.readlines()

    for password in passwords:
        password = password.strip()  # Remove leading/trailing whitespace, including '\n'
        try:
            with pikepdf.open(path, password=password) as pdf:
                return colored("The password is: {}".format(password), "green")
        except pikepdf.PasswordError:
            print(colored("Password tried: {}".format(password), "red"))
            continue
    return colored("Password not found", "red")

path = input("Enter the path of your PDF file: ")
wordlist = input("Enter the path of your wordlist file: ")
result = hack(path, wordlist)
print(result)
