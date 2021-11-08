#include <bits/stdc++.h>

using namespace std;

int main()
{
    int r, c, out;
    cin >> r >> c;

    if (r % 2 == 0)
    {
        out = r / 2 * c;
    }
    else if (c % 2 == 0)
    {
        out = c / 2 * r;
    }
    else
    {
        out = (r - 1) / 2 * (c - 1) + (r - 1) / 2 + (c - 1) / 2;
    }
    cout << out;
}