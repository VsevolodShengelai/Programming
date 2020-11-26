#pragma once
int fact(int  n)
{
	int P = 1;
	for (int i = 1; i <= n; i++)
	{
		P = P * i;
	}
	return(P);
}