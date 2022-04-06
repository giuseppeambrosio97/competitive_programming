#include <bits/stdc++.h>

using namespace std;

bool scan(vector<int> &a)
{
    bool repeat = false;
    for (int i = 0; i < a.size() - 1; i++)
    {
        if (a[i] > a[i + 1])
        {
            a[i] = a[i] + a[i + 1];
            a[i + 1] = a[i] - a[i + 1];
            a[i] = a[i] - a[i + 1];
            repeat = true;
        }
    }
    return repeat;
}

void bubble_sort(vector<int> &a)
{
    while (scan(a))
    {
    }
}

int main()
{
    vector<int> a = {85, 71, 56, 34, 107, 86, 64, 1, 0, 1000, 23, 156, 71, 107};
    bubble_sort(a);
    for (int e : a)
    {
        cout << e << " ";
    }
}