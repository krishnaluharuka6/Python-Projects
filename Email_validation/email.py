
import string

email = input("Enter your email: ")
punct = string.punctuation
punct = punct.replace('@',"")
punct = punct.replace('_',"")
punct = punct.replace('.',"")

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase


# min 6 char, no uppercase, first letter alphabet, @ only one, no space, . at 3rd or 4th index from last, special character : underscore,dot only


if len(email) >= 6:
    if " " not in email:
        if email.count('@') == 1:
            if email[0].isalpha():
                if (email[-3] == ".") ^ (email[-4] == "."):
                    for i in email:
                        if i in punct:
                            print(f"{i} special character can't be used in email")
                        elif i==i.upper():
                            if i == '@' or i=='_' or i=='.' or i.isdigit():
                                continue
                            else:
                                print(f"'{i}' can't be uppercase in your email")
                                break
                        else:
                            print("Correct email") 
                            break     
                else:
                    print("The dot character should be at 3 or 4 place from right to left")
            else:
                print("The email should begin with alphabet")
        else:
            print("@ can be used only once")
    else:
        print("Whitespace is not allowed in email")
else:
    print("Length of email should be greater than 6")

