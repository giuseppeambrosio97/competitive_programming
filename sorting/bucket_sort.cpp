#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

/**
 * This function given an integer el, the range of the values that el can assume (defined by M), the number of bucket we want
 * return the index of the bucket of el (zero based -> 0,1,...,k-1)
 *
 * 
 * 0-> 0...M*(1/k)-1
 * 1-> M*(1/k)...M*(2/k)-1
 * 2-> M*(2/k)...M*(3/k)-1
 * ...
 * k-1-> M*(k-1)/k...M-1
 * 
 * 
 * 
 * M=100 and k=5
 * 0->0...19
 * 1->20...39
 * 2->40...59
 * 3->60...79
 * 4->80...99
 * @param  {int} el : 
 * @param  {int} M  : 
 * @param  {int} k  : 
 * @return {int}    : 
 */
int getBucket(int el, int M, int k)
{
    return (el * k / M);
}
/**
 * @param  {vector<int>} a : 
 * @param  {int} M         : define the range of element in a -> a[i] in [0,...,M-1]
 * @param  {int} k         : number of bucket we will use
 * @return {vector<int>}  a_sorted : 
 */
vector<int> bucket_sort_with_sort(vector<int> a, int M, int k)
{
    vector<int> a_sorted;

    vector<vector<int>> b(k, vector<int>());

    for (int e : a)
    {
        b[getBucket(e, M, k)].push_back(e);
    }
    for (auto bi : b)
    {
        sort(bi.begin(), bi.end());
        for (auto bij : bi)
        {
            a_sorted.push_back(bij);
        }
    }

    return a_sorted;
}

vector<int> recursive_bucket_sort(vector<int> a, int M, int k)
{
    if (a.size() == 1)
    {
        return a;
    }
    if (a.empty())
    {
        return a;
    }

    vector<int> a_sorted;

    vector<vector<int>> b(k, vector<int>());

    for (int e : a)
    {
        b[getBucket(e, M, k)].push_back(e);
    }
    for (auto bi : b)
    {
        if (!bi.empty())
        {
            vector<int> bi_sorted = recursive_bucket_sort(bi, M / k, k);
            for (auto bij : bi_sorted)
            {
                a_sorted.push_back(bij);
            }
        }
    }
    return a_sorted;
}

int main()
{
    // int n;
    // cin >> n;
    vector<int> a = {70, 40, 25, 10, 8, 30, 60, 90, 80, 50, 41, 21};
    // vector<int> a;
    // while (n--)
    // {
    //     int e;
    //     cin >> e;
    //     a.push_back(e);
    // }

    for (int e : recursive_bucket_sort(a, 100, 5))
    {
        cout << e << " ";
    }
    cout << "\n";
}