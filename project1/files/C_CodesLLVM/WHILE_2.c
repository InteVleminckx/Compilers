#include <stdio.h>

// Should print the numbers 1 - 5
int main(){
	int i = 0;
	while (i < 5){
		i++;
		printf("%d;\n", i);
		if (i == 4) {
			printf("i is %d ga naar 0: ", i);
			while(i != 0){
				i = i - 1;
				printf("---> %d ", i);
			}
		}
		if (i == 0){
			break;
		}
	}
	return 1;
}
