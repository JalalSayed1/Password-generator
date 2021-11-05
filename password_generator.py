import string as s
from random import *
#pip install pyperclip
import pyperclip as clipboard

# Make a long string contains all alphabet letter (lowercase and uppercase) + all nums + all punctuation:
ch = s.ascii_letters + s.digits + s.punctuation

# Make a string contains random letters, nums and punctuations from ch. Its length between 8 and 25 chars:
password = "".join(choice(ch) for x in range(randint(15, 30)))

# print results:
# print(s.ascii_letters, "    ", s.digits, "   ", s.punctuation)
# print(f"Password: {password}")

# copy password to user's clipboard:
cp = clipboard.copy(password) # returns None


# Paste what has been copied to check it was copied correctly:
ps = clipboard.paste()
print(ps if ps == password else "The password was not copied correctly! Try again.")

