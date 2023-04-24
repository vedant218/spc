%{
    int w,c,l;
%}


%%

[\n] {l++;w++;}
[ ] {w++;}
[a-zA-Z0-9] {c++;}

%%

int main()
{ 
    yylex();
    printf("%d,%d,%d",w,c,l);
    return 0;
}