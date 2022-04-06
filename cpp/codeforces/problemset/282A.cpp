#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, x = 0;
    cin >> n;

    while (n--)
    {
        char ch;
        bool add = false;
        for (int i = 0; i < 3; i++)
        {
            cin >> ch;

            if (ch == '+')
            {
                add = true;
            }
            else if (ch == '-')
            {
                add = false;
            }
        }
        if (add)
        {
            x++;
        }
        else
        {
            x--;
        }
    }

    cout << x;
}