#IMPORTINFLibraries
import random
import string

#GeneratingPassword
def generate_password(length_Of_Password):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length_Of_Password))
    return password

def main():
    print("Welcome to Password Generator!")
    #DEsired LengthOfPassword
    length_Of_Password = int(input("Enter the desired length of the password: "))

    if length_Of_Password <= 0:
        print("Invalid password length. Please enter a positive integer.")
    else:
        password = generate_password(length_Of_Password)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
