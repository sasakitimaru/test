#include<iostream>
#include<cstdio>
#include<cmath>
#include<utility>
#include<vector>
#include<chrono>
#include<thread>
#include<cstdlib>
#include<random>
#include<algorithm>
#include<stdio.h>
void swap(int *a,int *b){
  int tmp;
  tmp = *a;
  *a = *b;
  *b = tmp;
}
void downheap(int a[], int n){
  int i=0,j=1;
  while(j<n){
    if(j+1<n && a[j]>a[j+1]) j++;
    if(a[i]>a[j]) swap(&a[i], &a[j]);
    i=j;
    j=2*i+1;
  }
}
int main(){
  std::vector<int> a{ 15, 31, 7, 24, 5, 19, 46 ,2, 10, 29};
  downheap(a,10);
  for(int i=0; i<10; i++){
    std::cout<<a[i];
  }
  return 0;
}
