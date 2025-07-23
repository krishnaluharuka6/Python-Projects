# a-z lower case
# 0-9
# . and _ only once before @
# @ only one
# . after @ index should be -3 or -4



# x =               r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[\.]\w{2,3}$"



import re

email_condition = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[\.]\w{2,3}$"

user_email = input("Enter your email")

if re.search(email_condition,user_email):
    print("Right email")
else:
    print("Wrong email")