#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int minimumSum(int num)
    {
        int dg[4] = {0};

        for (int i = 0; i < 4; i++)
        {
            dg[i] = num % 10;
            num /= 10;
        }

        sort(dg, dg + 4);

        int n1 = dg[0] * 10 + dg[2], n2 = dg[1] * 10 + dg[3];

        return n1 + n2;
    }
};

int main()
{
    Solution solution;
    cout << solution.minimumSum(4009) << endl;
}