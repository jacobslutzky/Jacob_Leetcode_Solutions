/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ArrayList<ListNode> split(ListNode src) {
        ListNode d1 = new ListNode(0);
        ListNode t1 = d1;
        ListNode d2 = new ListNode(0);
        ListNode t2 = d2;
        
        while (src != null) {
            t1.next = src;
            t1 = t1.next;
            src = src.next;
            if (src != null) {
                t2.next = src;
                t2 = t2.next;
                src = src.next;
            }
        }
        t1.next = null;t2.next=null;
        ArrayList<ListNode> r = new ArrayList<ListNode>();
        r.add(d1.next);
        r.add(d2.next);
        return r;
    }
    public ListNode swapPairs(ListNode head) {
        ArrayList<ListNode> a_b = split(head);        
        ListNode a = a_b.get(0);
        ListNode b = a_b.get(1);       
        if (b==null) return head;
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (b!=null) {
            tail.next = b;
            tail = tail.next;
            b = b.next;
            
            tail.next = a;
            tail = tail.next;
            a = a.next;
        }
        if (a!=null) tail.next = a;
        return dummy.next;
    }
}