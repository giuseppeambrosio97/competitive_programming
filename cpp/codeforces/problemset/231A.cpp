#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, o = 0;
    cin >> n;
    while (n--)
    {
        int it[3], c = 0;
        for (int i = 0; i < 3; i++)
        {
            cin >> it[i];
            if (it[i] == 1)
            {
                c++;
            }
        }
        if (c >= 2)
        {
            o++;
        }
    }
    cout << o << endl;
}