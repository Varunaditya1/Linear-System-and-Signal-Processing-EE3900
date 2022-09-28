#include<stdio.h>
#include<stdlib.h>
double x(int n)
{
    if((n>=0)&&(n<=3)){
        return n+1;
    }
    else if(n==4)
    {
        return 2;
    }
    else if(n==5)
    {
        return 1;
    }
    else return 0;
}
double y(int n)
{
    if(n<0)
        return 0;
    else    return x(n)+x(n-2)-0.5*(y(n-1));
}
int main() {
FILE* f1;
f1= fopen("wa.dat","w");
for(int i=0;i<20;i++)
{
    fprintf(f1,"%f\n",y(i));
}
fclose(f1);
    return 0;
}