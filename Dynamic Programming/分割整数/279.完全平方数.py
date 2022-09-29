#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    # # 该题在动态规划专题的“分割整数”、“完全背包”以及搜索的“BFS”专题中都出现过
    # 该题与「322.零钱兑换」十分相似，解题方法也一致
    # 
    # 方法一：动态规划
    # 
    # 状态定义：
    # dp[i]表示n=i时，可拆分成的最少完全平方数
    #
    # 状态转移方程：
    # dp[i] = min(dp[i], dp[i-j]+1)
    # 其中j为小于i的完全平方数列表元素，min中的两种情况分别是：
    # （1）dp[i]表示不拆分出j的情况
    # （2）dp[i-j]+1表示拆分出j的情况
    # 或者，min中的dp[i]也可以理解为找到所有嵌套循环后所得dp[i]中间结果的最小值
    #
    # 复杂度分析：
    # 时间复杂度为O(N*sqrt(N))，空间复杂度为O(N)
    # 方法一：传统动态规划
    def numSquares(self, n: int) -> int:
        # 获取小于n的完全平方数列表
        squares = [i*i for i in range(1, int(n**0.5+1))]
        # 初始化dp数组时，不全初始化为0，而是初始化为最坏的情况，即每个数都拆分成1，该初始化方法可以使下面的循环从4开始，并且省略循环中初始化dp[i]=i的步骤
        dp = [i for i in range(n+1)]
        # 从4开始循环，因为dp[0],dp[1],dp[2],dp[3]都已初始化
        for i in range(4, n+1):
            # dp[i] = i
            for j in squares:
                # 如果当前完全平方数比i大，则跳出循环，否则就执行状态转移方程
                if j > i:
                    break
                dp[i] = min(dp[i], dp[i-j] + 1)
        # 返回最终结果
        return dp[-1]

    # 方法二：完全背包动态规划
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        squares = [i*i for i in range(1, int(n**0.5)+1)]
        # 外层循环为物品列表
        for v in squares:
            # 内层循环为背包容量，正序
            for i in range(v,n+1):
                dp[i] = min(dp[i], dp[i-v] + 1)
        return dp[-1]
    
    # 方法三：BFS，该题以下步骤思路可以作为BFS的模板步骤进行使用
    def numSquares(self, n: int) -> int:
        # 初始化节点，前面的n为值，后面的0为step，可以理解为步骤或者到达路径长度
        node = (n, 0)
        # 初始化队列
        queue = [node]
        # 初始化已访问集合，避免队列中插入重复的值
        visited = {node[0]}

        while queue:
            # 弹出队首节点
            value, step = queue.pop(0)
            # 对弹出的节点进行操作
            targets = [value-i*i for i in range(1, int(value**0.5+1))]
            # 判断一堆节点是否符合业务条件，若符合，则return；若不符合，且不在已访问集合，则追加到队尾，并加入已访问集合
            for target in targets:
                if target == 0:
                    return step + 1
                if target not in visited:
                    queue.append((target,step+1))
                    visited.add(target)
        # 若以上遍历完成仍未return，返回-1
        return -1
# @lc code=end

