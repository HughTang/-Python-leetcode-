#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    # 关于reduce()函数：https://www.runoob.com/python/python-func-reduce.html
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x,y: x ^ y, nums)
# @lc code=end

