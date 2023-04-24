#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
#include <set>

using namespace std;

map<char, vector<string>> prod_rules;
map<char, vector<char>> first_ans;
map<char, set<char>> follow_ans;
set<char> done;

void findfollow(char nt)
{
    // cout<<"\nnt : "<<nt<<endl;
    if (done.find(nt) != done.end())
        return;
    for (auto i = prod_rules.begin(); i != prod_rules.end(); i++)
    {
        char fnt = i->first;
        // cout<<"fnt : "<<fnt<<endl;
        vector<string> rules = i->second;

        for (int j = 0; j < rules.size(); j++)
        {
            string rule = rules[j];
            // cout<<"rule : "<<rule<<endl;
            int flag = 0;
            int k;
            for (k = 0; k < rule.length(); k++)
            {
                // cout<<rule[k]<<",";
                if (rule[k] == nt)
                    flag = 1;
                else if (flag == 1)
                {
                    if (!isupper(rule[k]))
                    {
                        follow_ans[nt].insert(rule[k]);
                        flag = 0;
                    }
                    vector<char> first = first_ans[rule[k]];
                    int flag2 = 0;
                    for (int p = 0; p < first.size(); p++)
                    {
                        if (first[p] != '#')
                            follow_ans[nt].insert(first[p]);
                        else
                            flag2 = 1;
                    }
                    if (flag2 == 0)
                        flag = 0;
                }
            }
            // cout<<endl;
            if (k == rule.length() && flag == 1 && fnt != nt)
            {

                if (done.find(fnt) == done.end())
                    findfollow(fnt);
                set<char> follow = follow_ans[fnt];
                for (auto p : follow)
                    follow_ans[nt].insert(p);
            }
        }
    }
    done.insert(nt);
}

int main()
{
    prod_rules['E'].push_back("TR");
    prod_rules['R'].push_back("+TR");
    prod_rules['R'].push_back("#");
    prod_rules['T'].push_back("FY");
    prod_rules['Y'].push_back("*FY");
    prod_rules['Y'].push_back("#");
    prod_rules['F'].push_back("(E)");
    prod_rules['F'].push_back("i");

    first_ans['E'].push_back('(');
    first_ans['E'].push_back('i');
    first_ans['R'].push_back('+');
    first_ans['R'].push_back('#');
    first_ans['T'].push_back('(');
    first_ans['T'].push_back('i');
    first_ans['Y'].push_back('#');
    first_ans['Y'].push_back('*');
    first_ans['F'].push_back('(');
    first_ans['F'].push_back('i');

    follow_ans['E'].insert('$');

    for (auto i : prod_rules)
        findfollow(i.first);

    cout << "\n\n** Follow of Non terminals **\n\n"
         << endl;
    for (auto i : follow_ans)
    {
        cout << i.first << "->";
        for (auto j : i.second)
        {
            cout << j << ',';
        }
        cout << endl;
    }

    return 0;
}