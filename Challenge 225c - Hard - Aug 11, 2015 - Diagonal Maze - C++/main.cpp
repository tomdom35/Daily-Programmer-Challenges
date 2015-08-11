#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int main () {
string line;
ifstream myfile ("Maze.txt");
if (myfile.is_open()){
    getline(myfile,line);
    istringstream buffer(line);
    int numLines;
    buffer>>numLines;
    string lines[numLines];
    int mazeHeight = -1;
    int mazeWidth = -1;
    for (int i = 0; getline (myfile,line); i++ )
    {
        lines[i] = line;
        if(i==0){
            mazeWidth = std::count(line.begin(), line.end(), '+')-1;
        }
        if(line.at(0) == '+'){
            mazeHeight++;
        }
    }
    myfile.close();
    
    //Get Dimensions 
    int mazeThickness = ((numLines-1)/mazeHeight) - 1;
    int mazeLength = lines[0].size();
    int numHorzLines = mazeHeight+1;
    int numVertLines = mazeWidth+1;
    int diagonalSize = mazeThickness*10;
    int startIndent = mazeThickness*mazeHeight;
    string diagonalGrid[diagonalSize];
    
    //Create Empty Maze (Grid)
    string tempString = "";
    for(int i = 0; i<diagonalSize;i++){
        tempString += " ";
    }
    for(int i = 0; i<diagonalSize;i++){
        diagonalGrid[i] = tempString;
    }
    
    //Set Horizontal Lines
    for(int i = 0, j = 0, indent=startIndent; i<numHorzLines; i++, j+=mazeThickness+1,indent-=mazeThickness){
        int rightIndent = indent;
        int downIndent = (j-i);
        for(int k = 1; k<mazeLength-1; k+=mazeThickness+1){
            if(lines[j][k] == '-'){
                for(int count = 0; count<mazeThickness;count++, rightIndent++, downIndent++){
                    diagonalGrid[downIndent][rightIndent] = '\\';
                }
            }
            else{
                rightIndent+=mazeThickness;
                downIndent+=mazeThickness;
            }
        }
    }
    
    //Set Vertical Lines
    for(int i = 0, j = 0, indent=startIndent-1; i<numVertLines; i++, j+=mazeThickness+1,indent+=mazeThickness){
        int rightIndent = indent;
        int downIndent = (j-i);
        for(int k = 1; k<numLines-1; k+=mazeThickness+1){
            if(lines[k][j] == '|'){
                for(int count = 0; count<mazeThickness;count++, rightIndent--, downIndent++){
                    diagonalGrid[downIndent][rightIndent] = '/';
                }
            }
            else{
                rightIndent-=mazeThickness;
                downIndent+=mazeThickness;
            }
        }
    }
    
    //Print Maze
    for(int i = 0; i<diagonalSize; i++){
        cout<<diagonalGrid[i]<<endl;
    }
}
else cout << "Unable to open file"; 

return 0;
}
