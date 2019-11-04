#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 1、请将 "1,2,3"，变成 ["1","2","3"]

# 方法1
a = '1,2,3'
print(a.split(','))

# 方法2 遍历一下
a = '1,2,3'
sep = ','
result = []
for i in range(len(a)):
    if a[i] == sep:
        continue
    result.append(a[i])
print(result)

# 阿飞老师的评论
# 方法一就不讲了，是python自带的切割函数，比较简单。
# 方法二思路是对的，但是存在一点缺陷。这里要求你把字符串切割开来，给出的是单个字符的分隔符以及单个字母的字符串。
# 如果字符有两个，或者切割符有两个呢？第二种方法是否还适合，怎么改进？可以思考一下，将下面的三串字符串切割一下。

b = '12,23,34,45'
c = '12, 23, 34, 45'
d = '12, 2, 34, 56'
