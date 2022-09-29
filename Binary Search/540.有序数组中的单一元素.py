#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    # 本题与「136.只出现一次的数字」相似，区别在于本题的数组是有序的，而第136题是无序的
    # 方法一：异或运算
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     return functools.reduce(lambda x,y: x ^ y, nums)
    
    # 方法二：二分查找
    # 如果排序后的数组中的每个元素都恰好出现两次，它们将以下标为i和i+1的方式成对出现，其中i为偶数。
    # 也就是说，nums[i] = nums[i+1]且nums[i+1] != nums[i+2]。
    # 当我们将唯一元素插入这个列表时，它后面所有对的下标将移位1，使上面的关系反转。因此，对于任何偶数索引i，我们可以比较nums[i]和nums[i+1]。
    # （1）如果它们相等，则唯一元素必须出现在索引i+1之后的某个位置
    # （2）如果它们不相等，则唯一元素必须出现在索引i+1之前的某个位置
    # 利用这些知识，我们可以使用二分查找来找到唯一元素。
    # 我们只需要确保主索引总是偶数，所以我们可以使用mid = 2 * ((l + r) // 4)而不是通常的mid = (l + r) // 2。
    # Time: O(logn) Space: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = 2 * ((l + r) // 4)
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]
# @lc code=end

