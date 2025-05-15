/**
 * Floyd's Cycle Detection Algorithm
 * - use two pointers moving at different speeds
 * - if the list has a cycle, the fast pointer will eventually catch the slow one.
 * - if the list ends (fast reaches null), there is no cycle.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 
 */

// Floyd's Cycle Detection Algorithm

class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val: number) {
        this.val = val;
        this.next = null;
    }
}

function hasCycle(head: ListNode | null): boolean {
    // initialize two pointers at the head of the list
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    // Traverse the list with two pointers
    while (fast !== null && fast.next !== null) {
        slow = slow!.next; // move slow pointer by 1 step
        fast = fast.next.next; // move fast pointer by 2 steps

        // If the two pointers meet, there is a cycle
        if (slow === fast) {
            return true;
        
    }
}
return false; 
}
