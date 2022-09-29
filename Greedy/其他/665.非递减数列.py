#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    # 解题思路：
    # 由于该题中要求数列最多只能改变一个元素，因此整个数组如果想变成非递减数列，
    # 就最多只能出现一次nums[i] > nums[i+1]的情况。此外，nums[i]的修改还需要
    # 保证i前后序列维持非递减，所以分为修改nums[i]或者修改nums[i+1]两种情况。
    # 这里我们直接将nums[i]或nums[i+1]删除，然后进行排序，并与剩下的列表进行对比，
    # 就可以验证该序列在删除特定元素后会不会依然保持非递减。
    # 
    # 注意事项：
    # 由于nums[i:]或nums[:i]用法中i的值可以超过列表的下标长度，因此可以使用该方法
    # 将特定元素删除，但是如果使用del nums[i]、nums.pop(i)的方法删除元素，如果i的
    # 值超过列表的下标，则会报错，因此在本题中不可以使用该方法删除元素。
    def checkPossibility(self, nums: List[int]) -> bool:
        # i用于标识遍历的列表下标
        i = 0
        while i < len(nums)-1:
            # 如果符合nums[i] > nums[i+1]
            if nums[i] > nums[i+1]:
                break
            i += 1
        # 情况一：删除nums[i]
        nums1 = nums[:i] + nums[i+1:]
        # 情况二：删除nums[i+1]
        nums2 = nums[:i+1] + nums[i+2:]
        
        # 验证上述两种情况下列表是否存在非递减的情况
        return nums1 == sorted(nums1) or nums2 == sorted(nums2)

# @lc code=end

