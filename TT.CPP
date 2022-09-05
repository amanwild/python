#include<iostream>
using namespace std;
n1(int n){
    if (n<=0){
        printf(" iff  \n");
    return 0;
    }
    else{
        printf(" initialize \n");
        n1(n-1);
        printf(" p1 \n");
        printf("%d",n);
        printf(" p2 \n");
        n1(n-1);
    }
}



int main(){
    n1(3);
    return 0;
}