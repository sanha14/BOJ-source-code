// 셀프넘버
#include<stdio.h>
#include<string.h>
#include <stdlib.h>

int main()
{
	int number,non_self;
	int num_list[10001] = {0};
	number = 1;
	while(number<10)
	{
		non_self = number*2;
		num_list[non_self] = 1;
		number++;
	}
	while(number < 10001)
	{
		char s_num[6] = {'0','0','0','0','0','0'};
		int val = 0;
		sprintf(s_num, "%d", number);
		for(int i = 0; s_num[i] != '\0'; i++)
		{
			val += s_num[i] - '0';
		}
		non_self = number + val;
		if(non_self <= 10000)
		{
			num_list[non_self] = 1;
		}
		number++;
	}

	for(int i = 1; i<10001; i++)
	{
		if(num_list[i] == 0)
		{
			printf("%d\n",i);
		}
	}
	return (0);
}
