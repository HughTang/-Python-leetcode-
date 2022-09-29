#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

# @lc code=start
class Solution:
    # 解题思路：分块时每个块的最大元素正好是当前块最右边元素的下标，以这个为依据即可轻松解决该题。
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # length = 0
        # i = 0
        # while i < len(arr):
        #     j = arr.index(i)
        #     v = i+1
        #     while v <= j:
        #         if v in arr[:j+1]:
        #             v += 1
        #         else:
        #             j += 1
        #     i = j + 1
        #     length += 1
        # return length
        length = 0
        right = arr[0]
        for i in range(len(arr)):
            right = max(right, arr[i])
            if right == i:
                length += 1
        return length
# @lc code=end

