/* 
 * File:   main.cpp
 * Author: 1020071
 *
 * Created on June 29, 2015, 12:31 PM
 */

#include <iostream>
#include <string>

using namespace std;

/*
 * 
 */

int main(){
    string sentence = "NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS SALTY";
    int wordCount = 0;
    for(int i = 0; i<sentence.size(); i++){
        if(sentence[i] == ' '){
            wordCount++;
        }
    }
    wordCount++;
    string arr[wordCount];
    for(int i = 0; i<wordCount;i++){
        int index = sentence.find(" ");
        if(index != sentence.npos){
            arr[i] = sentence.substr(0,index);
            sentence = sentence.substr(index+1, sentence.size()-index);
        }
        else{
            arr[i] = sentence.substr(0,sentence.size());
        }
    }
    int right = 0;
    int down = 0;
    bool reverse = false;
    for(int i = 0; i<wordCount; i++){
        if(i%2==0){
            reverse = false;
            if(arr[i].size()<right){
                for(int c = 0; c<arr[i].size()/2;c++){
                    swap(arr[i][c], arr[i][arr[i].size()-c-1]);
                }
                right=right-arr[i].size()+1;
                reverse = true;
            }
            else{
                reverse = false;
            }
            for(int j = 0; j<right-1; j++){
                cout<<" ";
            }
            cout<<arr[i];
            cout<<""<<endl;
            if(!reverse){
                right+=arr[i].size()-1;
            }
        }
        else{
            if(i!=wordCount-1){
                for(int l = 1; l<arr[i].size()-1;l++){
                    for(int j = 0; j<right-1; j++){
                        cout<<" ";
                    }
                    if(i==1){
                        cout<<" ";
                    }
                    cout<<arr[i][l]<<endl;
                }
                if(i==1){
                    right++;
                }
            }
            else{
                for(int l = 1; l<arr[i].size();l++){
                    for(int j = 0; j<right-1; j++){
                        cout<<" ";
                    }
                    cout<<arr[i][l]<<endl;
                }
            }
            down+=arr[i].size();
        }
    }
}