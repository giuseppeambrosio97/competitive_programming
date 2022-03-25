#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int digits(int e)
{
    return int(log10(e)) + 1;
}

vector<int> radix_sort(vector<int> a)
{

    vector<int> sorted_a(a);

    int m = 10, q = 1;

    //find the number of digits of the greatest number
    int d = -1;
    for (int e : a)
    {
        int ed = digits(e);
        d = (ed > d) ? ed : d;
    }

    for (int i = 1; i <= d; i++)
    {
        vector<vector<int>> b(10, vector<int>());
        //BUCKET SORT ON DIGIT i
        for (int e : sorted_a)
        {
            int ed = (e % m) / q;
            b[ed].push_back(e);
        }

        int id = 0;
        for (int j = 0; j < 10; j++)
        {
            for (int k = 0; k < b[j].size(); k++)
            {
                sorted_a[id] = b[j][k];
                id++;
            }
        }

        m *= 10;
        q *= 10;
    }

    return sorted_a;
}

int main()
{
    int n;
    cin >> n;
    // vector<int> a = {85, 71, 56, 34, 107, 86, 64};
    vector<int> a;
    while (n--)
    {
        int e;
        cin >> e;
        a.push_back(e);
    }

    for (int e : radix_sort(a))
    {
        cout << e << " ";
    }
    cout << "\n";
}