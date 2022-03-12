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
//     ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
//     {
//         if (list1 == nullptr)
//         {
//             return list2;
//         }
//         if (list2 == nullptr)
//         {
//             return list1;
//         }

//         ListNode *mergedList = nullptr;

//         if (list1->val <= list2->val)
//         {
//             mergedList = list1;
//             list1 = list1->next;
//         }
//         else
//         {
//             mergedList = list2;
//             list2 = list2->next;
//         }

//         ListNode *head = mergedList;
//         while (list1 != nullptr && list2 != nullptr)
//         {
//             if (list1->val <= list2->val)
//             {
//                 mergedList->next = list1;
//                 list1 = list1->next;
//             }
//             else
//             {
//                 mergedList->next = list2;
//                 list2 = list2->next;
//             }
//             mergedList = mergedList->next;
//         }

//         if (list1 == nullptr)
//         {
//             mergedList->next = list2;
//         }
//         else
//         {
//             mergedList->next = list1;
//         }

//         return head;
//     }
// };

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode fake(-1);

        ListNode *last = &fake;
        while (list1 != nullptr && list2 != nullptr)
        {
            if (list1->val <= list2->val)
            {
                last->next = list1;
                list1 = list1->next;
            }
            else
            {
                last->next = list2;
                list2 = list2->next;
            }
            last = last->next;
        }

        if (list1 == nullptr)
        {
            last->next = list2;
        }
        else
        {
            last->next = list1;
        }

        return fake.next;
    }
};

int main()
{

    ListNode *head2 = new ListNode(4);
    ListNode *head1 = new ListNode(2, head2);
    ListNode *head = new ListNode(1, head1);

    ListNode *iter = head;

    while (iter != nullptr)
    {
        cout << iter->val << endl;
        iter = iter->next;
    }
}