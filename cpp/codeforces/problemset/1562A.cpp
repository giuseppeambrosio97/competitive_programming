#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * This solution has time complexity of O(r-l) 
 * */
int solve_linear(int r, int l)
{
    int mx = -1;
    for (int b = l; b <= r; b++)
    {
        int val = min(r - b, b - 1);
        if (val > mx)
        {
            mx = val;
        }
        else
        {
            return mx;
        }
    }
    return mx;
}


/**
 * First intuition: given (r,l) for a generic l<=b<=r the best b<=a<=r (such that a%b is max)
 *                  is min(r-b,b-1)-> 
 *                         if b+b-1 <= r -> b-1
 *                         if b+b-1 >  r -> r-b
 *                  a = b + min(r-b,b-1)
 * 
 * Example: (26,1) and b = 5 the best a is 9, but we can see that for example b = 6 is a better choice compared with b=5
 *          because the best a for b = 6 is 11 and give us a solution of 5 (4 is the solution associated with b = 5)
 * 
 * Second intuition: we want that b such that:
 *                  - b + b - 1 <= r because for a generic b we hope the best and the best is b-1
 *                  - r - b is min   because we want to waste as little as possible
 * 
 * Example: (26,1) and b = 5 the best a is 9 and the associated solution is 4 but we are wasting a lot because
 *          r-b = 26-5 = 21. This will say us that for sure will be better after.
 *          
 * */
int solve(int r, int l)
{
    return min(r - l, l - 1);
}

int main()
{
    // int t;

    // cin >> t;

    // vector<int> sols(t);

    // for (int i = 0; i < t; i++)
    // {
    //     int l, r;
    //     cin >> l >> r;

    //     sols[i] = solve_linear(r, l);
    // }

    // for (int e : sols)
    // {
    //     cout << e << "\n";
    // }

    cout << solve_linear(26, 8);
}