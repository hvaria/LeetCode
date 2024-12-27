// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>, 
        list2: Option<Box<ListNode>>
    ) -> Option<Box<ListNode>> {
        // Create a dummy node to simplify merging
        let mut dummy = ListNode::new(0);
        let mut tail = &mut dummy; // Pointer to build the new list

        let mut l1 = list1;
        let mut l2 = list2;

        while l1.is_some() && l2.is_some() {
            if l1.as_ref().unwrap().val <= l2.as_ref().unwrap().val {
                tail.next = l1; // Link the smaller node
                tail = tail.next.as_mut().unwrap(); // Move the tail pointer
                l1 = tail.next.take(); // Advance in list1
            } else {
                tail.next = l2; // Link the smaller node
                tail = tail.next.as_mut().unwrap(); // Move the tail pointer
                l2 = tail.next.take(); // Advance in list2
            }
        }

        // Append any remaining nodes
        if l1.is_some() {
            tail.next = l1;
        } else if l2.is_some() {
            tail.next = l2;
        }

        // Return the merged list starting after the dummy node
        dummy.next
    }
}