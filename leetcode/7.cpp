#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    int reverse(int x)
    {
        int rev = 0;
        while (x)
        {
            int digit = x % 10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && digit >= INT_MAX % 10))
            {
                return 0;
            }
            else if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && digit <= INT_MIN % 10))
            {
                return 0;
            }

            rev = rev * 10 + digit;
            x /= 10;
        }
        return rev;
    }
};

int main()
{
    Solution s;
    cout << s.reverse(-3210) << endl;
}