#include <bits/stdc++.h>

using namespace std;

int isMaiusc(char ch)
{
    return (ch >= 65 && ch <= 90) ? true : false;
}

int compare(char *s1, char *s2)
{
    for (int i = 0; i < strlen(s1); i++)
    {
        if (isMaiusc(s1[i]))
        {
            s1[i] += 32;
        }
        if (isMaiusc(s2[i]))
        {
            s2[i] += 32;
        }
        if (s1[i] < s2[i])
        {
            return -1;
        }
        else if (s1[i] > s2[i])
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    char s1[100], s2[100];

    char ch;

    scanf("%s\n%s", s1, s2);

    cout << compare(s1, s2);
}