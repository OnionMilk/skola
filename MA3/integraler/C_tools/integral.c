#include <stdio.h>
#include <string.h>

int main(int argc, char argv[]) {
	char cur_char[2];
	int i;
	int j = 0;
	int br = 0;
	int in_length = strlen(argv);

	/*all function parts outside of brackets*/
	char part0[10];
	char part1[10];
	char part2[10];
	char part3[10];
	char part4[10];
	char part5[10];
	char part6[10];
	char part7[10];
	char part8[10];
	char part9[10];

	/*all function parts within brackets*/
	char bracket0[10];
	char bracket1[10];
	char bracket2[10];
	char bracket3[10];

	for(i = 0; i <= in_length; i++){

	    cur_char = argv[i];

	    if(cur_char == "("){

		if(br = 0){

		    char bracket0 = argv[0, i-1];
		    br++;
		}
	    }

	}
	printf("%c", bracket0);

	return 0;
}
