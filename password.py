import string as s
from random import randint, choice
#pip install pyperclip
import pyperclip as clipboard
import sys


def generate_password(minLen, maxLen):
    chars = s.ascii_letters
    digits = s.digits
    punctuation = s.punctuation
    # Make a long string contains all alphabet letter (lowercase and uppercase) + all nums + all punctuation:
    ch = chars + digits + punctuation
    password = ""

    # password will always starts and ends with a char:
    while ((len(password) == 0) or not(password[0] in chars and password[-1] in chars)):
        # Make a string contains random letters, nums and punctuations from ch. Its length between 8 and 25 chars:
        password = "".join(choice(ch) for _ in range(randint(minLen, maxLen)))

    # copy password to user's clipboard:
    cp = clipboard.copy(password) # returns None


    # Paste what has been copied to check it was copied correctly:
    ps = clipboard.paste()
    print()
    print("Password: ")
    print(ps)
    print()
    print("Coppied it to clipboard for you, you can use it right ahead..")


if __name__ == '__main__':
    try:
        minLen = int(sys.argv[1])
        maxLen =  int(sys.argv[2])

    except IndexError as IE:
        print()
        print(f"usage:\n      password.py <int> <int>")

    else:
        generate_password(minLen, maxLen)

