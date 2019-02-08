

// g++ -frounding-math -ffloat-store -I/usr/local/include -I/usr/local/include/ibex  -O3 -DNDEBUG -Wno-deprecated -frounding-math  -o main main.cpp -L/usr/local/lib -libex -lprim -lClp -lCoinUtils

// g++ -frounding-math -ffloat-store -I/usr/local/include/ibex  -o main main.cpp -libex -lprim -lClp -lCoinUtils

// g++  -I/usr/local/include/ibex  -o main main.cpp -libex -lprim

#include <ibex/ibex.h>
#include <vector>
#include <queue>
#include <iostream>
#include <sstream>

#include "../include/sss.h"
#include "../include/utils.h"

using namespace ibex;
using namespace sss;
