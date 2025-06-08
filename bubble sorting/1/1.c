#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int main(){

    char choice [12];
    int x;
    int y;

    printf("Welcome to simple calculator\n");
    printf("\n");

    printf("Do you want to add subtract of divide? :\n");

    scanf("%s", &choice);


    switch (choice){ 
        case 'add' :
        printf("enter your first number: \n");
        scanf("%d", &x);
        printf("enter your second number: \n");
        scanf("%d", &y);
        printf("the sum is %d", x + y);

        
    }


    



    return 0;
}