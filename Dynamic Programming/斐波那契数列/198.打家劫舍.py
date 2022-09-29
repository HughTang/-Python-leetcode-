#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    # 用dp[i]表示前i间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：
    # dp[i]=max(dp[i−2]+nums[i],dp[i−1])
    # 边界条件为：
    # （1）dp[0]=nums[0]    只有一间房屋，则偷窃该房屋
    # （2）dp[1]=max(nums[0], nums[1])   只有两间房屋，选择其中金额较高的房屋进行偷窃

    # 方法一：顺推
    # 用dp[i]表示前i间房屋能偷窃到的最高总金额，空间复杂度为O(N)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        # 这里的dp[0]表示有1间可偷的情况
        dp[0] = nums[0]
        # 这里的dp[1]表示有2间可偷的情况
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

    # 方法二：顺推
    # 使用a和b两个变量存储dp[n-2]和dp[n-1]的值，空间复杂度为O(1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            # 借助中间变量
            # tmp = b
            # b = max(a + nums[i], b)
            # a = tmp
            
            # 不借助中间变量
            b, a = max(a + nums[i], b), b
        return b
# @lc code=end

