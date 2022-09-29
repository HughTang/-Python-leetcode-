#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        # 对nums的索引和值进行遍历
        for i,v in enumerate(nums):
            # 以v作为key，i作为value，然后去寻找target-v是否在哈希表中即可。
            if target - v in hashmap:
                return [hashmap[target - v],i]
            hashmap[v] = i
        return []
# @lc code=end

