#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    # 算法思想：
    # （1）定义状态：dp[i]表示从nums[0]到nums[i]，并且以nums[i]为结尾的 等差数列子数组 的数量。
    # （2）状态转移方程：dp[i] = dp[i-1] + 1 if nums[i]-nums[i-1]== nums[i-1]-nums[i-2] else 0
    # （3）解释：如果nums[i]能和nums[i-1]、nums[i-2]组成等差数列，则以nums[i-1]结尾的等差数列子数组均可以nums[i]结尾，
    # 且多了一个新等差数列[nums[i],nums[i-1],nums[i-2]]。因为递增子区间不一定以最后一个元素为结尾，可以是任意一个元素结尾，
    # 因此需要返回 dp 数组累加的结果。
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化dp数组，且其中包含了dp[0]、dp[1]赋值为0的操作
        dp = [0] * n
        for i in range(2,n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
# @lc code=end

