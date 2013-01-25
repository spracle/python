#coding=utf-8
"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

order,hello,would,test

Then, the output should be:

hello,order,test,would

Note: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
#方法1
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)

#方法2
s = raw_input().split(",")
s.sort()
print ','.join(s)