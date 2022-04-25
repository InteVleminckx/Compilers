#include <stdio.h>


int main(){
	int x = 5;
	int b = x + 5;

	{
		printf("Hello world!\n"); // Should print
	}
	{
		if (x != 4){
			printf("Hello world!\n"); // Should print
		}
	}
	return 1;
}
