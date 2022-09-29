#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    # 该题与剑指offer第10题一致，与leetcode第一题和NC125为同一类型的题目
    # 重点在于dic的初始化及`前缀和`的思路
    # 即求出前i个数的和（sum），然后找sum-k有没有在之前的前缀和里出现过。如果有，从i这个位置到之前sum-k出现的位置，这个片段之和就是k。
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 字典中的key为nums的前i项和，value为该和出现的次数，初始化为{0:1}是因为要涵盖数组中的某个值正好等于k的情况
        dic = {0:1}
        # ans存储最终结果，cur存储前i项和
        ans = cur = 0
        for v in nums:
            cur += v
            # 如果在dic中找到cur-k的值，则将ans再加上cur-k出现的频次，找不到就累加0
            ans += dic.get(cur-k, 0)
            # 如果cur已经在dic中，则将其频次+1，否则键值对初始化为cur:1
            dic[cur] = dic.get(cur, 0) + 1
        # 返回最终结果
        return ans
# @lc code=end

