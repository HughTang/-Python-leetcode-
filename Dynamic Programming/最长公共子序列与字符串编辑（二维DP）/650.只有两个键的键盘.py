#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    # 方法一：分解质因数（递归）
    # （1）若p为质数，那么只能复制1次之后，再粘贴p-1次，即f(p) = 1 + p - 1 = p
    # （2）若p为合数，对于p = p1 * p2（p1和p2都是质数），有三条途径可以得到p个'A'：
    #  ①在复制1次'A'的基础上，一直粘贴，这是操作数最多的情况，即f(p)=p 
    #  ②在复制1次'A'的基础上，粘贴p1-1次得到p1，然后复制p1个'A'，粘贴p2-1次，即f(p)=(1) + (p1 - 1) + (1) + (p2 - 1) = p1 + p2
    #  ③在复制1次'A'的基础上，粘贴p2-1次得到p2，然后复制p2个'A'，粘贴p1-1次，即f(p)=(1) + (p2 - 1) + (1) + (p1 - 1) = p2 + p1
    # 因此当p为合数时，f(p) = f(p1*p2*p3...pn) = p1 + p2 + p3 +...+ pn
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i + self.minSteps(n//i)
        return n
    
    # 方法二：动态规划
    # dp[i]表示输出i个'A'时所使用的最少操作次数 
    def minSteps(self, n: int) -> int:
        # dp[i]全部初始化为i，及在复制1次'A'的基础上，一直粘贴，这是操作数最多的情况
        dp = [i for i in range(n+1)]
        # 为了满足题目要求，当只需要一个'A'时，不需要任何操作，因此dp[1]初始化为0
        dp[1] = 0
        # 从2开始遍历
        for i in range(2, n+1):
            # 这里也是从25开始遍历，是为了找i的（质）因数
            for j in range(2, int(i ** 0.5) + 1):
                # 若j为i的（质）因数，则进行状态转移
                if i % j == 0:
                    dp[i] = dp[j] + dp[i//j]
                    # break
        # 最后输出结果dp[-1]（dp[n]）
        return dp[-1]
# @lc code=end

