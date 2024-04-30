#include <iostream>
using namespace std;
typedef long long ll;

ll n;
ll a[200001], s[200001], t[200001];

int main(void)
{
  cin >> n;
  for(int i = 1; i <= n; i++) cin >> a[i];
  for(int i = 1; i <= n-1; i++) cin >> s[i] >> t[i];
  
  for(int i = 1; i <= n-1; i++) a[i+1] += a[i]/s[i] * t[i];
  cout << a[n] << endl;
  
  return 0;
}
