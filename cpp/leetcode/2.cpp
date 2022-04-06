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

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode fake = ListNode(-1);
        ListNode *cur = &fake;
        int carry = 0;

        while (l1 != nullptr && l2 != nullptr)
        {
            int val = l1->val + l2->val + carry;
            cur->next = new ListNode(val % 10);
            carry = val / 10;
            cur = cur->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != nullptr)
        {
            int val = l1->val + carry;
            cur->next = new ListNode(val % 10);
            carry = val / 10;
            cur = cur->next;
            l1 = l1->next;
        }

        while (l2 != nullptr)
        {
            int val = l2->val + carry;
            cur->next = new ListNode(val % 10);
            carry = val / 10;
            cur = cur->next;
            l2 = l2->next;
        }

        if (carry > 0)
        {
            cur->next = new ListNode(carry);
        }

        return fake.next;
    }
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode fake = ListNode(-1);
        ListNode *cur = &fake;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry)
        {
            int val = l1 != nullptr ? l1->val : 0;
            val += l2 != nullptr ? l2->val : 0;
            val += carry;
            cur->next = new ListNode(val % 10);
            carry = val / 10;
            cur = cur->next;
            l1 = l1 != nullptr ? l1->next : nullptr;
            l2 = l2 != nullptr ? l2->next : nullptr;
        }
        return fake.next;
    }
};