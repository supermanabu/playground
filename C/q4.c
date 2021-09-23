#include <stdio.h>
void f1 (void);
void f2 (void);

int main ()
{
	f1 ();
	f1 ();
	f1 ();
	f2 ();
	return 0;
}

void f1 (void)
{
	printf("For he's a jolly good fellow!\n");
}

void f2 (void)
{
	printf("Which nobody can deny!\n");
}
