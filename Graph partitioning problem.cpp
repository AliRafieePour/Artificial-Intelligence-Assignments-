#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("C:\\Users\\A\\untitled\\test1.txt");
int mark[200];
long long majmoo[10];
vector<int> adj[100];
long weight[200];
int v;
int least=660860; //okay
int num;
int last=667501; // okay

bool check(){
    for(int i=1;i<=num;i++)
        if((majmoo[i]<least)||(majmoo[i]>last))
            return false;
    return true;
}

void solve(int str,int vertex){
    if(str>num){
        if(check()){
            for(int i=1;i<=v;i++)
                cout<<i<<":"<<mark[i]<<endl;
            for(int j=1;j<=num;j++)
                cout<<majmoo[j]<<endl;
        }
        return;
    }
    if((majmoo[str]<least)&&(majmoo[str]+weight[vertex]<=last)){

        majmoo[str]+=weight[vertex];
        mark[vertex]=str;
        bool ended=true;
        for(int i=1;i<=v;i++)
            if(!mark[i]){
                ended=false;
                break;
            }
        if(ended){
            //    cerr<<majmoo[1]<<' '<<majmoo[2]<<endl;
            if(check()){
                for(int i=1;i<=v;i++)
                    cout<<i<<":"<<mark[i]<<endl;
                for(int j=1;j<=num;j++)
                    cout<<majmoo[j]<<endl;
            }
            majmoo[str]-=weight[vertex];
            mark[vertex]=0;
            return;
        }
        for(int i=0;i<adj[vertex].size();i++)
            if(!mark[adj[vertex][i]]){
                //   cerr<<"type1 from "<<vertex<<endl;
                solve(str,adj[vertex][i]);
            }
        majmoo[str]-=weight[vertex];
        mark[vertex]=0;
        return;
    }
    if((majmoo[str]>=least)&&(majmoo[str]+weight[vertex]<=last)){

        majmoo[str]+=weight[vertex];
        mark[vertex]=str;
        bool ended=true;
        for(int i=1;i<=v;i++)
            if(!mark[i]){
                ended=false;
                break;
            }
        if(ended){
            //  cerr<<majmoo[1]<<' '<<majmoo[2]<<endl;
            if(check()){
                for(int i=1;i<=v;i++)
                    cout<<mark[i]<<endl;
                for(int j=1;j<=num;j++)
                    cout<<majmoo[j]<<endl;
            }
            majmoo[str]-=weight[vertex];
            mark[vertex]=0;
            return;
        }
        for(int i=0;i<adj[vertex].size();i++)
            if(!mark[adj[vertex][i]]){
                // cerr<<"type2 from "<<vertex<<endl;
                solve(str,adj[vertex][i]);
                //cerr<<"type2 from "<<vertex<<endl;
                solve(str+1,adj[vertex][i]);
            }
        majmoo[str]-=weight[vertex];
        mark[vertex]=0;
        return;
    }
    if((majmoo[str]>=least)&&(majmoo[str]+weight[vertex]>last)){
        //cerr<<"type3"<<endl;
        solve(str+1,vertex);
    }
    // cerr<<"hi"<<endl;*/
    return;
}
void read(){
    fin>>v>>num;
    for(int i=1;i<=v;i++){
        int x;
        fin>>x;
        for(int j=1;j<=x;j++){
            int q;
            fin>>q;
            adj[i].push_back(q);
        }
    }
    long long u=0;
    for(int i=1;i<=v;i++){
        fin>>weight[i];
        u+=weight[i];
    }
    // cerr<<u<<endl;
    return;
}

int main(){
    read();
    for(int i=1;i<=v;i++){
        cout<<i<<endl;
        solve(1,i);
    }
    return 0;
}