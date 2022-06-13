#include <stdio.h>

void f(){
	printf("Hello");
	return;
}

void g(int a){
	printf(" World\n");
	f();
	printf(" World\n");
	printf("Number a is equal to %d", a);
}

int main(){
    // Should print "hello world" twice
	f();
	g(5);
	return 1;
}