#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    # 方法一：哈希表
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for i,v in enumerate(numbers):
            if target - v in dic:
                return [dic[target-v]+1, i+1]
            dic[v] = i
        return []
    
    # 方法二：双指针，效率比方法一的哈希表法低
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            if num > target:
                right -= 1
            elif num < target:
                left += 1
            else:
                return [left+1, right+1]
        return []
# @lc code=end

