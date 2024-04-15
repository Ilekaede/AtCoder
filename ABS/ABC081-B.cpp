#include <iostream>
#include <vector>

using namespace std;
int main(){
    int N; cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }

    bool flag = true;
    int cnt = 0;
    while(flag){
        for(int i = 0; i < N; i++){
           if(A[i]%2 == 0){
                A[i] = A[i]/2;
           }
           else{
                flag = false;
                break;
           }
        }

        if(flag){
            cnt++;
        }

    }

    cout << cnt << endl;

    return 0;
}