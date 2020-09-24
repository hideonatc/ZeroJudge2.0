#include<iostream>
using namespace std;
int main(){
	int c=int('*')-int('1');
	string s;
	while(cin>>s){
		for(int i=0;i<s.length();i++){
			cout<<char(int(s[i])+c);
		}
		cout<<endl;
	}
}