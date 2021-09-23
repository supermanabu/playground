#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <functional>
#include <sstream>

int i,n,f,m,dt;
double tx,ty,dx,dy; 
const int mol=204;//链数 
const int sig=50;// 每条链所含粒子数 
const int begin=1000;//开始计算的帧数 
const int Frame=10000;//总帧数 
const int num=mol*sig;//总粒子数 
const double timestep=0.005;//步长 
const int dump=1000;//输出步长 
int id[Frame][num],type[Frame][num];
double xu[Frame][num],yu[Frame][num],cx[Frame][mol],cy[Frame][mol],msd[Frame],msdx[Frame],msdy[Frame];
static int count[Frame];
int main(void)
{
	using namespace std;
	FILE *fp;
	ifstream file1;
	file1.open("0.4chainN50n20u.lammpstrj",ios::in);
	for(f=0;f<Frame;f++)
	{
		using namespace std;
		string temp;
		for(i=0;i<9;i++)
		{
			getline(file1,temp);
		}
		for(n=0;n<num;n++)
		{
			getline(file1,temp);
			stringstream word(temp);
			word>>id[f][n]>>type[f][n]>>xu[f][n]>>yu[f][n];
		}
	}
	file1.close();
	fp=fopen("msd_0.4chainN50n20u.txt","w");
	for(f=begin;f<Frame;f++)//求质心 
	{
		for(m=0;m<mol;m++)
		{
			tx=0.0;
			ty=0.0;
			for(n=m*sig;n<(m+1)*sig;n++)
			{
				tx+=xu[f][n];
				ty+=yu[f][n];
			}
			cx[f][m]=tx/sig;
			cy[f][m]=ty/sig;
		}
	}
	for(f=0;f<Frame;f++)
	{
		msd[f]=0;
		count[f]=0;
		msdx[f]=0;
		msdy[f]=0;
	}
	for(f=begin;f<Frame;f++)//计算msd 
	{
		for(dt=1;f+dt<Frame;dt++)
		{
			for(m=0;m<mol;m++)
			{
				dx=(cx[f+dt][m]-cx[f][m])*(cx[f+dt][m]-cx[f][m]);
				dy=(cy[f+dt][m]-cy[f][m])*(cy[f+dt][m]-cy[f][m]);
				msdx[dt]+=dx;
				msdy[dt]+=dy;
				msd[dt]+=dx+dy;
				count[dt]++;
			}
		}
	}
	for(dt=1;dt<Frame-begin;dt++)
	{
		msdx[dt]/=count[dt];
		msdy[dt]/=count[dt];
		msd[dt]/=count[dt];
		fprintf(fp,"%f\t%f\t%f\t%f\n",dt*dump*timestep,msdx[dt],msdy[dt],msd[dt]);
	}
	fclose (fp);
	return 0;
}
