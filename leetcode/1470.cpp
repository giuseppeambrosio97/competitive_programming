#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * Space complexity O(1)
 * */
// class Solution
// {
// public:
//     vector<int> shuffle(vector<int> &nums, int n)
//     {
//         for (int j = 0; j < n - 1; j++)
//         {
//             int el = nums[n + j];
//             nums.erase(nums.begin() + n + j);
//             nums.insert(nums.begin() + j * 2 + 1, el);
//         }

//         return nums;
//     }
// };

class Solution
{
public:
    vector<int> shuffle(vector<int> &nums, int n)
    {
        vector<int> res(2 * n);
        for (int j = 0; j < n; j++)
        {
            res[j * 2] = nums[j];
            res[j * 2 + 1] = nums[n + j];
        }

        return res;
    }
};

int main()
{
    vector<int> a({2, 5, 1, 4, 3, 4, 7, 8});

    Solution solution;
    a = solution.shuffle(a, 4);

    for (int e : a)
    {
        cout << e << " ";
    }
    cout << "\n";
}