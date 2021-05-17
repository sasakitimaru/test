#include<stdio.h>
#include<stdlib.h>
unsigned char m[256], pc, reg;
int main(){
  unsigned char instr, n, add;
  m[0]=2;
  m[1]=10;
  m[2]=1;
  m[3]=6;
  m[4]=8;
  m[5]=8;
  m[6]=7;
  m[7]=2;
  m[8]=0;
  pc = 0;
  while(1){
    printf(" pc=%4d reg=%4d\n",pc,reg);
    instr = m[pc];
    pc = pc+1;
    switch (instr) {
      case 0: exit(0);
        break;
      case 1: printf("%d\n", reg);
        break;
      case 2: n = m[pc]; pc = pc+1;
        reg = n;
        break;
      case 3: add = m[pc]; pc = pc+1;
        reg = m[add];
        break;
      case 4:
        add = reg;  pc = pc+1;
        break;
      case 5:
        reg = reg+1; pc = pc+1;
        break;
      case 6:
        reg = reg-1; pc = pc+1;
        break;
      case 7:
        pc = m[pc]; pc = pc+1;
        break;
      case 8:
        if(reg==0){
          pc =m[pc];
          break;
        }
        pc = pc+1;
    }
  }
}
/*実行結果
pc=   0 reg=   0
 pc=   2 reg=  10
10
 pc=   3 reg=  10
 pc=   5 reg=   9
 pc=   7 reg=   9
 pc=   9 reg=   0
*/
