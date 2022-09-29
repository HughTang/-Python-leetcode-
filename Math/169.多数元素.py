#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    # 方法一：直接排序，然后返回数组中下标为n//2的元素，因为最中间那个数出现次数一定多于 n / 2
    # 时间复杂度为O(NlogN)，空间复杂度为O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    
    # 方法二：使用 cnt 来统计一个元素出现的次数，当遍历到的元素和统计元素不相等时，令 cnt--。如果前面查找了 i 个元素，且 cnt == 0，
    # 说明前 i 个元素没有 majority，或者有 majority，但是出现的次数少于 i / 2，因为如果多于 i / 2 的话 cnt 就一定不会为 0。此时剩下
    # 的 n - i 个元素中，majority 的数目依然多于 (n - i) / 2，因此继续查找就能找出 majority。
    # 时间复杂度为O(N)，空间复杂度为O(1)
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majority = nums[0]
        for v in nums:
            majority = v if cnt == 0 else majority
            cnt = cnt + 1 if majority == v else cnt - 1
        return majority
# @lc code=end

