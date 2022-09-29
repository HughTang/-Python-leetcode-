#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    # 本题要求判断两个字符串包含的字符类型和个数是否完全相同
    # 注：方法一代码量多，但时间效率高；方法二代码量少，但时间效率低
    #
    # 方法一：建立两个字典，key为字母，value为个数
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict()
        dic1 = dict()
        for i in s:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = int(1)
        for i in t:
            if i in dic1:
                dic1[i] = dic1[i] + 1
            else:
                dic1[i] = int(1)
        return dic == dic1
    
    # 方法二：用数组存储ASCII之差,ord()函数的作用就是获取字符对应的 ASCII 数值
    def isAnagram(self, s: str, t: str) -> bool:
        num = [0] * 26
        for c in s:
            num[ord(c) - ord('a')] += 1
        for c in t:
            num[ord(c) - ord('a')] -= 1
        return set(num) == {0}
# @lc code=end

