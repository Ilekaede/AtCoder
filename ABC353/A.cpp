#include <iostream>
#include <vector>
using namespace std;
int main(){
    int N; cin >> N;
    int H; cin >> H;
    for(int i = 1; i < N; i++){
        int h; cin >> h;
        if(H < h){
            cout << i + 1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}