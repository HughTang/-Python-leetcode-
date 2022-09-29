#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    # 方法一：动态规划
    # P表示需要+号的子集，S表示需要-号的子集
    # 由于P - S = target
    # 故 P - S + P + S = target + P + S
    # 即 2 * P = target + sum(nums)
    # 所以 P =  [target + sum(nums)] // 2
    # 因此该问题就可以转化为寻找nums中是否存在子集P，
    # 使其元素之和等于[target + sum(nums)] // 2
    # 那本题思路即可转换为「416.分割等和子集」的解题思路
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        w = sum(nums)
        # sum(nums)小于target的绝对值，或者[target + sum(nums)]不能与2整除，则返回0
        if target > w or target < -w or (w + target) & 1 == 1:
            return 0
        # w改为[target + sum(nums)] // 2
        w = (w + target) >> 1
        # dp[i]表示nums中存在元素之和为i的子集总数，初始化为[1] + [0] * w
        dp = [1] + [0] * w
        for v in nums:
            for i in range(w,v-1,-1):
                # 状态转移公式为dp[i] += dp[i-v]
                dp[i] += dp[i-v]
        # 返回dp的最后一个元素 
        return dp[-1]
    
    # 方法二：DFS，不推荐，会超时
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.findTarget(nums, 0, target)
    
    def findTarget(self, nums: List[int], start: int, target: int) -> int:
        if len(nums) == start:
            return 1 if target == 0 else 0
        return self.findTarget(nums, start+1, target+nums[start]) + self.findTarget(nums, start+1, target-nums[start])
# @lc code=end

