#include <bits/stdc++.h>

using namespace std;

bool type1player(string a, int i)
{
    return a[i] == '1' ? true : false;
}

char get_char(string res, int i, int j, int n)
{
    return res[i * (n + 1) + j];
}

void set_char(string &res, int i, int j, int n, char ch)
{
    res[i * (n + 1) + j] = ch;
}

string solve(string a)
{
    int n = a.size();
    string res(n * (n + 1), '=');
    for (int i = 0; i < n; i++)
    {
        set_char(res, i, n, n, '\n');
        set_char(res, i, i, n, 'X');
    }

    // int c = 0;
    // int i = 0;
    // int first_player2 = -1, last_player2 = -1;

    // while (i < n)
    // {
    //     if (!type1player(a, i))
    //     {
    //         c++;

    //         if (first_player2 == -1)
    //         {
    //             first_player2 = i;
    //         }

    //         int j = i + 1;

    //         bool find = false;

    //         while (j < n)
    //         {
    //             if (!type1player(a, j))
    //             {
    //                 find = true;
    //                 set_char(res, i, j, n, '+');
    //                 set_char(res, j, i, n, '+');
    //             }
    //             j++;
    //         }

    //         if (!find)
    //         {
    //             last_player2 = i;
    //             break;
    //         }

    //         i = j;
    //     }
    //     else
    //     {
    //         i++;
    //     }
    // }

    // set_char(res, first_player2, last_player2, n, '+');
    // set_char(res, last_player2, first_player2, n, '+');

    vector<int> players2;

    for (int i = 0; i < n; i++)
    {
        if (!type1player(a, i))
        {
            players2.push_back(i);
        }
    }

    if (players2.size() == 0)
    {
        return "YES\n" + res;
    }

    int k = players2.size();

    if (k <= 2)
    {
        return "NO\n";
    }

    for (int i = 0; i < k; i++)
    {
        set_char(res, players2.at(i), players2.at((i + 1) % k), n, '+');
        set_char(res, players2.at((i + 1) % k), players2.at(i), n, '-');
    }

    return "YES\n" + res;
}

int main()
{
    int t;

    cin >> t;

    vector<string> player;
    vector<string> res;

    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        string a;
        cin >> a;
        res.push_back(solve(a));
        player.push_back(a);
    }

    for (int i = 0; i < t; i++)
    {
        cout << res.at(i);
    }
}