#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    '''
    方法一：
        该题需要判断s与t的「双射」关系，即s的任意一个字符被t中
        唯一的字符对应，同时t的任意一个字符被s中唯一的字符对应。
        因此需要维护两张哈希表，并且使用zip()进行多序列遍历。
    '''
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = dict()
        # 判断s到t的「单射」关系
        for i,j in zip(s,t):
            if i in dic and dic[i] != j:
                return False
            dic[i] = j
        # 为了节省空间使用，将原字典清空
        dic.clear()
        # 判断t到s的「单射」关系
        for i,j in zip(t,s):
            if i in dic and dic[i] != j:
                return False
            dic[i] = j
        return True
    
    # 方法二
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
# @lc code=end

