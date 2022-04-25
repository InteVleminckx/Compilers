#include <stdio.h>

int main(){
    // this should print the numbers: 0, 1, 2, 3, 4, 5
	int i = 0;
	int j = 0;
	while(i < 10){
		while (j < 10){
			printf("i: %d, j: %d \n", i,j);
			j++;
		}
		j = 0;
		i++;
	}
	return 0;
}
