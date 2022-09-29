#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    # 方法一：递归
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        ans = list()
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                ans.append([nums[i]]+j)
        return ans
    
    # 方法二：回溯
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums,ans,[])
        return ans
    
    # DFS回溯，path为最重要的参数，代表了每个DFS路径的实时结果记录
    def dfs(self, nums: List[int], ans: List[List[int]], path: List[int]):
        if not nums:
            ans.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], ans, path+[nums[i]])
# @lc code=end

