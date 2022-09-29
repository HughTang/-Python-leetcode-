#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # 该题与「279.完全平方数」十分相似，解题方法也一致
    # 
    # 方法一：动态规划（分割整数思想）（完全背包思想请见“完全背包”专题）
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp数组为全float('inf')
        dp = [float('inf')] * (amount + 1)
        # 为了使后面的顺推过程顺利进行，需要初始化dp[0]为0
        dp[0] = 0
        # 由于后面对coins的遍历是从小到大的，所以需要事先将coins排序
        coins.sort()
        # 从1开始循环
        for i in range(1, amount+1):
            for coin in coins:
                # 如果当前硬币数值比i大，则跳出循环，否则就执行状态转移方程
                if coin > i:
                    break
                dp[i] = min(dp[i], dp[i-coin] + 1)
        # 判断零钱是否兑换成功，若兑换成功，则返回dp[-1]，若没有兑换方案，则返回-1
        return dp[-1] if dp[-1] != float('inf') else -1
    
    # 方法二：BFS
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 添加amount<=0时的特殊情况处理
        if amount <= 0:
            return 0
        node = (amount, 0)
        queue = [node]
        visited = {node[0]}

        while queue:
            value, step = queue.pop(0)
            # 注意这里的if value >= coin必须要加上，因为价格必须要>=硬币面值才可以相减
            targets = [value-coin for coin in coins if value >= coin]
            for target in targets:
                if target == 0:
                    return step + 1
                if target not in visited:
                    queue.append((target, step+1))
                    visited.add(target)
        return -1
# @lc code=end

