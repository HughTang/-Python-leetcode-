#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = dict()
        # 将nums中的所有元素及相同元素个数存放在hashmap中
        for v in nums:
            if v in hashmap:
                hashmap[v] += 1
            else:
                hashmap[v] = int(1)
        ans = 0
        # 在hashmap中逐个寻找每个元素x及x+1是否在hashmap中
        # 然后引入max()函数获得ans最大的结果
        for x in hashmap:
            if x+1 in hashmap:
                ans = max(ans,hashmap[x] + hashmap[x+1])
        return ans
# @lc code=end

