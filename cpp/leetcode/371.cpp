#include <bits/stdc++.h>

using namespace std;

/**
 * Time complexity O(32) = O(1)
 * */
// class Solution
// {
// public:
//     int getSum(int a, int b)
//     {
//         int res = 0, carry = 0;
//         for (int i = 0; i < 32; i++)
//         {
//             int bit_i_a = (a >> i) & 1;
//             int bit_i_b = (b >> i) & 1;
//             int bit_i_res = bit_i_a ^ bit_i_b ^ carry;
//             carry = carry ? bit_i_a | bit_i_b : bit_i_a & bit_i_b;
//             res |= bit_i_res << i;
//         }
//         return res;
//     }
// };

// class Solution
// {
// public:
//     int recSolve(int a, unsigned int b)
//     {
//         if (a == 0 || b == 0)
//         {
//             return a | b;
//         }
//         return recSolve(a ^ b, (a & b) << 1);
//     }
//     int getSum(int a, int b)
//     {
//         unsigned int b_ = (a & b);
//         return recSolve(a ^ b, b_ << 1);
//     }
// };

class Solution
{
public:
    int getSum(int a, int b)
    {
        while (b != 0)
        {
            unsigned int c = (a & b);
            a = a ^ b;
            b = c << 1;
        }

        return a;
    }
};

int main()
{
    Solution s;
    cout << s.getSum(-1, 1) << endl;
}