#include<stdio.h>

int powerof(int number, unsigned int base) 
{ 
    int temp; 
    if( base == 0) 
        return 1; 
    temp = powerof(number, base/2); 
    if (base%2 == 0) 
        return temp*temp; 
    else
        return number*temp*temp; 
} 

int main()
{
    char main_string[1000];
    fgets(main_string,1000,stdin);
    int main_base;
    scanf("%d",&main_base);
    int main_int=0,main_base_converted=0,length;
    for (length=0;main_string[length]!='\0';++length);
    length=length-2;
    for(int i=0;main_string[i]!='\0';i++)
    {
        if(main_string[i]=='0')
        {
            main_int=main_int*10;
            main_base_converted=main_base_converted+(0*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='1')
        {
            main_int=(main_int*10)+1;
            main_base_converted=main_base_converted+(1*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='2')
        {
            main_int=(main_int*10)+2;
            main_base_converted=main_base_converted+(2*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='3')
        {
            main_int=(main_int*10)+3;
            main_base_converted=main_base_converted+(3*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='4')
        {
            main_int=(main_int*10)+4;
            main_base_converted=main_base_converted+(4*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='5')
        {
            main_int=(main_int*10)+5;
            main_base_converted=main_base_converted+(5*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='6')
        {
            main_int=(main_int*10)+6;
            main_base_converted=main_base_converted+(6*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='7')
        {
            main_int=(main_int*10)+7;
            main_base_converted=main_base_converted+(7*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='8')
        {
            main_int=(main_int*10)+8;
            main_base_converted=main_base_converted+(8*powerof(main_base,length));
            length--;
        }
        else if(main_string[i]=='9')
        {
            main_int=(main_int*10)+9;
            main_base_converted=main_base_converted+(9*powerof(main_base,length));
            length--;
        }
    }
    printf("%d",main_base_converted);
}