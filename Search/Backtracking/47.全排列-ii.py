#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    # 本题是第46题的变体，只不过需要去重，所以需要提前对nums排序，在DFS回溯时进行重复判断
    # 本题的去重方法与「40.组合总和-ii」一致，都是先排序后剪枝
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 关键点1：对nums排序
        nums.sort()
        self.dfs(nums,ans,[])
        return ans
    
    # DFS回溯，path是回溯最重要的参数
    def dfs(self, nums: List[int], ans: List[List[int]], path: List[int]):
        if not nums:
            ans.append(path)
            return 
        for i in range(len(nums)):
            # 如果相邻元素重复，则跳过（剪枝）
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], ans, path+[nums[i]])
# @lc code=end

