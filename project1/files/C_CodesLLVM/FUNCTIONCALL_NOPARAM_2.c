#include <stdio.h>

void a(){
	printf("a\n");
}

void b(){
	printf("b\n");
	a();
}

void c(){
	printf("c\n");
	b();
	a();
}
int main(){
	a();
	b();
	c();
	return 1;
}
