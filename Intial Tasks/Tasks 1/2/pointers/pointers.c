#include <stdio.h>

void Pointer_Sort(int* main_array,int total_size)
{
    for (int iterator1 = 0; iterator1<total_size; iterator1++) 
    { 
        for (int iterator2=iterator1+1; iterator2<total_size; iterator2++) 
        { 
            if (*(main_array + iterator2) < *(main_array + iterator1)) 
            { 
                int swap_key = *(main_array + iterator1); 
                *(main_array + iterator1) = *(main_array + iterator2); 
                *(main_array + iterator2) = swap_key; 
            } 
        } 
    }
    for (int ptr=0;ptr<total_size;ptr++) 
        printf("%d\n",*(main_array+ptr));
}

void main() 
{
    int size_of_the_array;
    scanf("%d\n",&size_of_the_array);
    
    int integer_array[size_of_the_array];
    for(int i=0;i<size_of_the_array;i++)
    {
        scanf("%d",&integer_array[i]);
    }
    Pointer_Sort(integer_array,size_of_the_array);
}
