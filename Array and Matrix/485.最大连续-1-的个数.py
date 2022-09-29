#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for v in nums:
            cur = cur + 1 if v == 1 else 0
            ans = max(ans,cur)
        return ans
# @lc code=end

