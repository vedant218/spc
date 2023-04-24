%{

%}

%%

[a|e|i|o|u] {
        printf("vowel %s",y);
        return 1;
    }

. {printf("consonant %s",yytext);return 1;}

%%

int main()
{
    char choice;
    do{
    printf("\nEnter a letter :\n");
    yylex();
    printf("\nDo you want to continue ? \n");
    scanf("%c",&choice);
    }
    while(choice == 'y');
    return 0;
}