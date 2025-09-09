struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {  // NOLINT
        ListNode* before_first = new ListNode;
        int to_add = 0;
        const int kBase = 10;
        ListNode* curr = before_first;

        while (l1 != nullptr || l2 != nullptr || to_add != 0) {
            int l1_digit = l1 != nullptr ? l1->val : 0;
            int l2_digit = l2 != nullptr ? l2->val : 0;

            int result = l1_digit + l2_digit + to_add;
            ListNode* new_node = new ListNode();
            new_node->val = result % kBase;

            to_add = result / kBase;

            curr->next = new_node;
            curr = curr->next;

            l1 = l1 != nullptr ? l1->next : l1;
            l2 = l2 != nullptr ? l2->next : l2;
        }

        return before_first->next;
    }
};