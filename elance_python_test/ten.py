#coding=utf-8
"""
A bank has implemented criteria for determining whether the transaction passwords typed by customers of the bank are valid or not.

Following are the criteria for checking the transaction password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [*#+@]
4. Minimum length of transaction password: 4
5. Maximum length of transaction password: 6
6. No space is allowed

Write a program which will accept a sequence of comma separated transaction passwords and will check them according to the bank's criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

Abc@1,a B1#,2w3E*,2We#3345

Then, the output of the program should be:

Abc@1,2w3E*

Note: In case of input data being supplied to the question, it should be assumed to be a console input.
"""

#方法1
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<4 or len(p)>6:
        continue
    else:
        pass

    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[*#+@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass

    value.append(p)

print ",".join(value)
#and re.search("[a-z]",x) 
    #and re.search("[*#+@]",x) and not re.search("\s",x)

#方法2
print ",".join(filter(lambda x:len(x)>=4 and len(x)<=6 and re.search("[a-z]",x)\
    and re.search("[0-9]",x) and re.search("[A-Z]",x) \
    and re.search("[*#+@]",x) and not re.search("\s",x),raw_input().split(",")))