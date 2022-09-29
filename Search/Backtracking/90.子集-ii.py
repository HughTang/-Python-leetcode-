#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    # 回溯+剪枝，本题与「40.组合总和-ii」方法几乎相同，都是要用到剪枝的思想
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums数组有序是剪枝的前提
        nums.sort()
        ans = []
        self.dfs(nums, ans, [])
        return ans
    
    def dfs(self, nums: List[int], ans: List[List[int]], path: List[int]):
        ans.append(path)
        if not nums:
            return
        for i in range(len(nums)):
            # 剪枝操作，这里判断的是i>0，旨在保留对第一个元素的处理，而筛掉从第二个元素开始的重复元素DFS
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], ans, path+[nums[i]])
# @lc code=end

