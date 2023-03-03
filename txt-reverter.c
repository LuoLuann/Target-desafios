#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   
    char* txt = (char*) malloc(sizeof(char));
    char temp;
    int i, j;
    
    
    while(1) {
        printf("entre com a palavra a ser invertida: ");
    //fgets(txt, sizeof(strlen(txt)), stdin);
        scanf("%s", txt); 
        i = 0;
        j = strlen(txt) - 1;
        j = strlen(txt) - 1;
        while(i < j){
            temp = txt[i];
            txt[i] = txt[j];
            txt[j] = temp;
            i++;
            j--;
        }
        printf("\nInvertida: %s\n", txt);
    
    }
    return 0;
}
