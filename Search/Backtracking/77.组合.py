#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    # 方法一：带start参数的回溯
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(n, k, ans, [], 1)
        return ans

    # DFS回溯，添加了start参数，是为了保证其组合时不会重复组合已遍历的数值，因此start在每层递归过程中是会变化的
    def dfs(self, n: int, k: int, ans: List[List[int]], path: List[int], start: int):
        # 递归出口：递归深度为k
        if k == 0:
            ans.append(path)
            return 
        for i in range(start, n+1):
            # k-1是为了保证能达到递归出口
            # path+[i]是为了保存实时路径结果
            # start传入i+1是为了避免重复使用已递归过的值
            self.dfs(n, k-1, ans, path+[i], i+1)
    
    # 方法二：不带start参数的回溯
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        # 由于DFS传入的是搜索范围列表list(range(1,n+1))，因此可以直接在DFS递归过程中对该列表进行下标约束，因此可以省略原有的start参数
        self.dfs(list(range(1,n+1)), k, ans, [])
        return ans

    # DFS参数分析：nums标识搜索范围列表，k标识递归深度，ans存储最终结果列表，path存储实时路径结果
    def dfs(self, nums: List[int], k: int, ans: List[List[int]], path: List[int]):
        # 递归出口：递归深度为k
        if k == 0:
            ans.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, ans, path+[nums[i]])    
# @lc code=end

