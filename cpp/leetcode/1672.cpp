#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int maximumWealth(vector<vector<int>> &accounts)
    {
        int mx = 0;
        for (vector<int> customer_banks : accounts)
        {
            int sum = 0;
            for (int money_customer_bank : customer_banks)
            {
                sum += money_customer_bank;
            }
            mx = max(sum, mx);
        }
        return mx;
    }
};