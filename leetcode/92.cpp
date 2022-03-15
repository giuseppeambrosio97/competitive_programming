#include <bits/stdc++.h>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// class Solution
// {
// public:
//     ListNode *reverseBetween(ListNode *head, int left, int right)
//     {
//         ListNode *node_i_prev = nullptr, *node_i = head;
//         for (int i = 1; i < left; i++)
//         {
//             node_i_prev = node_i;
//             node_i = node_i->next;
//         }

//         ListNode *prev = nullptr, *cur = node_i;

//         int i = left;
//         while (i <= right && cur != nullptr)
//         {
//             ListNode *tmp = cur->next;
//             cur->next = prev;
//             prev = cur;
//             cur = tmp;
//             i++;
//         }

//         node_i->next = cur;

//         if (left > 1)
//         {
//             node_i_prev->next = prev;
//             return head;
//         }
//         else
//         {
//             return prev;
//         }
//     }
// };

/**
 * Solution with fake node
 * */
// class Solution
// {
// public:
//     ListNode *reverseBetween(ListNode *head, int left, int right)
//     {
//         ListNode fake(-1, head);
//         ListNode *node_i_prev = &fake, *node_i = head;
//         for (int i = 1; i < left; i++)
//         {
//             node_i_prev = node_i;
//             node_i = node_i->next;
//         }

//         ListNode *prev = node_i_prev, *cur = node_i;

//         int i = left;
//         while (i <= right && cur != nullptr)
//         {
//             ListNode *tmp = cur->next;
//             cur->next = prev;
//             prev = cur;
//             cur = tmp;
//             i++;
//         }

//         node_i->next = cur;
//         node_i_prev->next = prev;
//         return fake.next;
//     }
// };

/**
 * Solution with fake node and uses less variables than the previous solution.
 * */
class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        ListNode fake(-1, head);
        ListNode *left_prev = &fake, *cur = head;
        for (int i = 1; i < left; i++)
        {
            left_prev = cur;
            cur = cur->next;
        }

        ListNode *prev = nullptr;

        int i = left;
        while (i <= right && cur != nullptr)
        {
            ListNode *tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
            i++;
        }

        left_prev->next->next = cur;
        left_prev->next = prev;
        return fake.next;
    }
};

int main()
{
    ListNode *head5 = new ListNode(5);
    ListNode *head4 = new ListNode(4, head5);
    ListNode *head3 = new ListNode(3, head4);
    ListNode *head2 = new ListNode(2, head3);
    ListNode *head1 = new ListNode(1, head2);

    Solution s;
    ListNode *new_head = s.reverseBetween(head1, 2, 4);

    while (new_head != nullptr)
    {
        cout << new_head->val << " ";
        new_head = new_head->next;
    }
}
