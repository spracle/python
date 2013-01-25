#coding=utf-8
"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 1000 and 1200 (both included).
The numbers obtained should be printed in a comma separated sequence on a single line.
"""


#方法1
l=[]
for i in range(1000, 1201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print ','.join(l)

#方法2
print ','.join(map(lambda x:(str(x)),filter(lambda x:x%7==0 and x%5!=0,range(1000,1201))))

'''
Write a program to calculate the bill amount, in cents, for the units of power consumed. Following are the rates applicable:

1. First 0-100 units: 60 cents per unit
2. Next 200 units: 70 cents per unit
3. Beyond 300 units: 80 cents per unit

The program should accept three different usage unit readings.

Example

If the following inputs are supplied:

305
180
120

Then, the output should be:

20400
11600
7400

Note: You should assume that input to the program is from console input (raw_input) 
'''

#用raw_input不要用input，因为输出会影响input
for i in range(3):
	num = int(raw_input())
	if num <= 100:
		print num * 60
	elif num > 100 and num <= 300:
		print 6000 + (num - 100)*70
	elif num > 300:
		print 20000 + (num - 300)*80
'''
Below are the error details

File "prog.py", line 2, in 
File "", line 1
150
^
SyntaxError: unexpected EOF while parsing
'''