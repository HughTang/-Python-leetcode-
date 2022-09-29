#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    分类奇偶节点后合并，即在链表不为空的情况下，将存放奇数的表头
    oddHead指向head，存放偶数的表头evenHead指向head.next，然后
    使用odd和even两个指针遍历原链表，最后将odd.next指向evenHead，
    最后返回oddHead即可。时间复杂度为O(N)，空间复杂度为O(1)。
    注意：该题中最重要的部分是while循环遍历原链表时的循环条件，
    由于本题每次循环结束后even指针（包括链表长度为奇数时最后的
    None）总在odd指针的后面，因此可以将even and even.next作为
    while的循环条件。
    
    '''
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 由于后面用到了head.next的赋值操作，因此需要对head判空
        if not head:
            return head
        
        # oddHead和evenHead为表头指针，odd和even分别为遍历指针
        oddHead = odd = head
        evenHead = even = head.next

        # while循环体，注意循环条件
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        # 由于even在循环结束时一定会指向None，所以只需要将
        # odd.next指向偶链表的表头evenHead即可。
        odd.next = evenHead
        # 返回奇链表头结点
        return oddHead
# @lc code=end

