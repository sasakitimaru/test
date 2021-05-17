#include<stdlib.h>
#include<stdio.h>
/*int max(int a[], int n){
  int ma = a[0];
  for(int i=0;i<n;i++){
    if(ma<a[i]) ma = *a[i];
  }
  return ma;
  }
int min(int a[], int n){
  int mi = a[0];
  for(int i=0;i<n;i++){
    if(mi>a[i]) mi = a[i];
  }
  return mi;
  }*/
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
void upheap(int a[], int n){
  int i=n-1,j;
  while (i>0) {
    j=(i-1)/2;
    if(a[j]>a[i]) swap(&a[i], &a[j]);
    i=j;
  }
}
/*void heap(int a[], int n){
  while(sizeof(a)>1){
    swap(min(a,sizeof(a)),a[n]);
    n--;
    return 0;
  }
  }*/
int main(void){
  int a[10] = { 15, 31, 7, 24, 5, 19, 46 ,2, 10, 29};
  downheap(a,10);
  for(int i=0; i<10; i++){
    printf("%d ",a[i]);
  }
  printf("\n");
  upheap(a,10);
  for(int i=0; i<10; i++){
    printf("%d ",a[i]);
  }
  printf("\n");
  /*heap(a,10);
  for(int i=0; i<10; i++){
    printf("%d ",a[i]);
  }
  printf("\n");*/
  return 0;
}
/*
7 31 15 24 5 19 46 2 10 29 
upheap実行
5 7 15 24 31 19 46 2 10 29 
*/
