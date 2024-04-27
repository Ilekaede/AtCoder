#include <iostream>
#include <vector>

using namespace std;
int main(){
    int N;
    cin >> N;
    vector<vector<char> > A(N, vector<char>(N)), B(N, vector<char>(N));
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> A[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> B[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(A[i][j] != B[i][j]){
                cout << i + 1 << " " << j + 1 << endl;
                return 0;
            }
        }
    }

    return 0;

}