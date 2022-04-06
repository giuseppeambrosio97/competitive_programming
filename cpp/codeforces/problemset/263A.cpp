#include <bits/stdc++.h>

using namespace std;

int main()
{
    int r, c;

    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            int val;
            cin >> val;
            if (val)
            {
                r = i;
                c = j;
            }
        }
    }

    cout << abs(r - 3) + abs(c - 3);
}