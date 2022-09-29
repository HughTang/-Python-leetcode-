#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    # 方法一：快慢指针，本题与环形链表II的思路相同
    # 参考题解：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
    
    # 方法二：sum求和相减（不符合O(1)空间复杂度的要求）
    def findDuplicate(self, nums: List[int]) -> int:
        num = sum(nums) - sum(set(nums))
        ret = len(nums) - len(set(nums))
        return num // ret

        
    # 方法三：二分查找，即根据鸽巢原理并利用二分查找的思路，
    # 与第378题类似，但两题中二分查找的判断条件有区别，注意区分。
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            cnt = 0
            mid = left + (right - left) // 2
            for v in nums:
                if v <= mid:
                    cnt += 1
            # 此处为>的判断，而378题为>=的判断
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

