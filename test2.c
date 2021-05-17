/*　逐次代入法で方程式　x=f(x)　の解を求める*/
#include<stdio.h>
#include<math.h>

/*方程式f(x)*/          
double f(double x)
{	
  return -(x*x)+4*x-2;
}
                          
/*大域変数の宣言*/      
double eps=0.00000001;/*収束判定条件*/
int max=50;/*計算回数の上限*/
                                          
int main(void)
{
	/*局所変数の宣言*/
	double x=0.5;/*xの初期値は0.5から*/
	double xnew;
	int i;
	/*逐次代入法の実行*/
	for(i=0;i<max;i++){ /*収束しなくてもmax回計算すると止まる*/
		printf("%2d回目  x=%9.7f\n",i,x);
		xnew=f(x);
		/*xnewとxの差の絶対値が小さく収束したら終了*/
		if(fabs(xnew-x)<eps)break;
		x=xnew;/*xnewを次のxにする*/
	}
	if(i>=max)printf("収束しませんでした！");
	return 0;
}
