#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    # 重复的数：sum(nums) - sum(set(nums))
    # 缺失的数：sum(list(range(1, len(nums) + 1))) - sum(set(nums))
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(list(range(1, len(nums) + 1))) - sum(set(nums))]
# @lc code=end

