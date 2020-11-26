#ifndef the_second_H_
#define the_second_H_
#include <cmath>

double Tailor(double x, int k) 
{	                                              

	double tsum = 0;
	double ksum = 0;
	for (int i = 0; i < k; i++)
	{
		ksum = pow((-1), i)*pow(x, 2*i+1) / double (fact(2*i+1));
		tsum += ksum;
	}

	return tsum;
}
#endif