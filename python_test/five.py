#coding=utf-8
"""
Write a program which will convert the given RGB input values into the corresponding hexadecimal values preceded with a # sign.

A single input sequence will be provided, consisting of RGB values separated by "-". Each RGB combination will be separated by ",". The outputs should be comma separated and in uppercase. Also, it should be checked if a color value is greater than 255. In such a case, the output for the corresponding combination should be given as INVALID.

Note: Number 10, which has a hexadecimal value of A, must be represented as "0A" and not as "A". The same rule applies to other single digit hexadecimal numbers.

Example

Suppose the following input sequence is supplied to the program:

12-13-14,45-156-23,234-234-256

The output of the program should be:

#0C0D0E,#2D9C17,INVALID

Note: In case of input data being supplied to the question, it should be assumed to be a console input.

"""

#方法1
input_data = raw_input()

cal_rgb_list = []
rgb_list = input_data.split(",")

for rgb in rgb_list:
    rgb_t = rgb.split("-")
    cal_rgb_list.append(rgb_t)

result = ""
for rgb in cal_rgb_list:
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    if r > 255 or g >255 or b > 255:
        result = result + "," + "INVALID"
        continue
    t_rgb=(r, g, b)
    result = result + "," +  "#" + "".join(map(chr, t_rgb)).encode('hex')

result = result.upper()
result = result[1:]
print result

#方法2,记住ord 和 chr
ret = []
for val in raw_input().split(','):
    rgbList = val.split('-')
    if int(rgbList[0]) > 255 or int(rgbList[1]) > 255 or int(rgbList[2]) > 255:
        ret.append("INVALID")
    else:
        ret.append('#' + "".join(map(chr,map(lambda x:int(x),rgbList))).encode('hex'))

print ",".join(ret).upper()

input()
