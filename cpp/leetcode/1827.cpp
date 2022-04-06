#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int minOperations(vector<int> &nums)
    {
        int count = 0, cur = nums[0];

        for (int i = 1; i < nums.size(); i++)
        {
            
            int delta = max(0, cur - nums[i] + 1);
            count += delta;
            cur = nums[i] + delta;
        }

        return count;
    }
};