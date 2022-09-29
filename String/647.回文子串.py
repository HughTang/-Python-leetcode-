#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    '''
        使用中心拓展法，枚举每一个可能的回文中心，然后用两个指针
        分别向左右两边拓展，当两个指针指向的元素相同的时候就拓展，
        否则停止拓展。
        由于回文子串的长度可能是奇数或者偶数，因此需要分两种情况
        讨论，即分别调用两次不同参数的拓展函数extendSubstrings()
        然后返回并统计所有符合条件的子串数量。
    '''
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            # 奇数长度回文子串
            ans += self.extendSubstrings(s,i,i)
            # 偶数长度回文子串
            ans += self.extendSubstrings(s,i,i+1)
        return ans
    # 该函数用于统计给定某个特定回文中心后的回文子串个数
    def extendSubstrings(self, s: str, start: int, end: int) -> int:
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1
        return count    
# @lc code=end

