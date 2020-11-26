#ifndef the_third_H_
#define the_third_H_
int Soch(int k, int n)
{
	double C = fact(n) / double(fact(k) * fact(n - k));

	return(C);
}
#endif