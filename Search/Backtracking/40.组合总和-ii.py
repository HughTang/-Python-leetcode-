#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    # 回溯+剪枝
    # 数组candidates有序是深度优先遍历过程中实现「剪枝」的前提，因此需要先对candidates进行升序排序，
    # 重复的元素一定不是排好序以后相同的连续数组区域的第1个元素。也就是说，剪枝发生在：同一层数值
    # 相同的结点第2、3 ... 个结点，因为数值相同的第1个结点已经搜索出了包含了这个数值的全部结果，
    # 同一层的其它结点，候选数的个数更少，搜索出的结果一定不会比第1个结点更多，并且是第1个结点的真子集。
    # 注：本题去重的方法与「47.全排列-ii」一致，都是先排序后剪枝
    # 参考网址：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/ 
    #
    # 方法一：传入start参数的回溯+剪枝
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # 重点一：排序
        candidates.sort()
        self.dfs(candidates, target, ans, [], 0)
        return ans
    
    def dfs(self, nums: List[int], target: int, ans: List[List[int]], path: List[int], start: int):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return 
        for i in range(start, len(nums)):
            # 重点二：剪枝
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], ans, path+[nums[i]], i+1)
    
    # 方法二：不传入start参数的回溯+剪枝
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        # 重点一：排序
        candidates.sort()
        self.dfs(candidates, target, ans, [])
        return ans
    
    def dfs(self, nums: List[int], target: int, ans: List[List[int]], path: List[int]):
        if target < 0:
            return 
        if target == 0:
            ans.append(path)
            return 
        for i in range(len(nums)):
            # 重点二：剪枝，这里判断的是i>0，旨在保留对第一个元素的处理，而筛掉从第二个元素开始的重复元素DFS
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 为了代替start的作用，这里传入的是nums[i+1:]
            self.dfs(nums[i+1:], target-nums[i], ans, path+[nums[i]])
# @lc code=end

