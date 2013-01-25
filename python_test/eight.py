#coding=utf-8
"""

Write a Program which calculates and prints the Optimal Order Quantity for the production of LCD sets. Following is the formula to calculate Optimal Order Quantity:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

Fixed cost per order, denoted by C, is $50.
Annual holding cost per unit, denoted by H, is $30.

Only the Annual Demand Quantity (D) of the product varies. The values of D are supplied as input to your program in a comma separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

Note: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)

Note: In case of input data being supplied to the question, it should be assumed to be a console input.
"""

#方法1
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)

#方法2
import math
print ','.join(map(lambda x:str(int(round(math.sqrt(2*50*float(x)/30)))),raw_input().split(',')))


'''
Write a program which will accept 4 digit binary numbers each separated by a comma as its input and then check whether they are divisible by 3 or not. The numbers that are divisible by 3 are to be printed, separated by a comma.

Example

Suppose the following input is given to the program:

0011,0100,0101,1001

Then, the output of the program should be:

0011, 1001

Note: You should assume that input to the program is from console input (raw_input) 
'''

#有关进制转换：还要弄懂chr,odr
ret = []
for val in raw_input().split(','):
	if int(val,2)%3==0:
		ret.append(val)
print ','.join(ret)

