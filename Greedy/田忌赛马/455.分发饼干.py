#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    # 贪心思路：局部最优 -> 全局最优
    # （1）给一个孩子的饼干应当尽量小并且又能满足该孩子，这样大饼干才能拿来给满足度比较大的孩子。
    # （2）因为满足度最小的孩子最容易得到满足，所以先满足满足度最小的孩子。
    # 时间复杂度为O(NlogN)，空间复杂度为O(1)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # ans存储最终结果
        ans = 0
        # 对孩子胃口值和饼干尺寸列表进行排序
        g.sort()
        s.sort()
        # i，j初始化为0，分别代表孩子胃口值g猎列表的下标和饼干尺寸s的下标
        i, j = 0 ,0
        # while 下标<最大长度 循环体
        while i < len(g) and j < len(s):
            # 给一个孩子的饼干尽量小并且又能满足该孩子时，ans++，i++
            if g[i] <= s[j]:
                ans += 1
                i += 1
            # 不管饼干满不满足孩子，饼干尺寸列表s下标都要+1
            j += 1
        # 返回最终结果
        return ans
# @lc code=end

