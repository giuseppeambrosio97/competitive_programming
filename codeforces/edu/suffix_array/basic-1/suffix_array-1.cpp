#include <bits/stdc++.h>

using namespace std;

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
        //take cyclic substrings of length 2^k
        vector<pair<pair<int, int>, int>> a(n); // this array will contain the encoding of the substring based on the equivalence classes in c[p[]]
                                                // of the encode cyclic substring with equivalence classes in c[p[]]. This encoding is formed by two part:
                                                // two indexes, the first is the index of the substring of the first 2^{k-1} characters and the second is the
                                                // index of the substring of the other 2^{k-1} characters
        for (int i = 0; i < n; i++)
        {
            a[i] = {{c[i],
                     c[(i + (1 << k)) % n]},
                    i};
        }
        sort(a.begin(), a.end());

        //new array p
        for (int i = 0; i < n; i++)
        {
            p[i] = a[i].second;
        }
        //new array c
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
