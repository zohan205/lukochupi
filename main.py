import random
import base64
from __version__ import VERSION

#########################################################
# Project: https://github.com/zohan205/lukochupi        #
# Creator: Zohan                                        #
# Version: 1.0.0                                        #
#########################################################

def banner(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(banner(255, 0, 0, '''
  _         _                 _                    _
 | |       | |               | |                  (_)
 | | _   _ | | __ ___    ___ | |__   _   _  _ __   _
 | || | | || |/ // _ \  / __|| '_ \ | | | || '_ \ | |
 | || |_| ||   <| (_) || (__ | | | || |_| || |_) || |
 |_| \__,_||_|\_ \\___/  \___||_| |_| \__,_|| .__/ |_|
                                           | |
                                           |_|
'''))

print("🔐 A simple password generator with various encryption methods.\n")

print("Open Source: https://github.com/zohan205/lukochupi\n"
      "Creator: Zohan (https://github.com/zohan205)")
print("Version: " + VERSION + "\n")

# Characters used for the randomized password
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while True:
    password_length = int(input('How many characters will your password be: '))
    password = ""

    #loop through provided characters to randomized password
    for x in range(0,password_length):
        password_chars = random.choice(a)
        password = password + password_chars
    print('Here is your password: '+password)
    break

#encryption begins here
encrypt_ans = input("Would you like to encrypt your password? (yes/no): ")
# Asks user if they would like to save password & encryption in a file (.txt)
file_push = input("\nWould you like your password saved in a file (yes/no): ")

#Base64 Encryption
def encrypt_base64():
    bs64_string = password
    bs64_bytes = bs64_string.encode("utf-8")
    bs64_encoded_password = base64.b64encode(bs64_bytes)

    print("Base64 Encoded:",bs64_encoded_password.decode("utf-8"))

    if file_push == "yes":
        f = open("base64.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encoded Password: " + bs64_encoded_password.decode("utf-8"))
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

#Reverse Cipher
def encrypt_reverse():
    result = password[::-1]

    print("Reversed Cipher: "+result)

    if file_push == "yes":
        f = open("reverse.txt", "w")
        f.write(f"Password: {password}\n")
        f.write(f"Reversed Password: {result}")
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

#Base32 Encryption
def encrypt_base32():
    bs32_string = password
    bs32_bytes = bs32_string.encode("utf-8")
    bs32_encoded_password = base64.b32encode(bs32_bytes)

    print("Base32 Encoded: ",bs32_encoded_password.decode("utf-8"))

    if file_push == "yes":
        f = open("base32.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encoded Password: " + bs32_encoded_password.decode("utf-8"))
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")


if encrypt_ans == 'yes':
    print("[1]--> Base64\n"
          "[2]--> Reverse Cipher\n"
          "[3]--> Base32\n")
    option = int(input('Please select any option: '))
    if option == 1:
        encrypt_base64()
    elif option == 2:
        encrypt_reverse()
    elif option == 3:
        encrypt_base32()
    else:
        print('Please enter a valid option.')


elif encrypt_ans == 'no':
    print("Don't forget your password: "+password)

else:
    print('Please select a valid option')
