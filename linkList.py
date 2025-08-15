from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        # while curr:
        #     temp = curr.next      # Store next node
        #     curr.next = prev      # Reverse pointer
        #     prev = curr           # Move prev forward
        #     curr = temp           # Move curr forward
        # return prev               # New head of reversed list
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # tail = dummy

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next

        # # Attach the remaining part
        # tail.next = list1 or list2

        # return dummy.next
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Floyd's Tortoise and Hare
        slow, fast = head, head
        
        while fast and fast.next:
            print('sdsadad')
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def build_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Example usage:
head = build_linked_list([1, 2, 3, 4])
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 5])
cycle_linked_list = build_linked_list([1, 2, 3, 4])

sol = Solution()
# Call the reverse function
reversed_head = sol.reverseList(head)

#Merge Link list
mergeLinkList = sol.mergeTwoLists(list1, list2)

# Call the hasCycle function
# Find the last node
last = cycle_linked_list
while last.next:
    last = last.next

# Create a cycle: point last node (4) back to node 2
print(last.val)
last.next = cycle_linked_list.next  # head.next is node 2
has_cycle = sol.hasCycle(cycle_linked_list)
print(has_cycle)

# Print the reversed list
while reversed_head:
    print(reversed_head.val, end=" -> " if reversed_head.next else "\n")
    reversed_head = reversed_head.next

# Print the merged list
# while mergeLinkList:
#     print(mergeLinkList.val, end=" -> " if mergeLinkList.next else "\n")
#     mergeLinkList = mergeLinkList.next

        