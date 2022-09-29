#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    # 该问题属于求解顺序的完全背包问题，对物品的迭代应该放在最里层，
    # 对背包的迭代放在外层，只有这样才能让物品按一定顺序放入背包中。
    #
    # 状态定义：
    # dp[i]表示s的长度为i时的拆分成功与否的结果
    # 
    # 状态转移方程（l为每个单词的长度）：
    # dp[i] = dp[i] or dp[i-l]
    #
    # 时间复杂度分析：
    # 时间复杂度：O(NM)，N为s的长度，M为wordDict的长度。
    # 空间复杂度：O(N)，N为s的长度，只借助了dp列表的空间。
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[0]为s长度为0时，只需要不从wordDict里面取单词就能满足要求，因此初始化为True，其他初始化为False
        dp = [True] + [False] * n
        # 外层循环为背包循环，且循环下标需要从1开始，因此dp[1]表示s的长度为1且s下标为0的情况下的结果
        for i in range(1, n+1):
            # 内层循环为物品循环
            for word in wordDict:
                # l是物品所占容量，即单词的长度
                l = len(word)
                # 如果背包容量>=物品所占容量（s长度>=word长度），并且s中包含word，则执行状态转移方程
                if i >= l and word == s[i-l:i]:
                    dp[i] = dp[i] or dp[i-l]
            # 如果某轮循环后存在目标顺序序列，即dp[-1]为True时，则返回True
            if dp[-1]:
                return True
        # 否则，返回False
        return False
# @lc code=end

