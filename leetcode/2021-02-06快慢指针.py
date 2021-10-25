# coding:utf-8
"""
2021-02-06 Chenfeng Yuan 
来自微博用户：爱可可爱生活的分享
解法仅供参考
"""

'''这是一道真实的互联网面试题
Most candidates cannot solve this problem:

    Input: "aaaabbbcca"
    Output: [("a",4),("b",3),("c",2),("a",1)]

Write a function that converts the input to the output
I ask it in the screening interview and give it 25 minutes
How would you solve it?
'''

# 抖机灵的解法


def func(x):
    return [("a", 4), ("b", 3), ("c", 2), ("a", 1)]


print(func("aaaabbbcca"))

# 算法求解


def count_char(s):

    """典型的快慢指针解题"""

    result = []
    if s is None or len(s) == 0:
        return result
    if len(s) == 1:
        return [(s[0], 1)]
    slow, fast = 0, 1
    length = len(s)
    idx = 1
    while fast <= length - 1:
        if s[slow] == s[fast]:
            idx += 1
        else:
            result.append((s[slow], idx))
            idx = 1
        slow += 1
        fast += 1
    result.append((s[slow], idx))
    return result


print(count_char("aaaabbbcca"))
print(count_char("aaaabbbcc"))
print(count_char("aaaab"))
print(count_char("aaaabc"))
print(count_char("aaaa"))
print(count_char("a"))
print(count_char(""))
print("Hello World!你好，世界！")


def sum_(a, b):
    return a + b


print(sum_(1, 2))


