#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_map<int, int> h;

        for (int e : nums)
        {
            if (h[e])
            {
                return true;
            }
            else
            {
                h[e] = 1;
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<int> v({1, 2, 4, 53, 22});
    cout << s.containsDuplicate(v) << "\n";

    return 0;
}