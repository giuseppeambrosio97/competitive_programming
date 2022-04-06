#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        int ans = 0;
        for (int i = 0; i < 32; i++)
        {
            if (n & (1 << i))
            {
                ans++;
            }
        }
        return ans;
    }
    int hammingWeightv2(uint32_t n)
    {
        int ans = 0;
        for (int i = 0; i < 32; i++)
        {
            ans += n & 1;
            n >>= 1;
        }
        return ans;
    }
    int hammingWeightv3(uint32_t n)
    {
        int ans = 0;
        for (int i = 0; i < 32; i++)
        {
            ans += n % 2;
            n >>= 1;
        }

        return ans;
    }

    int hammingWeightv4(uint32_t n)
    {
        int ans = 0;
        while (n > 0)
        {
            ans += n % 2;
            n >>= 1;
        }

        return ans;
    }

    /************
     * This solution makes ans iteration instead of 32 like the previous one.
     * 
     * Why does it work?
     *      Given a number (in binary) 1101000 and compute the number minus 1 in binary
     *      1101000
     *      0000001
     *      -------
     *      1101111
     *      In generally the result of this operation will have:
     *          - in corrispondence of all the 0 before the first 1 has 1 -> this because 0 - 1 in binary is 1 with 1 carry over
     *                                                                    this carry over will be brought forward until we meet a 1
     *                                                                    When we meet a 1, we have 1 - 1 in binary which is 0
     *          - in corrispondence of the first bit equal to 1 
     *          - in corrispondence of all the bits after the first 1 has the same bit of the input number
     *      So if we have a number n and compute the number n-1 and compute the and bit by bit of these two numbers we will have a number that:
     *          - in corrispondence of all the 0 before the first 1 in n has 0 because n-1 has 1 in these positions
     *          - in corrispondence of the first bit equal to 1 in n has 0 because n-1 has 0 in this positions
     *          - in corrispondence of all the remaining bits has the same bits of n because also n-1 has these bit
     * So at each iteration we will erase the leftmost bit, when we erase all the 1 we will have 0 and finished
     * */
    int hammingWeightTricky(uint32_t n)
    {
        int ans = 0;
        while (n > 0)
        {
            n = n & (n - 1);
            ans++;
        }

        return ans;
    }
};