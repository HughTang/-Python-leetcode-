#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    # 具体思路借鉴官方解答，这里将两个数组改为了left和right变量来存储中间结果
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 将output数组元素全部初始化为1
        output = [1] * n
        # left变量用于保存从左到右的每次乘积结果，初始化为1
        left = 1
        # 从左到右遍历数组，进行乘积计算
        for i in range(1,n):
            # left存储上一个left与num[i-1]的乘积
            left *= nums[i-1]
            # 将乘积保存在output数组中
            output[i] *= left
        # right变量用于保存从右到左的每次乘积结果，初始化为1
        right = 1
        # 从右到左遍历数组，进行乘积计算，这里用到了reversed
        for i in reversed(range(n-1)):
            # right存储上一个right与num[i+1]的乘积
            right *= nums[i+1]
            # 将乘积与output数组中的值相乘
            output[i] *= right
        # 返回最终数组output
        return output
# @lc code=end

