#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        int l = 0, r = s.length() - 1;

        while (l < r && l < s.length() && r >= 0)
        {
            while (l < r && !iswalnum(s[l]))
            {
                l++;
            }

            while (l < r && !iswalnum(s[r]))
            {
                r--;
            }

            if (tolower(s[l]) != tolower(s[r]))
            {
                return false;
            }
            r--;
            l++;
        }

        return true;
    }
};

int main()
{
    Solution solution;
    cout << solution.isPalindrome(".,") << endl;
}