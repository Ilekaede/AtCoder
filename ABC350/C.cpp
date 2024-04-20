#include <iostream>
#include <vector>
#include <set>
#include <tuple>
using namespace std;
int main(){
    int N; cin >> N;
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    set<tuple<int, int> > st;
    for(int i = 0; i < N - 1; i++){
        int m = i;
        for(int j = i+1; j < N; j++){
            if(A[j] < A[m]){
                m = j;
            }
        }
        if(m != i){
            int temp = A[i];
            A[i] = A[m];
            A[m] = temp;
            st.emplace(i+1, m+1);
        }
    }

    cout << st.size()<< endl;
    for(const auto& element:st){
        cout << get<0>(element) << " " << get<1>(element)<< endl;
    }

    return 0;
}


