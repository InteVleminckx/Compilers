#include <stdio.h>

// Should print the numbers 1 - 5
int main(){
	int i = 0;
	while (i < 5){
		i++;
		printf("%d;\n", i);
		if (i == 4) {
			printf("%s\n", "Reached 4");
		}
	}
	return 1;
}
