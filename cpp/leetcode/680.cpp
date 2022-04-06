#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    bool isPal(string s, int l, int r)
    {
        while (l < r)
        {
            if (s[l] != s[r])
            {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    bool validPalindrome(string s)
    {
        int count = 0, l = 0, r = s.length() - 1;
        while (l < r)
        {
            if (s[l] != s[r])
            {
                break;
            }

            l++;
            r--;
        }

        if (l >= r)
        {
            return true;
        }

        return isPal(s, l, r - 1) || isPal(s, l + 1, r);
    }
};