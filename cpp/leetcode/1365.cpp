#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    /**
     * Solution with the assumptions that 0<=nums[i]<=100
     * */
    vector<int> smallerNumbersThanCurrent(vector<int> &nums)
    {
        int cnt[101] = {0}, f[101] = {0};

        for (int e : nums)
        {
            cnt[e]++;
        }

        for (int i = 1; i <= 100; i++)
        {
            f[i] = f[i - 1] + cnt[i - 1];
        }

        vector<int> res;

        for (int e : nums)
        {
            res.push_back(f[e]);
        }

        return res;
    }

    vector<int> smallerNumbersThanCurrent_hashmap_over_vect(vector<int> &nums)
    {
        unordered_map<int, int> h, f;
        set<int> s;
        for (int e : nums)
        {
            h[e]++;
            s.insert(e);
        }

        vector<int> nums_dist(s.begin(), s.end());

        for (int i = 1; i < nums_dist.size(); i++)
        {
            int prev = nums_dist[i - 1];
            f[nums_dist[i]] = f[prev] + h[prev];
        }

        vector<int> res;

        for (int e : nums)
        {
            res.push_back(f[e]);
        }

        return res;
    }

    vector<int> smallerNumbersThanCurrent_hashmap_over_set(vector<int> &nums)
    {
        unordered_map<int, int> h, f;
        set<int> s;
        for (int e : nums)
        {
            h[e]++;
            s.insert(e);
        }

        set<int>::iterator it = s.begin();
        int prev = *it;
        it++;
        for (; it != s.end(); it++)
        {
            f[*it] = f[prev] + h[prev];
            prev = *it;
        }

        vector<int> res;

        for (int e : nums)
        {
            res.push_back(f[e]);
        }

        return res;
    }
};

int main()
{
    Solution solution;

    vector<int> v({8, 1, 2, 2, 3});
    for (int e : solution.smallerNumbersThanCurrent_hashmap_over_set(v))
    {
        cout << e << " ";
    }
}