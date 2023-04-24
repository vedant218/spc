%{


%}


%%


([a-zA-Z]*) {
        printf("word");
        return 1;
    }

[0-9]* {
        printf("number");
        return 1;
    }

([a-zA-Z0-9]*) {
        printf("alphanumeric");
        return 1;
    }

%%

int main()
{
    char choice;
    do{
    printf("Enter a string : ");
    yylex();
    printf("\nDo you want to continue ? \n");
    scanf("%c",&choice);
    }
    while(choice == 'y');
    return 0;
}