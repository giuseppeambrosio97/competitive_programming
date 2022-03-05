#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * 
 * This solution has:
 *  - time complexity O(log_10 x)
 *  - space complexity O(log_10 x)
 * 
 * */
// class Solution
// {
// public:
//     vector<int> digits(int x)
//     {
//         vector<int> digits;
//         ll m = 10, q = 1;
//         while (x % m != x)
//         {
//             digits.push_back((x % m) / q);
//             m *= 10;
//             q *= 10;
//         }
//         digits.push_back((x % m) / q);
//         return digits;
//     }
//     bool isPalindrome(int x)
//     {
//         if (x >= 0)
//         {
//             vector<int> ds = digits(x);
//             int n = ds.size();
//             for (int i = 0; i < n / 2; i++)
//             {
//                 if (ds[i] != ds[n - i - 1])
//                 {
//                     return false;
//                 }
//             }
//             return true;
//         }

//         return false;
//     }
// };

/**
 * 
 * This solution has:
 *  - time complexity O(log_10 x)
 *  - space complexity O(1)
 * 
 * */
// class Solution
// {
// public:
//     bool isPalindrome(int x)
//     {
//         if (x < 0 || (x % 10 == 0 && x != 0))
//         {
//             return false;
//         }

//         int l = x, r = 0;

//         while (r < l)
//         {
//             r = r * 10 + (l % 10);
//             l /= 10;
//         }

//         return r == l || r / 10 == l;
//     }
// };

/**
 * Same time and space complexity of the above solution, but with a different logic to test 
 * if we have reached the half of the number x
 * */
class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0 || (x % 10 == 0 && x != 0))
        {
            return false;
        }

        int l = x, r = 0;
        int m = 10;

        while (r % m != r || l % m != l)
        {
            r = r * 10 + (l % 10);
            l /= 10;
            m *= 10;
        }
        cout << l  << " " << r << endl;

        return r == l || r == l / 10;
    }
};