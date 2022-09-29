#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 分割多空格字符串的方法有如下两种。
        # 方法一：split()函数在不设置参数的情况下可以默认匹配
        # 多个空格并且按照空格分隔的非空元素返回一个列表。
        # 方法二：用filter函数对split(' ')的结果进行过滤，即
        # inputwords = filter(None,str.split(' '))
        inputwords = s.split()
        # 对列表中每个元素进行反转，并将列表反转
        inputwords = inputwords[::-1]
        # 使用join()函数对列表中每个元素以空格为分隔进行组合
        output = ' '.join(inputwords)
        return output 
        # 上面的代码也可以简写为一行
        # return ' '.join(s.split()[::-1])   
# @lc code=end

