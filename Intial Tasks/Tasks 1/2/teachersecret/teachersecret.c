#include <stdio.h> 
#include <string.h>

int main() 
{ 
    int size;
    scanf("%d",&size);
    char array[size][1000]; 
    int marks[size];

    for (int i = 0; i < size; i++) 
        scanf("%s", array[i]); 
        
    for (int i = 0; i < size; i++) 
        scanf("%d", &marks[i]);
        
    char main_string[1000];
    scanf("%s",main_string);
    fgets(main_string,1000, stdin);
    int main_len=strlen(main_string);
    int tot_score=0;
    for(int i=0;i<size;i++)
    {
        int sub_len=strlen(array[i]);
        int frequency=0;
        for(int j=0;j<main_len;)
        {
            int index=0;
            int temp_count=0;
            while ((main_string[j] == array[i][index]))
            {
                temp_count++;
                index++;
                j++;
            }
            if(temp_count==sub_len)
            {
                temp_count=0;
                frequency++;
            }
            else
            {
                j++;
            }
        }
        tot_score=tot_score+(marks[i]*frequency);
    }
    printf("%d",tot_score);
}

