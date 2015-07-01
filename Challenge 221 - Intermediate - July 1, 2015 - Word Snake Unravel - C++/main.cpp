#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;
int main() {
    int height = 0;
    int width = 0;
    std::ifstream file("input.txt");
    std::string line;
    cout<<line;
    if(file.is_open()){
        getline(file,line);
        height = atoi(line.c_str());
        string grid[height];
        int count = 0;
        while(getline(file, line)){
            if(count != height-1){
                line = line.substr(0, line.size()-1);
            }
            cout<<line<<endl;
            grid[count] = line;
            if(line.size()>width){
                width = line.size();
            }
            count++;
        }
        cout<<"\n";
        for(int i = 0; i<height; i++){
            for(int j = grid[i].size();j<width;j++){
                grid[i]+=' ';
            }
        }
        bool up = false, down = false, left = false, right = false, done = false, newWord = false;
        char tempChar = '!';
        void * lastChar = static_cast<void *>(&tempChar);
        string word = "";
        string words = "";
        for(int h = 0, w = 0; !done;){
            word.push_back(grid[h][w]);
            if(h == 0 || grid[h-1][w] == ' ' || static_cast<void *>(&grid[h-1][w]) == lastChar){
                if(up){
                    newWord = true;
                    up = false;
                }
            }
            else{
                up = true;
            }
            if(w == 0 || grid[h][w-1] == ' ' || static_cast<void *>(&grid[h][w-1]) == lastChar){
                if(left){
                    newWord = true;
                    left = false;
                }
            }
            else{
                left = true;
            }
            if(h == height-1 || grid[h+1][w] == ' ' || static_cast<void *>(&grid[h+1][w]) == lastChar){
                if(down){
                    newWord = true;
                    down=false;
                }
            }
            else{
                down = true;
            }
            if(w == width-1 || grid[h][w+1] == ' ' || static_cast<void *>(&grid[h][w+1]) == lastChar){
                if(right){
                    newWord = true;
                    right = false;
                }
            }
            else{
                right = true;
            }
            if(newWord){
                word.push_back(' ');
                words += word;
                word = "";
                word.push_back(grid[h][w]);
                newWord = false;
            }
            lastChar = static_cast<void *>(&grid[h][w]);
            if(up) h--;
            if(down) h++;
            if(left) w--;
            if(right) w++;
            done = !up && !down && !left && !right;
        }
        cout<<words<<endl;
    }
    file.close();
    return 0;
}

