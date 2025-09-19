class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize pointers
        prev = None  # Previous node starts as None
        curr = head  # Current node starts at the head

        # Traverse the list
        while curr is not None:
            next_node = curr.next  # Save the next node
            
            curr.next = prev  # Reverse the link
            
            # Move pointers forward
            prev = curr  # Move prev to the current node
            curr = next_node  # Move curr to the next node

        # prev is now the new head of the reversed list
        return prev
