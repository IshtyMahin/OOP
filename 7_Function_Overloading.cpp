#include<bits/stdc++.h>
using namespace std;

class Calculator{
    public:
    int add(int a,int b){
        return a+b;
    }
    int add(int a,int b,int c){
        return a+b+c;
    }
    float add(float a,float b){
        return a+b;
    }
};
int main(){
    Calculator cal;
    cout<<cal.add(1,2)<<endl;
    cout<<cal.add(1,2,3)<<endl;
    cout<<cal.add(1.1f,2.2f)<<endl;
    return 0;
}