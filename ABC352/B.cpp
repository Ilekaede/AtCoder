#include <iostream>
#include <vector>

using namespace std;
int main(){
    string S; cin >> S;
    string T; cin >> T;
    int cnt = 0;
    int index = 0;
    while(cnt != S.length()){
        for(int i = index; i < T.length(); i++){
            
            if(S[cnt] == T[i]){
                cout << i + 1;
                cnt++;
                index = i + 1;
                break;
            }
        }
        if(cnt == S.length()){
            cout << endl;
        }
        else{
            cout << " ";
        }
    }

    return 0;
}