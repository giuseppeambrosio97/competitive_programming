#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int longestPalindrome(string s)
    {
        unordered_map<char, int> h;
        int n = s.length();

        for (int i = 0; i < n; i++)
        {
            h[s[i]]++;
        }
        int len = 0;
        for (auto &it : h)
        {
            len += it.second / 2 * 2;
        }

        return (n - len > 0 ? 1 : 0) + len;
    }
};

class Solution
{
public:
    int longestPalindrome(string s)
    {
        int h[128] = {0};
        int n = s.length();

        for (int i = 0; i < n; i++)
        {
            h[s[i]]++;
        }
        int len = 0;
        for (int val : h)
        {
            len += val / 2 * 2;
        }

        return (n - len > 0 ? 1 : 0) + len;
    }
};

int main()
{
    Solution solution;
    cout << solution.longestPalindrome("abccccdd") << endl;
}