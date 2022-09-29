#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = list()
        for i in range(num+1):
            ans.append(bin(i).count('1'))
        return ans
# @lc code=end

