#include <stdio.h>

void main() 
{
    int size_of_array;
    scanf("%d",&size_of_array);
    float array[size_of_array];
    float average=0;
    for(int i=0;i<size_of_array;i++)
    {
        scanf("%f",&array[i]);
        average+=array[i];
    }
    float avg=average/(float)size_of_array;
    int counter=0;
    while(avg<9.5)
    {
        average+=10;
        counter++;
        avg=average/(float)(size_of_array+counter);
    }
    printf("%d",counter);
}

