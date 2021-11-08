#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int it[n];
    int o = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> it[i];
    }

    for (int i = 0; i < n; i++)
    {
        if (it[i] > 0 && it[i] >= it[k - 1])
        {
            o++;
        }
    }

    cout << o;

    // if (it[k - 1] > 0)
    // {
    //     for (int i = k; i < n; i++)
    //     {
    //         if (it[k - 1] == it[i])
    //         {
    //             o++;
    //         }
    //         else
    //         {
    //             break;
    //         }
    //     }
    //     o = k + o;
    // }
    // else
    // {
    //     for (int i = k; i > 0; --i){
    //         if(it[i] == 0){

    //         }
    //     }
    // }
}