#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    # 该题的思路在于保存nums中所有可能的组合情况，因此本质上还是组合回溯问题
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, ans, [])
        return ans
    
    # DFS回溯
    def dfs(self, nums: List[int], ans: List[List[int]], path: List[int]):
        # 将每层递归的path实时结果进行保存，最终得到的ans就是最终结果列表
        ans.append(path)
        # 递归出口
        if not nums:
            return
        # for循环递归 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], ans, path+[nums[i]])
# @lc code=end

