#include <stdio.h>

int main(){
	char buf[5];
	
	read(0,buf,5);
	puts(buf);

	return 0;

}