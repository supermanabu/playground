#include <stdio.h>

#define ORDER 11
long Fibonacci(int);

int main(void)
{
	int n;
	n = Fibonacci(ORDER);
	printf("%d\n", n);
	return 0;
}

long Fibonacci(int n)
{
	if (n > 2)
		return Fibonacci(n-1) + Fibonacci(n-2);
	else
		return 1;
}