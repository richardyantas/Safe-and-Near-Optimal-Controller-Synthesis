#include "ibex.h"

using namespace ibex;
using namespace std;

int main(){

  const int n = 2;
  Variable y(n);

  // State vector is a zonotope
  Affine2Vector state(n);
  state[0] = 0.0;
  state[1] = 0.0;

  double t = 0;
  const double sampling = 0.005;
  Affine2 integral(0.0);

  while (t < 3.0) {
    Affine2 goal(10.0);
    Affine2 error = goal - state[0];

    // Controleur PI discret
    integral = integral + sampling * error;
    Affine2 u = 1400.0 * error + 35.0 * integral;
    state[1] = u;

    // Dynamique d'une voiture avec incertitude sur sa masse
    Function ydot(y, Return((y[1] - 50.0 * y[0] - 0.4 * y[0] * y[0])
			    / Interval (990, 1010), Interval(0.0)));
    ivp_ode vdp = ivp_ode(ydot, 0.0, state);

    // Integration numerique ensembliste
    simulation simu = simulation(&vdp, sampling, RK4, 1e-6);
    simu.run_simulation();

    // Mise a jour du temps et des etats
    state = simu.get_last();
    t += sampling;

    cerr << state.itv() << endl;
  }

  return 0;
}