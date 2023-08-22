/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> q = new PriorityQueue<>((o1,o2)->{
            return o1.val-o2.val;
        });
        for(int i=0;i<lists.length;i++){
            if(lists[i]!=null)
            q.add(lists[i]);
        }
        ListNode ans = new ListNode(-1);
        ListNode curr = ans;
        while(!q.isEmpty()){
            ListNode head = q.poll();
            ans.next = head;
            ans = ans.next;
            if(head.next!=null)
            q.add(head.next);
        }
        return curr.next;
    }
    
}