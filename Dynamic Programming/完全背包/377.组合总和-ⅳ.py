#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    # 涉及顺序的完全背包问题，所求问题为组合数，解题方法借鉴「139.单词拆分」
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1,target+1):
            for v in nums:
                if i >= v:
                    dp[i] += dp[i-v]
        return dp[-1]
# @lc code=end

