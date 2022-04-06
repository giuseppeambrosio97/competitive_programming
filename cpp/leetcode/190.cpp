#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        uint32_t n_reverse = 0;
        for (int i = 0; i <= 31; i++)
        {
            if (n & (1 << i))
            {
                n_reverse = (n_reverse << 1) + 1;
            }
            else
            {
                n_reverse = n_reverse << 1;
            }
        }

        return n_reverse;
    }
    void represent(uint32_t n)
    {
        for (int i = 31; i >= 0; i--)
        {

            if (n & (1 << i))
            {
                cout << 1 << " ";
            }
            else
            {
                cout << 0 << " ";
            }
        }
    }
};

int main()
{
    Solution solution;

    uint32_t reverse = solution.reverseBits(3);
    solution.represent(3);
    cout << "\n";
    solution.represent(reverse);
}