#coding=utf-8
"""

Write a program which accepts bank account transactions in a comma separated sequence and prints the net account balance. The various transactions are classified as deposits (D) and withdrawals (W). Deposit transactions are suffixed with a hyphen followed by D and Withdrawal transactions are suffixed with a hyphen followed by W.

If the net account balance is more than 5000 dollars, an interest of 5% should be added to the balance. The amount to be printed should be an integer value, such that if you are getting an output of 4321.0, the program should give the output as 4321.

Example

If following input is supplied to the program:

2000-D,4000-D,500-W

Then, the output of the program should be:

5775

In this example, since the net balance was above $5000, 5 % interest has been added to it.

Note: In case of input data being supplied to the question, it should be assumed to be a console input.
"""

#方法1
items=[x for x in raw_input().split(',')]
netValue = 0
for item in items:
    numString= item[:-2]
    operation=item[-1]
    if operation=="D":
        netValue+=int(numString)
    else:
        netValue-=int(numString)

if netValue>=5000:
    netValue+=netValue*0.05

print int(netValue)

#方法2
ret = 0
for s in raw_input().split(','):
	if s[-1] == "D":
		ret += int(s[:-2])
	else:
		val -= int(s[:-2])
if ret >= 5000:
	ret += ret*0.05

print int(ret)