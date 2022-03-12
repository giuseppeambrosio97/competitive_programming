#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * Space complexity O(n)
 * */
// class Solution
// {
// public:
//     bool hasCycle(ListNode *head)
//     {
//         unordered_map<ListNode *, int> h;
//         ListNode *last = head;
//         while (last != nullptr)
//         {
//             auto it = h.find(last);
//             if (it != h.end())
//             {
//                 return true;
//             }

//             h.insert(make_pair(last, 1));
//             last = last->next;
//         }
//         return false;
//     }
// };

/**
 * Space complexity O(1)
 * */
// class Solution
// {
// public:
//     bool hasCycle(ListNode *head)
//     {
//         ListNode fake(-1);
//         ListNode *last = head;
//         while (last != nullptr)
//         {
//             if (last == &fake)
//             {
//                 return true;
//             }
//             ListNode *tmp = last;
//             last = last->next;
//             tmp->next = &fake;
//         }
//         return false;
//     }
// };

/**
 * Space complexity O(1)
 * */
class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        ListNode *last = head;
        while (last != nullptr)
        {
            if (last->val == 10001)
            {
                return true;
            }
            last->val = 10001;
            last = last->next;
        }
        return false;
    }
};

/**
 * Space complexity O(1)
 * Floyd's Tortoise & Hare
 * */
class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        ListNode *slow = head, *fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{

    ListNode *node4 = new ListNode(-4);
    ListNode *node3 = new ListNode(0, node4);
    ListNode *node2 = new ListNode(2, node3);
    ListNode *node1 = new ListNode(3, node2);
    node4->next = node2;

    Solution solution;

    cout << solution.hasCycle(node1) << "\n";
}