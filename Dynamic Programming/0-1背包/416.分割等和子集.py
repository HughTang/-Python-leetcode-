#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    # dp[i]表示背包容量为i时，i是否可以通过数组中的某个子集元素之和得到
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        # 如果数组元素之和为奇数，则不可能分成两个和相同的子集，直接返回False
        if w & 1:
            return False
        # w减半，这里使用的是无符号右移，w//=2亦可
        w >>= 1
        
        # 初始化dp，其中dp[0]需要初始化为True
        # dp = [True] + [False] * w
        dp = [False] * (w + 1)
        dp[0] = True
        
        # 可优化的地方
        for v in nums:
            for i in range(w,v-1,-1):
                dp[i] = dp[i] or dp[i-v]
        
        # 返回最终结果
        return dp[-1]
    
    # 优化后
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        if w & 1:
            return False
        w >>= 1
        dp = [True] + [False] * w
        
        # 在某次循环中将dp[-1]已经为True时，说明此时已经找到了合适的子集之和为w，
        # 可以直接跳出循环并返回True
        for v in nums:
            for i in range(w,v-1,-1):
                dp[i] = dp[i] or dp[i-v]
            if dp[-1]:
                return True
        
        # 循环结束后未结束，则说明不存在满足条件的子集，返回False
        return False
# @lc code=end

