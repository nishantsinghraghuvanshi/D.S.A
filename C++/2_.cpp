#include<iostream>
#include <algorithm>
using namespace std;

int splitter(){
    cout <<
}

int main(){
    string time_time,time_format;
    cout<<"Enter the time in (HH/MM/SS) : ";
    cin>>time_time;
    cout<<"AM or PM : ";
    cin>>time_format;
    transform(time_format.begin(), time_format.end(), time_format.begin(), ::toupper);
    cout<<time_format;
    splitter()
}