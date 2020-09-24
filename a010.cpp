#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int input;
	cin>>input;
	int idx=2,m;
	bool fir=1;
	while(input>1){
		m=0;
		while(input%idx==0){
			input/=idx;
			m++;
		}
		if(m==0){
			idx++;
			continue;
		}
		else{
			if(fir)fir=0;
			else cout<<" * ";
			if(m==1)cout<<idx;
			else printf("%d^%d",idx,m);
		}
		idx++;
	}
	cout<<endl;
}