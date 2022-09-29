#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # 滑动窗口
    # 用字典lookup的key来记录字符值，value保存该值上一次出现的下标。从而可以通过key来判断字符值是否重复，用value来获取该重复字符的下标。
    # 定义start不动，i一直向后移动，并处理以下两种情况：
    # 1）当s[i]是重复字符时，还要进一步判断start是否在s[i]的值上一次（不是第一次，因为该字符值的下标会实时更新）出现的下标的前面或相等，则start会重新赋值为上一个重复字符的位置的后一位。
    # 2）当s[i]不是重复字符时，则记录获取最长实时长度，即在max(max_length, i-start+1)
    # 每轮循环都要实时更新lookup字典的字符值所对应的value最新下标
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化start初始下标与最大长度为0
        start = ans = 0
        # 初始化lookup字典
        lookup = dict()
        for i,c in enumerate(s):
            # 当c是重复字符且start在此字符上一次出现的值的下标前面或相同
            if c in lookup and start <= lookup[c]:
                # start重新赋值为上一个重复字符的位置的后一位
                start = lookup[c] + 1
            else:
                # 当s[i]不是重复字符时，记录获取最长实时长度
                ans = max(ans, i - start + 1)
            # 实时更新字典，每个字符值的下标都是i及i之前上一次出现的下标
            lookup[c] = i
        # 返回最大长度
        return ans
# @lc code=end

