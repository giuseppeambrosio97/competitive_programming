#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    /**
     * Time complexity O(n^2)
     * */
    int numIdenticalPairs_NN(vector<int> &nums)
    {
        int cnt = 0, n = nums.size();
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i] == nums[j])
                {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    /*****
     * Time complexity O(n)
     * */
    int numIdenticalPairs(vector<int> &nums)
    {
        int cnt = 0, n = nums.size();
        unordered_map<int, int> h;
        for (int i = 0; i < n; i++)
        {
            cnt += h[nums[i]];
            h[nums[i]]++;
        }
        return cnt;
    }

    int numIdenticalPairs_array(vector<int> &nums)
    {
        int cnt = 0, n = nums.size();
        int h[101] = {0};
        for (int i = 0; i < n; i++)
        {
            cnt += h[nums[i]];
            h[nums[i]]++;
        }
        return cnt;
    }
};