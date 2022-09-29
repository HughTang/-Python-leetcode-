#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    # 方法一：双指针法（推荐）
    # 从后往前的双指针法，时间复杂度为O(m+n)，空间复杂度为O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        index = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        if p2 >= 0:
            nums1[:index+1] = nums2[:p2+1]

    # 方法二：直接进行排序（推荐）
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1 
        if n > 0:
            nums1[:n] = nums2[:n]
            

    # 方法三：双指针法
    # 从后往前的双指针法，时间复杂度为O(m+n)，空间复杂度为O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1和p2分别指向nums1和nums2的最右边的有效元素
        p1, p2 = m-1, n-1
        # tail指向两数组合并后的最后一个元素
        tail = m+n-1
        # 循环合并
        while p1 >= 0 or p2 >= 0:
            # 判断nums1的有效元素是否已经全部处理完
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            # 判断nums2的有效元素是否已经全部处理完
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            # 如果nums1和nums2都未处理完，则对两个指针指向的元素进行比较
            # 如果nums1[p1] > nums2[p2]，那就把nums1[p1]放到tail的位置
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            # 如果nums1[p1] <= nums2[p2]，那就把nums2[p2]放到tail的位置
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            # 每次循环结束都把tail往前移动一位
            tail -= 1
# @lc code=end

