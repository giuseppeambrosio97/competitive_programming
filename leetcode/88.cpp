#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

// class Solution
// {
// public:
//     void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
//     {
//         ll k = m + n - 1;
//         int j = n - 1, i = m - 1;
//         while (k >= 0)
//         {
//             while (j >= 0 && (i < 0 || nums1[i] <= nums2[j]))
//             {
//                 nums1[k--] = nums2[j--];
//             }
//             if (i >= 0)
//             {
//                 nums1[k--] = nums1[i--];
//             }
//         }
//     }
// };

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        ll k = m + n - 1;
        int j = n - 1, i = m - 1;
        while (i >= 0 && j >= 0)
        {
            if (nums1[i] <= nums2[j])
            {
                nums1[k--] = nums2[j--];
            }
            else
            {
                nums1[k--] = nums1[i--];
            }
        }

        if (j < 0)
        {
            //in this case there are still i elements to place. But this elements are already
            //correctly placed
            return;
        }

        while (j >= 0)
        {
            nums1[k--] = nums2[j--];
        }
    }
};