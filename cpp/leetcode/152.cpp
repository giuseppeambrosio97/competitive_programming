#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(n^2)
 * TLE
 * */
// class Solution
// {
// public:
//     int maxProduct(vector<int> &nums)
//     {
//         int n = nums.size(), mx = INT_MIN;
//         for (int i = 0; i < n; i++)
//         {
//             int prod = 1;
//             for (int j = i; j < n; j++)
//             {
//                 prod *= nums[j];
//                 mx = max(mx, prod);
//             }
//         }
//         return mx;
//     }
// };

/**
 * Time complexity O(n)
 * Space complexity O(n)
 * 
 * d[i] = max product subarray ending in a[i]
 * 
 * To solve the problem we can't do just d[i]=max(d[i-1],a[i],d[i-1]*a[i])
 * a = [-1,-2,-3], d[1] = 2, d[2] = max(2,-3,2*-3)=2 but it's clearly doens't work Because
 * the optima solution in this case is 6.
 * 
 * First of all we can notice that any array containing zero can be be splitted in correspondence of the zeros.
 * Doing this we end up with having more array and the solution of the initial array will be the max of solutions among
 * this subarray. 
 * That said we can assume we don't have zero
 * 
 * So how we can compute that?
 * Looking at the example we can see that to find 6 we should have keep track -2 because 6=-3*-2.
 * Notice that -2 is the minimum product subarray ending in a[i].
 * But what happen if instead of -3 we would have 3? The optimal solution would be again 6 but 
 * for the multiplication of different elements -1*-2*-6. Notice that -1*-2 is the optimal
 * solution of the subproblem [-1,-2].
 * 
 * So to solve the problem we need to keep track of two values:
 *      - the maximum product subarray ending in a[i] -> dmx[i]
 *      - the minimum product subarray ending in a[i] -> dmn[i]
 * 
 * In this way we can solve the problem in this way:
 * 
 * 
 * dmx[i] = max(
 *      dmx[i-1]*a[i],  [2,6] -> dmx[1] = 12
 *      dmn[i-1]*a[i],  [-1,-2,6] -> dmx[2] = 12
 *      a[i])           [-1,2] -> dmx[1] = 2  
 * dmn[i] = max(
 *      dmx[i-1]*a[i],  [-1,3,-2] -> dmn[1] = -6 
 *      dmn[i-1]*a[i],  [-1,2] -> dmn[1] = -2 
 *      a[i])           [3,-2] -> dmn[1] = -2 
 * d[i] = max(d[i-1],dmx[i])
 * */
class Solution
{
public:
    int max3(int a, int b, int c)
    {
        return max(max(a, b), c);
    }
    int min3(int a, int b, int c)
    {
        return min(min(a, b), c);
    }
    int maxProduct(vector<int> &nums)
    {
        int res, n = nums.size();
        vector<int> d(n), dmx(n, 1), dmn(n, 1);

        dmx[0] = nums[0];
        dmn[0] = nums[0];
        res = nums[0];

        for (int i = 1; i < n; i++)
        {
            if (nums[i] != 0)
            {
                dmx[i] = max3(nums[i] * dmx[i - 1], nums[i] * dmn[i - 1], nums[i]);
                dmn[i] = min3(nums[i] * dmx[i - 1], nums[i] * dmn[i - 1], nums[i]);

                res = max(dmx[i], res);
            }
            else
            {
                res = max(res, 0);
            }
        }

        return res;
    }
};

/**
 * This solution follow the same reasoning as the previous one.
 * But has Space complexity O(1)
 * 
 * Further reasoning:
 * 
 * [-1,-2]
 *     mx = 2
 *     mn =-2
 * [-1,-2, 3]
 *     mx = 6
 *     mn =-6
 * [-1,-2, -3]
 *     mx = 6, mn of the previous iteration times -3 -> -2*-3
 *     mn =-6, mx of the previous iteration times -3 ->  2*-3
 * */
class Solution
{
public:
    int max3(int a, int b, int c)
    {
        return max(max(a, b), c);
    }
    int min3(int a, int b, int c)
    {
        return min(min(a, b), c);
    }
    int maxProduct(vector<int> &nums)
    {
        int res, n = nums.size(), mx = 1, mn = 1;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] != 0)
            {
                int tmp_mx = mx;
                mx = max3(nums[i] * mx, nums[i] * mn, nums[i]);
                mn = min3(nums[i] * tmp_mx, nums[i] * mn, nums[i]);
                res = max(mx, res);
            }
            else
            {
                mx = 1;
                mn = 1;
                res = max(res, 0);
            }
        }

        return res;
    }
};

int main()
{
    Solution solution;
    vector<int> v({3, -1, 4});
    cout << solution.maxProduct(v) << endl;
}