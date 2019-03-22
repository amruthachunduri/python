#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
  int amu,*b,n=0;
  scanf("%d",&amu);
  b=(int*)malloc(sizeof(int)*amu);
  for(int i=0;i<amu;i++)
  {
    scanf("%d",&b[i]);
  }  
  for(int i=0;i<(amu-2);i++)
  {
    for(int j=i+1;j<(amu-1);j++)
    {
      for(int k=j+1;k<amu;k++)
      {
        if(b[j]>b[i] && b[k]>b[j])
        {
        n++;
        }
      }
    }
  }
  printf("%d",n);
}
