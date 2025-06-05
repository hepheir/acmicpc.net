#include <iostream>

using namespace std;

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);

    string s;

    cin >> s;
    int i = 0;
    int j = s.length()-1;

    while (i < j) {
        if (s[i] != s[j]) {
            cout << 0;
            return 0;
        }
        i++;
        j--;
    }
    cout << 1;

    return 0;
}

X second

X*3+2
X*3+2