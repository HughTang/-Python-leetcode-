#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    # 本题的解题方法有很多，而且性能差别不大，此处选取了经典的双指针解法，思路如下：
    #
    # 考虑使用指针p0来交换0，p2来交换2。此时，p0的初始值仍然为0，而p2的初始值为n-1。在遍历的过程中，我们需要找出所有的0交换至数组的头部，
    # 并且找出所有的2交换至数组的尾部。由于此时其中一个指针p2是从右向左移动的，因此当我们在从左向右遍历整个数组时，如果遍历到的位置超过了p2，
    # 那么就可以直接停止遍历了。具体地，我们从左向右遍历整个数组，设当前遍历到的位置为i，对应的元素为nums[i]；
    # 
    #     （1）如果找到了0，那么与前面两种方法类似，将其与nums[p0]进行交换，并将p0向后移动一个位置；
    #     （2）如果找到了2，那么将其与nums[p2]进行交换，并将p2向前移动一个位置。
    # 
    # 可以发现，对于第二种情况，当我们将nums[i]与nums[p2]进行交换之后，新的nums[i]可能仍然是2，也可能是0。然而此时我们已经结束了交换，开始
    # 遍历下一个元素nums[i+1]，不会再考虑nums[i] 了，这样我们就会得到错误的答案。因此，当我们找到2时，我们需要不断地将其与nums[p2]进行交换，
    # 直到新的nums[i]不为2。此时，如果nums[i]为0，那么对应着第一种情况；如果nums[i]为1，那么就不需要进行任何后续的操作。

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # p0指针初始化为下标0，p0指针初始化为下标len(nums) - 1
        p0, p2 = 0, len(nums) - 1
        # i初始化为0，用于遍历数组
        i = 0
        # 当i > p2时跳出循环
        while i <= p2:
            # nums[i]与nums[p2]的循环交换
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            # nums[i]与nums[p0]的循环交换
            while p0 <= i and nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            # i自增继续向后遍历
            i += 1
# @lc code=end

