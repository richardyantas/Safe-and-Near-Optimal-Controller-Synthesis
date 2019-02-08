#include "ibex.h"
using namespace ibex;

#define __PREC__ 1e-11
#define __METH__ RK4
#define __DURATION__ 10.0

int main(){
  // Dimension of the IVP
  const int n= 2;

  // State variables
  Variable y(n);

  // Initial conditions
  IntervalVector yinit(n);
  yinit[0] = Interval(1.5,2.0);
  yinit[1] = Interval(-2.0,-1.5);

  // Derivative function
  Function ydot = Function (y,Return (y[0]-2*y[1],
             3*y[0]-4*y[1]));

  // Ivp contruction (initial time is 0.0)
  ivp_ode problem = ivp_ode (ydot, 0.0, yinit);

  // Simulation construction and run
  simulation simu = simulation (&problem, __DURATION__, __METH__, __PREC__);
  simu.run_simulation();

  return 0;
}