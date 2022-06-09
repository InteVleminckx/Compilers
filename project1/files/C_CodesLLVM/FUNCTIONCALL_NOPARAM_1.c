#include <stdio.h>

void f(int a){
	printf("Hello %d", a);
	return;
}

void g(){
	printf("World\n");
	f();
	printf("World\n");
}

int main(){
    // Should print "hello world" twice
	f();
	g();
	return 1;
}
