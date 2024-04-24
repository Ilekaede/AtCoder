#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main(){
    int H, W, N; cin >> H >> W >> N;
    string T; cin >> T;
    vector< vector<char> > S(H, vector<char>(W));
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            cin >> S[i][j];
        }
    }
    int cnt = 0;
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            if(S[i][j] == '#'){
                continue;
            }
            else if(i == 0 || j == 0 || i == H - 1 || j == W - 1){
                continue;
            }
            else{
                int y = i;
                int x = j;
                for(int k = 0; k < N; k++){
                    if(T[k] == 'L'){
                        if(S[y][x - 1] == '#'){
                            break;
                        }
                        else{
                            x--;
                        }
                    }
                    else if(T[k] == 'R'){
                        if(S[y][x + 1] == '#'){
                            break;
                        }
                        else{
                            x++;
                        }
                    }
                    else if(T[k] == 'U'){
                        if(S[y - 1][x] == '#'){
                            break;
                        }
                        else{
                            y--;
                        }
                    }
                    else if(T[k] == 'D'){
                        if(S[y + 1][x] == '#'){
                            break;
                        }
                        else{
                            y++;
                        }
                    }
                    if(k == N - 1){
                        cnt++;
                    }
                }
            }
        }
    }

    cout << cnt << endl;
    return 0;
}