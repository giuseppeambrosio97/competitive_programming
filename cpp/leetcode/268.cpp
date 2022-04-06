#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        int sum = 0;
        for (int e : nums)
        {
            sum += e;
        }
        int n = nums.size();
        return n * (n + 1) / 2 - sum;
    }

    int missingNumberXOR(vector<int> &nums)
    {
        int ans = 0, n = nums.size();

        for (int i = 0; i < n; i++)
        {
            ans = ans ^ i ^ nums[i];
        }
        return ans ^ n;
    }
};