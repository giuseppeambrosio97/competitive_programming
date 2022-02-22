#include <bits/stdc++.h>

using namespace std;

/**
 * Counting sort of array p by keys in array C. The idea is that elements in p are just item at each element is associated
 * a key in c (i.e. the equivalence class)
 * @param  {vector<int>} p : 
 * @param  {vector<int>} c : 
 */
void counting_sort(vector<int> &p, vector<int> &c)
{
    int n = p.size();

    {
        vector<int> cnt(n);
        for (auto x : c)
        {
            cnt[x]++;
        }

        vector<int> p_new(n);
        vector<int> pos(n);
        pos[0] = 0;
        for (int i = 1; i < n; i++)
        {
            pos[i] = pos[i - 1] + cnt[i - 1];
        }
        for (auto x : p)
        {
            int i = c[x];
            p_new[pos[i]] = x;
            pos[i]++;
        }
        p = p_new;
    }
}

int main()
{
    //INPUT
    string s;
    cin >> s;
    s += "$";
    //declare var
    int n = s.size();
    vector<int> p(n); //array with index of the suffixes ->
                      // p[i] is equal at the index associated at the suffix actually in position i in the lexicographically order
                      // ad each iteration k it contains the substring with length 2^k

    vector<int> c(n); //array with equivalence classes ->
                      //c[i]=equivalence class of the suffix with index i, so if we lookup the array c by indexing on the output of the lookup
                      // on the array p, we have-> c[p[i]] the equivalence class of the suffix in position i in the lessico lexicographically order
    {
        //k=0 -> single character
        vector<pair<char, int>> a(n); //it contains the character and the index associated in the input string
        for (int i = 0; i < n; i++)
        {
            a[i] = {s[i], i};
        }
        sort(a.begin(), a.end());

        //init p,c
        for (int i = 0; i < n; i++)
        {
            p[i] = a[i].second;
        }
        c[p[0]] = 0;
        for (int i = 1; i < n; i++)
        {
            if (a[i].first == a[i - 1].first)
            {
                c[p[i]] = c[p[i - 1]];
            }
            else
            {
                c[p[i]] = c[p[i - 1]] + 1;
            }
        }
    }

    /*
        s=ababba$
        k=0
        vector <char,int> a = {(a,0),(b,1),(a,2),(b,3),(b,4),(a,5),($,6)}
        vector <char,int> a_sorted = {($,6),(a,0),(a,2),(a,5),(b,1),(b,3),(b,4)}
        p[]=   [6,0,2,5,1,3,4]
        c[]=   [1,2,1,2,2,1,0]
        c[p[]]=[0,1,1,1,2,2,2]
    */
    int k = 0;
    while ((1 << k) < n) //loop while 2^k < n
    {

        //with this we have the string of length 2^{k+1} sorted by the second half (first digit of the number)
        for (int i = 0; i < n; i++)
        {
            p[i] = (p[i] - (1 << k) + n) % n;
        }

        //sorting the strings by the first half (second digit of the number)
        counting_sort(p, c);

        //we need to build the new equivalence classes using old equivalence classes
        vector<int> c_new(n);
        c_new[p[0]] = 0;
        for (int i = 1; i < n; i++)
        {
            pair<int, int> prev = {c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n]};
            pair<int, int> now = {c[p[i]], c[(p[i] + (1 << k)) % n]};
            if (now == prev)
            {
                c_new[p[i]] = c_new[p[i - 1]];
            }
            else
            {
                c_new[p[i]] = c_new[p[i - 1]] + 1;
            }
        }
        c = c_new;
        //sort it
        k++;
    }

    // for (int i = 0; i < n; i++)
    // {
    //     cout << p[i] << " " << s.substr(p[i], n - p[i]) << "\n";
    // }
    for (int i = 0; i < n; i++)
    {
        cout << p[i] << " ";
    }
}
