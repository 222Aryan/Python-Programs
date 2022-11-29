#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> num1;
    num1={4,1,2};
    vector<int> num;
    num={1,3,4,2};
    int l=num.size();
    cout<<l<<endl;
    vector<int> res;
    for(int i=0;i<l-1;++i){
        if(num[i]<num[i+1])
            res.push_back(num[i+1]);
        else
            res.push_back(-1);
    }
    res.push_back(-1);
    for(int i=0;i<l;++i)
        cout<<res[i]<<" ";
        cout<<endl;
    
    unordered_map<int,int>m;

    for(int i=0;i<num1.size();++i){
        m[num1[i]]++;
    }

    for()
}