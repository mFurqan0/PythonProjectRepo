import random
import string

CharValues = string.ascii_letters + string.digits + string.punctuation
pass_len = 12

Password = ""
for i in range(pass_len):
    Password += random.choice(CharValues)

print("Your password is:",Password)

