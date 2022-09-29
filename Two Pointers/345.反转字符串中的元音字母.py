#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    # 方法一：双指针法，算法性能比方法二好
    def reverseVowels(self, s: str) -> str:
        # 使用集合来存储所有的元音字母
        # 注意：存储这种判别元素时，尽量用字典或集合，不要用列表、元组和字符串，因为集合和字典的存取时间复杂度为O（1），效率更高。
        vowels = {'a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I'}
        # res列表用于s中依次出现的每个字符
        res = list(s)
        # 初始化左下标指针变量left为0
        left = 0
        # 初始化右下标指针变量right为len(s)-1
        right = len(s) - 1
        # 在循环过程中对res的左右元音字母进行交换
        while left < right:
            # left与right所对应下标的字母都是元音字母，则交换两者，并使left右移，right左移
            if res[left] in vowels and res[right] in vowels:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            # 下面的两个循环同时完成了两者中只有一个元音字母和两者都不是元音字母的指针移动处理
            elif res[left] not in vowels:
                left += 1
            elif res[right] not in vowels:
                right -= 1
        # 最后调用“字符串.join(元素列表) -> str”的方法返回最终结果
        return ''.join(res)

    # 方法二：存储下标法
    def reverseVowels(self, s: str) -> str:
        # 使用集合来存储所有的元音字母
        vowels = {'a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I'}
        # res列表用于s中依次出现的每个字符
        res = list(s)
        # ls用来依次存储res中出现的元音字母及其下标
        ls = list()
        # 遍历res，按照[下标，元音字母]的列表形式存入列表ls中
        for i,c in enumerate(s):
            if c in vowels:
                ls.append([i,c])
        # 正向遍历ls中存储的下标，反向遍历ls中存储的元音字母，从而修改res中的元音字母
        for i,j in zip(ls,ls[::-1]):
            res[i[0]] = j[1]
        # 最后调用“字符串.join(元素列表) -> str”的方法返回最终结果
        return ''.join(res)
# @lc code=end

