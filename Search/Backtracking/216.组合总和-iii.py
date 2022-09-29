#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    # 本题涉及的解法是前面几个组合回溯问题的解法结合
    # 方法一：带start参数的回溯
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 处理特殊情况
        if k <= 0 or n < 0:
            return [[]]
        ans = []
        self.dfs(k,n,ans,[], 1)
        return ans

    # DFS参数分析：k标识递归深度，n标识目标结果，ans存储最终结果列表，path存储实时路径结果，start存储搜索列表的起始下标
    def dfs(self, k: int, n: int, ans: List[List[int]], path: List[int], start: int):
        # 递归出口1：递归深度大于k或当前路径和大于n，由于k和n是一路递减过来的，所以这里判断的是两者是否小于0
        if k < 0 or n < 0:
            return 
        # 递归出口2：递归深度为k且路径和等于n，此时递减过来的k和n都应该等于0
        if k == n == 0:
            ans.append(path)
            return 
        # DFS递归回溯，k和n递减，path加入当前值，start取i+1（避免取重复元素）
        for i in range(start,10):
            self.dfs(k-1, n-i, ans, path+[i], i+1)

    # 方法二：不带start参数的回溯
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 处理特殊情况
        if k <= 0 or n < 0:
            return [[]]
        ans = []
        # 由于DFS传入的是搜索范围列表list(range(1,10))，因此可以直接在DFS递归过程中对该列表进行下标约束，因此可以省略原有的start参数
        self.dfs(list(range(1,10)), n, k, ans, [])
        return ans

    # DFS参数分析：nums标识搜索范围列表，n标识目标结果，k标识递归深度，ans存储最终结果列表，path存储实时路径结果
    def dfs(self, nums: List[int], n: int, k: int, ans: List[List[int]], path: List[int]):
        # 递归出口1：递归深度大于k或当前路径和大于n，由于k和n是一路递减过来的，所以这里判断的是两者是否小于0
        if k < 0 or n < 0:
            return 
        # 递归出口2：递归深度为k且路径和等于n，此时递减过来的k和n都应该等于0
        if k == n == 0:
            ans.append(path)
            return 
        # DFS递归回溯，nums取nums[i+1:]，k和n递减，path加入当前值
        for i in range(len(nums)):
            self.dfs(nums[i+1:], n-nums[i], k-1, ans, path+[nums[i]])
# @lc code=end

