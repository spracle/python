#coding=utf-8

import time

#翻转字符串
sStr1 = '12345'
print sStr1[::-1]

#查找字符串，查不到则结果为-1
sStr1 = 'abcdefg'
sStr2 = 'cde'
print sStr1.find(sStr2)

#比较字符串
sStr1 = "abc"
sStr2 = "def"
print cmp(sStr1,sStr2)

#连接字符串，容器中只能是字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)


#返回值为list
str = 'f-i-s-h-h-a-t'
print str.split("-")
print str.split("-",2)

#startswith 和 endswith,返回值是true 和 false
str = 'fishhat'
print str.startswith('fi')
print str.startswith('sh',2,4)
print str.endswith('hat')
print str.endswith('ha',4,6)

#replace函数，注意原字符串不会受到影响
str1 = 'AAAAABBBBBDDDDD'
str2 = str1.replace('A','a',3)
print str2
print str1

#时间函数
str1 = time.localtime()
str2 = time.strftime('%Y-%m-%d %X',str1)
print str1
print str2

#去空格
str.strip()    #去两边空格
str.lstrip()   #去左空格
str.rstrip()   #去右空格

#判断
str.isalpha()  #是否全字母
str.isdigit()  #是否全数字
str.islower()  #是否全小写
str.isupper()  #是否全大写