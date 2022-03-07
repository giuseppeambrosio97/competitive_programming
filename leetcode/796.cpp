#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    bool rotateString(string s, string goal)
    {
        int n = s.length();
        for (int i = 0; i < n; i++)
        {
            bool good = true;
            for (int j = 0; j < n; j++)
            {
                if (s[(i + j) % n] != goal[j])
                {
                    good = false;
                    break;
                }
            }
            if (good)
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    Solution solution;
    cout << solution.rotateString("abcde", "cdeab") << "\n";
}