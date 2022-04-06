#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int balancedStringSplit(string s)
    {
        int count = 0;
        int i = 0, n = s.length();
        while (i < n)
        {
            int L = 0;
            do
            {
                if (s[i] == 'R')
                {
                    L--;
                }
                else
                {
                    L++;
                }
                i++;
            } while (L != 0);
            count++;
        }
        return count;
    }
};

int main()
{
    Solution solution;
    string s = "LLLLRRRR";
    cout << solution.balancedStringSplit(s) << endl;
}