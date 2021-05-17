#include <stdio.h>
#include <math.h>
double a[1000000]={0};
double b[1000000]={0};
double f1(double x, double y)
{
    return y*y*y -3*(x*x)*y;
}
double f2(double x, double y)
{
    return x*x*x -3*(y*y)*x;
}

double J11(double x, double y)
{
    return -6*x*y;
}
double J12(double x, double y)
{
    return 3*y*y-3*x*x;
}
double J21(double x, double y)
{
    return -6*x*y;
}
double J22(double x, double y)
{
    return 3*x*x-3*y*y;
}
 
int ucalc(double x, double y, double *ux, double *uy)
{
  double det;
 
  det = J11(x, y) * J22(x, y) - J12(x, y) * J21(x, y);
  *ux = -1 / det * (J22(x, y) * f1(x, y) - J12(x, y) * f2(x, y));
  *uy =  1 / det * (J21(x, y) * f1(x, y) - J11(x, y) * f2(x, y));
  return 0;
}
 
int newton2(double *x, double *y, double eps)
{
  int n=0;
  double x0, y0, ux, uy, err;
 
  /*printf("# n, x, y, err\n");
  printf("%4d, % .15e, % .15e\n", n, *x, *y);*/
  do {
    n++;
    x0 = *x;
    y0 = *y;
    ucalc(*x, *y, &ux, &uy);
    *x += ux;
    *y += uy;
    err = hypot(*x - x0, *y - y0);
    //printf("%4d, % .15e, % .15e, % .15e\n", n, *x, *y, err);
  }while (err >= eps);
  return 0;
}
int main(void)
{
    double x,y,x0=-1, y0=-1, eps = 1e-10;
    int cnt = 0;
    //char s[128];
    for(int i=1; i<=1000; i++){
        for(int j=1; j<=1000; j++){
            /*fprintf(stderr, "# x0 y0 = "); fgets(s, 128, stdin); sscanf(s, "%lf%lf", &x, &y);*/
            x = x0 + 0.002*i;
            y = y0 + 0.002*j;
        
            //printf("(%f,%f)\n", x, y);
            newton2(&x, &y, eps);
            a[cnt] = x;
            b[cnt] = y;
            //z[cnt] = y;
            //printf("[% .15e % .15e]\n", x, y);
            cnt++;
        }
    }
    
    FILE *gp;
    gp = popen("gnuplot -persist", "w");
    fprintf(gp, "set multiplot\n");
    fprintf(gp, "set xrange [-0.000000001:0.000000001]\n");
    fprintf(gp, "set yrange [-0.000000001:0.000000001]\n");
    fprintf(gp, "set xlabel \"x1\"\n");
    fprintf(gp, "set ylabel \"x2\"\n");

    // 曲線のプロット
    fprintf(gp, "plot '-' with points pointtype 1\n");
    for (int i=0; i<1000000; ++i) {
        fprintf(gp, "%f\t%f\n", a[i], b[i]);
    }
    fprintf(gp, "e\n");
    return 0;
}
