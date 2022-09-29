#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    # 方法一：传入start参数的回溯
    # 本题与「77.组合」的解题方法差不多，只不过由于该题允许每个值多次使用，因此start参数在DFS递归时传入的是i，而不是i+1
    # 该题的关键点在于前面已经组合过的数值，以后除了本身就再也不会被组合到，因此需要传入start，start的值在上面也已经提过
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(candidates,target,ans,[], 0)
        return ans
    
    def dfs(self, candidates: List[int], target: int, ans: List[List[int]], path: List[int], start: int):
        # 两个递归出口
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return
        for i in range(start, len(candidates)):
            # target-candidates[i]是为了保证能达到递归出口
            # path+[candidates[i]]是为了保存实时路径结果
            # start传入i是为了保证能重复取到前一个值
            self.dfs(candidates, target-candidates[i], ans, path+[candidates[i]], i)
        
    # 方法二：不传入start参数的回溯
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(candidates,target,ans,[])
        return ans
    
    def dfs(self, nums: List[int], target: int, ans: List[List[int]], path: List[int]):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
        for i in range(len(nums)):
            # 这里直接传入nums数组下标i及后面的下标元素，使其能够达到start参数的效果，省略start参数
            self.dfs(nums[i:], target-nums[i], ans, path+[nums[i]])
# @lc code=end

