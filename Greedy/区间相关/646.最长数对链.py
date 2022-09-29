#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    # 注：该题目为 动态规划 专题题目，但是由于存在效率更高的贪心算法解法，因此作者加入到了Greedy题目中。
    # 方法一：动态规划
    # 只需要将pairs提前按照第一个元素升序，其他思路与「300.最长递增子序列」算法思想相同
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs or len(pairs) == 0:
            return 0
        pairs.sort(key=lambda elem: elem[0])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    # 方法二：贪心算法(效率更高)
    # 算法思想：
    # 需要首先将pairs中的列表按照第二个元素升序，然后运用Greedy中的区间相关算法解题即可
    # 
    # 复杂度分析：
    # 时间复杂度：O(NlogN)，其中 N 是数对的长度。排序步骤复杂度最高，其余步骤是线性复杂度。
    # 空间复杂度：O(N)。使用常数空间存储 cur 和 ans，但是排序的空间复杂度为 O(N)，这与使用的语言有关。
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda elem: elem[1])
        cur, ans = float('-inf'), 0
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1
        return ans   
# @lc code=end

