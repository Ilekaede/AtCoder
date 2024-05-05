#include <iostream>
#include <vector>
using namespace std;
int main(){
    int N; cin >> N;
    vector<int> A(N), B(N);
    for(int i = 0; i < N; i++){
        cin >> A[i] >> B[i];
    }
    long long int ans = 0;
    long long int max_head = B[0] - A[0]; //頭の高さの基準
    for(int i = 0; i < N; i++){
        ans += A[i];
        if(max_head < B[i] - A[i]){
            max_head = B[i] - A[i];
        }
    }
    cout << ans + max_head << endl;

    return 0;
}