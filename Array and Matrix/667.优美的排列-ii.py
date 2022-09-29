#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#

# @lc code=start
class Solution:
    # 利用等差数组的特点，进行不停的反转即可：
    # 若n=8初始状态
    # 1 2 3 4 5 6 7 8
    # k=1        | 1 2 3 4 5 6 7 8 (不翻转，直接返回)
    # k=2        1 | 8 7 6 5 4 3 2
    # k=3        1 8 | 2 3 4 5 6 7
    # k=4        1 8 2 | 7 6 5 4 3
    # 总结规律：当k>1时,需要翻转的次数为k-1次，每次翻转保留前m(m = 1,2,3...k-1)个数，每次翻转都在原数组进行。
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1,n+1))
        for i in range(1,k):
            ans[i:] = ans[:i-1:-1]
        return ans
# @lc code=end

