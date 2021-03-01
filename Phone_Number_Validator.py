import re
#your code goes here
num = input()
pattern = r"\A(1|8|9)\d{7}$"

match = re.search(pattern, num)
if match:
    print("Valid")
else:
    print("Invalid")
