#include <stdio.h>

int main(){
    // Should print the numbers from 0 to 9
	for(int a = 0; a < 10; a++){
		printf("a = %d --> b's: |", a);
		for(int b = 0; b < 10; b++){
			printf(" %d |", b);
		}
		printf("\n");
	}
	return 0;
}
