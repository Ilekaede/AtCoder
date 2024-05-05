#include <iostream>

using namespace std;
int main(){
    int n, x, y, z; cin >> n >> x >> y >> z;
    for(int i = x; i <= y; i++){
        if(i == z){
            cout << "Yes" << endl;
            return 0;
        }
    }

    for(int i = y; i <= x; i++){
        if(i == z){
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;
    return 0;
}