#include <stdio.h>

void main() 
{
    int number1,number2,number3,tot_time;
    scanf("%d\n%d\n%d\n%d",&number1,&number2,&number3,&tot_time);
    int tot_score=0;
    for(int i=0;i<tot_time;i++)
    {
        if(number1>=number2 && number1>=number3)
        {
            if(number1>=1)
            {
                tot_score+=number1;
                number1=number1-1;
            }
            else
            {
                tot_score+=number1;
            }
        }
        else if(number2>=number1 && number2>=number3)
        {
            if(number2>=1)
            {
                tot_score+=number2;
                number2=number2-1;
            }
            else
            {
                tot_score+=number2;
            }
        }
        else if(number3>=number1 && number3>=number2)
        {
            if(number3>=1)
            {
                tot_score+=number3;
                number3=number3-1;
            }
            else
            {
                tot_score+=number3;
            }
        }
    }
    printf("%d",tot_score);
}
