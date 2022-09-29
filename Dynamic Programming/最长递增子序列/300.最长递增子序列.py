#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
from typing import BinaryIO


class Solution:
    # 方法一：动态规划
    # 状态定义：
    # dp[i]的值代表nums以nums[i]结尾的最长子序列长度。
    #
    # 转移方程：
    # 设j∈[0,i)，考虑每轮计算新dp[i]时，遍历[0,i)列表区间，做以下判断：
    # （1）当nums[i] > nums[j]时：nums[i]可以接在nums[j]之后（此题要求严格递增），此情况下最长上升子序列长度为dp[j]+1；
    # （2）当nums[i] <= nums[j]时：nums[i]无法接在nums[j]之后，此情况上升子序列不成立，跳过。
    # 上述所有（1）情况下计算出的dp[j] + 1的最大值，为直到i的最长上升子序列长度（即dp[i]）。实现方式为遍历j时，每轮执行dp[i] = max(dp[i], dp[j] + 1)。
    # 
    # 初始状态：
    # dp[i]所有元素置1，含义是每个元素都至少可以单独成为子序列，此时长度都为1。
    # 
    # 返回值：
    # 返回dp列表的最大值，即可得到全局最长上升子序列长度。
    #
    # 复杂度分析： 
    # 时间复杂度 O(N^2) ： 遍历计算dp列表需O(N)，计算每个dp[i]需O(N)。   
    # 空间复杂度 O(N) ： dp列表占用线性大小额外空间。
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 方法二：动态规划+二分查找
    # 算法思想：
    # 方法一的时间复杂度为 O(N^2)，可以使用二分查找将时间复杂度降低为O(NlogN)。
    # 定义一个 tails 数组，其中 tails[i] 存储长度为 i + 1 的最长递增子序列的最后一个元素。对于一个元素 x，
    # （1）如果它大于 tails 数组所有的值，那么把它添加到 tails 后面，表示最长递增子序列长度加 1；
    # （2）如果 tails[i-1] < x <= tails[i]，那么更新 tails[i] = x。
    # 其中tails列表一定是严格递增的： 即当尽可能使每个子序列尾部元素值最小的前提下，子序列越长，其序列尾部元素值一定更大。
    # 
    # 举例：
    # 比如序列是78912345，前三个遍历完以后tail是789，这时候遍历到1，就得把1放到合适的位置，于是在tail二分查找1的位置，变成了189（如果序列在此时结束，因为res不变，所以依旧输出3），再遍历到2成为129，然后是123直到12345。
    #
    # 复杂度分析：
    # 时间复杂度O(NlogN)：遍历nums列表需O(N)，在每个nums[i]二分法需O(logN)。
    # 空间复杂度O(N)：tails列表占用线性大小额外空间。
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [0] * n
        length = 0
        for i in range(n):
            index = self.binary_search(tails,length,nums[i])
            tails[index] = nums[i]
            if index == length:
                length += 1
        return length 
    
    def binary_search(self, tails: List[int], end: int, key: int) -> int:
        start = 0
        while start < end:
            mid = start + (end - start) // 2
            if tails[mid] == key:
                return mid
            # 此处为end需要被赋值为mid，而不是mid-1
            elif tails[mid] > key:
                end = mid
            else:
                start = mid + 1
        return start
# @lc code=end

