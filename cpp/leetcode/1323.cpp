#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int maximum69Number(int num)
    {
        int pos_last_six = 0, q = 1, m = 10, dg;

        while ((dg = (num % m) / q) != 0)
        {
            if (dg == 6)
            {
                pos_last_six = q;
            }

            q *= 10;
            m *= 10;
        }

        return num + 3 * pos_last_six;
    }
};

int main()
{
    Solution solution;
    cout << solution.maximum69Number(9999) << endl;
}