#include <string>
#include <vector>
#include <map>
#include <iostream>

using std::string;
using std::vector;

class Solution {
    public:
        int romanToInt(const string &s) 
        {
            int current, old, total = 0;
            for(int i=s.length()-1; i>=0; i--)
            {
                switch(s[i]) {
                case 'I': current = 1; break;
                case 'V': current = 5; break;
                case 'X': current = 10; break;
                case 'L': current = 50; break;
                case 'C': current = 100; break;
                case 'D': current = 500; break;
                case 'M': current = 1000; break;
                }
                if(current<old){
                    total-=current;
                }
                else{
                    total+=current;
                }
                old = current;
            }
            return total;
        }
};

int main(){

    string roman = "III";
    // std::cout<<"Roman\t:\t";
    // std::cin>>roman;

    Solution mySolution;
    int output = mySolution.romanToInt(roman);
    std::cout<<"\n"<<output<<"\n";
}