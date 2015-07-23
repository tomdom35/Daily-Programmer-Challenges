#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
	randSwap();
    return 0;
}

int randSwap(){
	srand(time(NULL));
	int list[] = {0,1,2,3,4,5,6,7,8,9};
	int listSize = (sizeof(list)/sizeof(int));
    int r = rand() % (listSize);
    int i = 0;
    while(i<listSize){
        int indexOne = rand() % (listSize);
        int indexTwo = rand() % (listSize);
        int temp = list[indexOne];
        list[indexOne] = list[indexTwo];
        list[indexTwo] = temp;
        i = i+1;
    }
    i = 0;
    while(i<listSize){
        printf("%d\n", list[i]);
        i = i + 1;
    }
    return 0;
}