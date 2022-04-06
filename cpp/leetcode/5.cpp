#include <bits/stdc++.h>

using namespace std;

/******
 * Time complexity O(n^2)
 * Space complexity O(1) 
 * */
class Solution
{
public:
    int expand(string s, int l, int r)
    {
        while (l >= 0 && r < s.length() && s[l] == s[r])
        {
            r++;
            l--;
        }
        return r - l - 1;
    }
    string longestPalindrome(string s)
    {
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++)
        {
            int l_odd = expand(s, i, i);
            int l_even = expand(s, i, i + 1);
            int len = max(l_odd, l_even);
            if (len > end - start + 1)
            {
                /******
                 * ababa
                 * with i = 3
                 * there are:
                 *      - 2 characters before i len/2
                 *      - 2 characters after i len/2
                 *
                 * ecddce
                 * with i = 2, len = 6
                 * there are:
                 *      - 2 characters before i (len-1)/2 -> you can imagine that by chopping the last character, the last e in this case, in this way
                 *                                           you have a string with odd length and now to find the first character of this string we can use
                 *                                           the same argument used before, but now len is len - 1 ! so we have (len - 1) / 2 characters before i
                 *      - 3 characters after i len/2
                 * */
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substr(start, end - start + 1);
    }
};



/**
 * Time complexity O(n^2)
 * Space complexity O(n^2)
 * */
class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for (int i = 0; i < n; i++)
        {
            dp[i][i] = true;
        }

        int L = 0, R = 0;

        for (int len = 1; len < n; len++)
        {
            for (int i = 0; i + len < n; i++)
            {
                if (len > 2)
                {
                    dp[i][i + len] = (s[i] == s[i + len]) && dp[i + 1][i + len - 1];
                }
                else
                {
                    dp[i][i + len] = (s[i] == s[i + len]);
                }
                if (dp[i][i + len] && len > R - L)
                {
                    L = i;
                    R = i + len;
                }
            }
        }
        return s.substr(L, R - L + 1);
    }
};

/**
 * Time complexity O(n^2 logn)
 * Space complexity O(1)
 * */
class Solution
{
public:
    bool isPal(string s)
    {
        int n = s.length();
        for (int i = 0; i < n / 2; i++)
        {
            if (s[i] != s[n - 1 - i])
            {
                return false;
            }
        }
        return true;
    }

    /**
     * Time complexity O(n^2)
     * */
    int good(string s, int len)
    {
        for (int i = 0; i + len <= s.length(); i++)
        {
            if (isPal(s.substr(i, len)))
            {
                return i;
            }
        }
        return -1;
    }

    string longestPalindrome(string s)
    {
        int n = s.length();

        int best_start = 0, best_len = 0;

        for (int parity : {0, 1})
        {
            int start = 1, end = n;
            if (start % 2 != parity)
            {
                start++;
            }
            if (end % 2 != parity)
            {
                end--;
            }
            while (start <= end)
            {
                int mid = (start + end) / 2;

                if (mid % 2 != parity)
                {
                    mid++;
                }

                int start_tmp = good(s, mid);
                if (start_tmp != -1)
                {
                    if (mid > best_len)
                    {
                        best_len = mid;
                        best_start = start_tmp;
                    }
                    start = mid + 2;
                }
                else
                {
                    end = mid - 2;
                }
            }
        }

        return s.substr(best_start, best_len);
    }
};

int main()
{
    Solution solution;
    string s = "abazabaa";
    cout << solution.longestPalindrome(s) << endl;
    // cout << solution.expand("babad", 1, 2) << endl;
    // cout << solution.good(s, 4) << endl;
}