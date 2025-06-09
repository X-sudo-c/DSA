#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int main(){

    char choice [12];
    int x;
    int y;

    printf("Welcome to simple calculator\n");
    printf("\n");

    printf("Do you want to add subtract or divide? :\n");

    scanf("%s", choice);


    // switch (choice){ 
    //     case 'add' :
    //     printf("enter your first number: \n");
    //     scanf("%d", &x);
    //     printf("enter your second number: \n");
    //     scanf("%d", &y);
    //     printf("the sum is %d", x + y);

        
    // }
    // so i found out that you cant compare strings in using the switch statement its only used for ints and char
    //and also you dont need to add & to an array just do scanf("%s", <array name no '&'>)



    if (strcmp(choice, "add")== 0)
    {
        printf("you want to add ?");
    }
    else if(strcmp(choice, "subtract")== 0)
    {
        printf("you want to subtract");
    }
    else if(strcmp(choice, "divide") == 0)
    {
        printf("you want to divide");
    }else{
        printf("Invalid operation selected");
    }


    



    return 0;
}