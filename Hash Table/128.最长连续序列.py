#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 列表判空
        if not nums:
            return 0
        # 将列表nums转换为集合，并筛除重复元素
        s = set(nums)
        longestLen = 0
        for v in s:
            curLen = 1
            # 为了减少时间复杂度，若v-1在集合中，则跳过本次循环
            if v-1 in s:
                continue
            # while来判断v+1是否在集合中，并将长度存储在curLen中
            while v+1 in s:
                curLen += 1
                v += 1
            # 使用max()函数来获得连续序列最大长度
            longestLen = max(longestLen,curLen)
        return longestLen
# @lc code=end

