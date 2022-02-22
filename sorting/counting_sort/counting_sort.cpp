#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> counting_sort(vector<int> a)
{

    //PREPROCESSING STEP
    int k = *max_element(a.begin(), a.end()) + 1;
    int b[k] = {0};

    for (int e : a)
    {
        b[e]++;
    }

    for (int i = 1; i < k; i++)
    {
        b[i] += b[i - 1];
    }

    for (int i = k - 1; i > 0; i--)
    {
        b[i] = b[i - 1];
    }

    b[0] = 0;

    //ASSIGNMENT STEP
    vector<int> a_sorted(a.size(), 0);
    for (int e : a)
    {
        a_sorted[b[e]] = e;
        b[e]++;
    }

    return a_sorted;
}

int main()
{
    int n;
    cin >> n;
    // vector<int> a = {1, 0, 3, 1, 3, 1};
    vector<int> a;
    while (n--)
    {
        int e;
        cin >> e;
        a.push_back(e);
    }

    for (int e : counting_sort(a))
    {
        cout << e << " ";
    }
    cout << "\n";
}