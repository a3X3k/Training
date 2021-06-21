#include <stdio.h>

int main() {

    char string_array1[1000000],string_array2[1000000];
    fgets(string_array1,1000000,stdin);
    fgets(string_array2,1000000,stdin);
    int size_of_string1=0,size_of_string2=0;
    
    for (size_of_string1 = 0; string_array1[size_of_string1] != '\0'; ++size_of_string1);
    for (size_of_string2 = 0; string_array2[size_of_string2] != '\0'; ++size_of_string2);
    
    if(size_of_string1<size_of_string2)
    {
        printf("First");
    }
    else if(size_of_string2<size_of_string1)
    {
        printf("Second");
    }
    else if(size_of_string2==size_of_string1)
    {
        printf("Equal");
    }
    return 0;
}