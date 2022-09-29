#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    # 二维动态规划问题
    # 题目理解：
    # 这里的插入、删除、替换操作都是相对于word1来说的，因此在定义状态和状态转移方程时都应该是对word1的插入、删除、替换操作 
    #
    # 状态定义：
    # 定义 dp[i][j] 表示将word1[0:i-1]转换为word2[0:j-1]的最少操作数。（注：word1[0:i-1]表示的是word1的第0个元素到第i-1个元素，两端都包含）
    # 之所以dp[i][j]的定义不是word1[0:i]和word2[0:j]，是为了方便当i = 0或者j = 0的时候，dp[i][j]表示的为空字符串到另外一个字符串的转化做少操作数，
    # 因此dp[i][0]需要初始化为i，dp[0][j]需要初始化为j
    #
    # 状态转移方程：
    # （1）当 word1[i-1] == word2[j-1] 时，说明word1的第i位与word2的第j位相等，所以只需要关注dp[i-1][j-1](即word1的0~i-2转换为word2的0~j-2的操作数)即可，因此状态转移方程为dp[i][j] = dp[i-1][j-1]
    # （2）当 word1[i-1] != word2[j-1] 时，说明word1的第i位与word2的第j位不相等，那么此时的状态dp[i][j]的取值分别对应下面三种操作，然后三者取最小值+1即可。
    #  ①替换操作：可能word1的0~i-1位置与word2的0~j-1位置的字符都相同，只是当前位置的字符不匹配，进行替换操作后两者变得相同，所以此时dp[i][j]=dp[i-1][j-1]+1(这个加1代表执行替换操作)
    #  ②删除操作：若此时word1的0~i-1位置与word2的0~j位置已经匹配了，此时多出了word1的i位置字符，应把它删除掉，才能使此时word1的0~i(这个i是执行了删除操作后新的i)和word2的0~j位置匹配，因此此时dp[i][j]=dp[i-1][j]+1(这个加1代表执行删除操作)
    #  ③插入操作：若此时word1的0~i位置只是和word2的0~j-1位置匹配，此时只需要在原来的i位置后面插入一个和word2的j位置相同的字符，使得此时的word1的0~i(这个i是执行了插入操作后新的i)和word2的0~j匹配得上，所以此时dp[i][j]=dp[i][j-1]+1(这个加1代表执行插入操作)
    # 
    # 对状态转移方程的举例理解：
    # 以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将word1的前5个字符转换为word2的前3个字符，也就是将horse转换为ros，因此有：
    # （1）替换操作：dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）
    # （2）删除操作：dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符
    # （3）插入操作：dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作
    #
    # 遍历方向与范围：
    # 由于 dp[i][j] 依赖与 dp[i - 1][j - 1] , dp[i - 1][j], dp[i][j - 1]，所以 i 和 j 的遍历顺序肯定是从小到大的。
    # 另外，由于当 i 或 j 取值为 0 的时候，dp[i][0]和dp[0][j]需要提前初始化，然后直接让 i 和 j 从 1 开始遍历即可。
    #
    # 最终返回结果：
    # 由于 dp[i][j] 表示将word1[0:i-1]转换为word2[0:j-1]的最少操作数，因此最终返回dp[-1][-1]
    # 
    # 复杂度分析：
    # 时间复杂度：O(mn)，其中m和n分别是字符串word1和word2的长度。二维数组dp有m+1行和n+1列，需要对dp中的每个元素进行计算。
    # 空间复杂度：O(mn)，其中m和n分别是字符串word1和word2的长度。创建了m+1行n+1列的二维数组dp。
    def minDistance(self, word1: str, word2: str) -> int:
        # 定义两个字符串长度和dp数组
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # 初始化i或j为0时dp[i][j]的值
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j
        
        # 从1开始遍历
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

