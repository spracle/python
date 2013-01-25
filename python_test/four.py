#coding=utf-8
"""
Write a program which takes 4 inputs, where each input consists of 2 numbers in the format x,y. You are required to print a two dimensional array having x rows and y columns for each input. The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.

Example

Suppose the following 4 inputs are given to the program:

2,2
2,3
3,3
3,4

Then, the output of the program should be:

[[1, 2], [3, 4]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Note: In case of input data being supplied to the question, it should be assumed to be a console input.

"""
#方法1
digitsList=[]
for i in range(4):
    str = raw_input()
    digits=[int(x) for x in str.split(',')]
    digitsList.append(digits)

for i in range(len(digitsList)):
    rowNum = digitsList[i][0]
    colNum = digitsList[i][1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    #print multilist

    val = 1
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= val
            val +=  1

    print multilist

#方法2
for i in range(4):
    inputs = map(lambda x:int(x),raw_input().split(','))
    ret = []
    for j in range(inputs[0]):
        ret.append(map(lambda x:x+j*inputs[1]+1,range(inputs[1])))
    print ret

input()

'''
Write a program which will receive a comma separated sequence of numbers. Suppose a particular input number is represented by "n". The program should find the greatest "n" digit number which is divisible by "n" itself. The output should be comma separated.

The greatest n digit number is denoted by "n" number of 9's occurring, like, the greatest 6 digit number is 999999 or the greatest 4 digit number is 9999. Note that although the greatest 4 digit number is 9999, it is not divisible by 4, but 9996 is divisible by 4.

Examples

If the following input is supplied to program:

2,5,8

Then, the output should be:

98,99995,99999992

Note: You should assume that input to the program is from console input (raw_input) 
'''

#各种运算符：包括 **，//
rets = []
for val in map(lambda x:int(x),raw_input().split(',')):
    for ret in range(10 ** val-1,0,-1):
        if ret % val == 0:
            rets.append(ret)
            break
print ",".join(map(lambda x:str(x),rets))