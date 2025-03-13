class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = ListNode(-1)
        ret = first
        l1_node = l1
        l2_node = l2

        while l1_node or l2_node:
            if not l1_node:
                ret.next = l2_node
                break
            elif not l2_node:
                ret.next = l1_node
                break

            if l1_node.val <= l2_node.val:
                tmp = l1_node.next
                ret.next = l1_node
                l1_node = tmp                
            else:
                tmp = l2_node.next
                ret.next = l2_node
                l2_node = tmp
            ret = ret.next
            ret.next = None

        return first.next