#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> solve(vector<int> &a, vector<int> &b)
{
    vector<int> c(a.size() + b.size());

    int i = 0, j = 0, k = 0;
    while (i < a.size() || j < b.size()) // loop while there are at least one element in one the the two arrays
    {
        if (j == b.size() || (i < a.size() && a[i] < b[j])) // we pick the element a[i] if a[i] < a[j] and i < a.size() OR j == b.size() (there are no more elements in b)
        {
            c[k++] = a[i++];
        }
        else
        {
            c[k++] = b[j++];
        }
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

    for (int e : solve(a, b))
    {
        cout << e << " ";
    }
    cout << "\n";

    return 0;
}