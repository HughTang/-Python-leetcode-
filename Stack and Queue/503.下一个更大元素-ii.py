#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    '''
        该题与「739.每日温度」十分相似，且使用的都是单调栈的思想，将nums
    数组的下标单调存放在栈中，不过需要注意的是，为了保证循环数组的最后一个
    元素能够再次遍历数组到n-1的位置，所以需要遍历n + n-1 = 2*n-1次。此外，
    为了避免数组下标溢出，需要提前初始化为[-1]*len(nums)个元素。
    '''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 利用len()获取循环数组长度
        n = len(nums)
        # 初始化结果数组num为len(nums)个-1
        num = [-1] * n
        # 初始化栈
        stack = list()
        # 循环遍历下标2*n-1次
        for i in range(2*n-1):
            # 循环条件为：栈不为空且找到了下一个更大的元素
            while stack and nums[stack[-1]] < nums[i % n]:
                # 出栈并赋值
                num[stack.pop()] = nums[i % n]
            # 不符合循环条件则进栈
            stack.append(i % n)
        # 返回结果列表
        return num
# @lc code=end

