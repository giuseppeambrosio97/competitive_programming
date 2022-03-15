struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * Iterative version 
 * Time complexity O(n)
 * Space complexity O(1)
 * */
// class Solution
// {
// public:
//     ListNode *reverseList(ListNode *head)
//     {

//         ListNode *prev = nullptr, *cur = head;

//         while (cur != nullptr)
//         {
//             ListNode *succ = cur->next;
//             cur->next = prev;
//             prev = cur;
//             cur = succ;
//         }
//         return prev;
//     }
// };

/**
 * Recursive version
 * Time complexity O(n)
 * Space complexity O(n)
 * */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }

        ListNode *new_head = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }
};
