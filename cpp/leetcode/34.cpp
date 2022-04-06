#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        vector<int>::iterator it = lower_bound(nums.begin(), nums.end(), target);
        if (it == nums.end())
            return vector<int>({-1, -1});
        int i = it - nums.begin();
        if (nums[i] != target)
            return vector<int>({-1, -1});

        int j = lower_bound(nums.begin() + i, nums.end(), target+1) - nums.begin();

        return vector<int>({i, j-1});
    }
};

int main()
{

    Solution sol;
    vector<int> nums({1, 2});
    vector<int> v = sol.searchRange(nums, 3);

    cout << v[0] << " " << v[1] << " " << endl;

    return 0;
}