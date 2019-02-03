#include "ibex.h"
#include <iostream>

using namespace std;
using namespace ibex;


int main(int argc, char** argv) {
	Interval x(0,1);
	Interval y=exp(x+1); //y is [1,7.389...]
	cout << y << endl;
}