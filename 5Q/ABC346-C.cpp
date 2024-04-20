#include <iostream>
#include <set>
#include <vector>
using namespace std;
int main(){
    long long int N, K; cin >> N >> K;
    set<long long int> st;
    long long int A;
    for(long long int i = 0; i < N; i++){
        cin >> A;
        st.insert(A);
    }

    long long int sum = (1 + K) * K / 2;

    for(auto x:st){
        if(x >= 1 && x <= K){
            sum -= x;
        }
    }

    cout << sum << endl;
    return 0;
}