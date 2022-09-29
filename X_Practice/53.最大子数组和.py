#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # k = [[1,2],[1,2],[2,2]]
        s = input().split('],[')
        s[0] = s[0][2:]
        s[-1] = s[-1][:-2]
        nums = list()
        for x in s:
            nums.append(x.split(','))
        print(nums)
# @lc code=end

