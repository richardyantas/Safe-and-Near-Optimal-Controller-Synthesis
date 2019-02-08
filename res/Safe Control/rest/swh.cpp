#include "ibex.h"
#include<vector>
#include<queue>
#include<iostream>
#include<sstream>

using namespace ibex;
using namespace std;

class sampledSwitchedSystem
{
	double period;
	vector<Function*> dynamics;
	int nb_dynamics;	
}