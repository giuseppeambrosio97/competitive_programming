#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> solve(vector<int> &a, vector<int> &b)
{
    vector<int> c(b.size());

    int i = 0, j = 0;
    for (int j = 0; j < b.size(); j++)
    {
        while (i < a.size() && a[i] < b[j]) // for each b[j] iterate through a until you find an element greater or equal to b[j]
        {
            i++;
        }
        c[j] = i;
        /**
         * this because when you exit the cycle i is equal:
         * 1) to n this means that b[j] is greater than all the element of a[]
         * 2) i < n && a[i] >= b[j] and in this case a[i] is smaller element greater or equal to b[j]. Since we start count from 0 the element
         *    we want to count are 0...i-1 and they are exactly i!
         * */
    }
    return c;
}

vector<int> solve_binary_search(vector<int> &a, vector<int> &b)
{
    vector<int> c(b.size());

    int i = 0, j = 0;
    for (int j = 0; j < b.size(); j++)
    {
        i = lower_bound(a.begin() + i, a.end(), b[j]) - a.begin();
        c[j] = i;
    }
    return c;
}

int main()
{

    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    vector<int> b(m);
    for (int j = 0; j < m; j++)
    {
        cin >> b[j];
    }

    for (int e : solve_binary_search(a, b))
    {
        cout << e << " ";
    }
    cout << "\n";

    // vector<int> a({0, 1, 1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15});

    // int lb = lower_bound(a.begin(), a.end(), 1) - a.begin();
    // int ub = upper_bound(a.begin(), a.end(), 1) - a.begin();

    // cout << lb << " " << ub << "\n";

    return 0;
}