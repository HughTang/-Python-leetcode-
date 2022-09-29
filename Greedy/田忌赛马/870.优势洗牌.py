#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
    # 田忌赛马问题：
    # 把数组nums1看作田忌的马，把数组nums2看作齐王的马，其中数组元素值的大小看作马跑的快慢
    # 如果田忌最快的马比齐王最快的马跑的快，那么就用田忌最快的马和齐王最快的马比赛
    # 如果田忌最快的马比齐王最快的马跑的慢，那么就用田忌最慢的马和齐王最快的马比赛
    # 
    # 这里由于齐威王的nums2不能改变位置，因此定义一个order列表来存储nums2以值为关键字的下表降序排列结果，
    # nums1重新更改为可以在两侧弹出的deque，并将值按照降序排列，然后初始化ans为[0]*n，
    # 最后遍历order中的下标，如果nums1最右侧的最大值比nums[i]大，就将最大值弹出，否则就将左侧的最小值弹出，
    # 最后将弹出的结果赋为ans[i]的值，最后ans存储的就是最优的排列结果。

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        # 定义一个order列表来存储nums2以值为关键字的下表降序排列结果
        order = sorted(range(n), key = lambda x: nums2[x], reverse=True)
        # nums1重新更改为可以在两侧弹出的deque，并将值按照降序排列
        nums1.sort()
        # 初始化ans
        ans = [0] * n
        # 依次遍历order的元素i，这个i代表了nums2中从大到小的值的下标
        for i in order:
            # 如果nums1最右侧的最大值比nums[i]大，就将最大值弹出，否则就将左侧的最小值弹出，然后将弹出的结果赋为ans[i]的值
            ans[i] = nums1.pop() if nums1[-1] > nums2[i] else nums1.pop(0)
        # 返回ans
        return ans
# @lc code=end

