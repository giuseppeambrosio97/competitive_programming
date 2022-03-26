#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int r = nums.size() - 1, l = 0;

        while (l <= r)
        {
            int m = l + (r - l) / 2;
            if (nums[m] == target)
            {
                return m;
            }

            if (nums[l] <= target && target <= nums[m])
            {
                r = m - 1;
            }
            else if (nums[m] <= target && target <= nums[r])
            {
                l = m + 1;
            }
            /*****
             * Because one of the two segments of the array is sorted. We know for sure
             * that the segment in which could be target is the one not sorted.
             * examples:
             *      [4 5 6 0 1 2 3], target = 5
             * So find the ordered segment and find that target doesnt fit in it, tell us that the segment to look for
             * is the one not sorted.
             * What we do is check if target fit in one of the two segments. If it's not then find in the segment not sorted.
             * */
            else if (nums[l] > nums[m])
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
        }

        return -1;
    }
};

int main()
{
    Solution s;
    vector<int> v({4, 5, 6, 7, 0, 1, 2});
    cout << s.search(v, 5) << endl;
}