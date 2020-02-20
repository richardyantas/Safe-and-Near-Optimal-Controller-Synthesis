#pragma once

#include<ibex.h>
#include<iostream>
#include<vector>
using namespace std;
using namespace ibex;

// Data type for sampled switched systems
typedef struct {
  double period;
  std::vector< Function > dynamics;
  std::vector<IntervalVector> states;
  int nb_dynamics;

} sampledSwitchedSystem;

typedef struct {
  IntervalVector *Yinit;
  Affine2Vector *Ycurrent;
  std::vector<int> pattern;  
} node;

// Post operator
IntervalVector post(sampledSwitchedSystem& sys, const IntervalVector W,
		    const std::vector<int> pattern) {

  Affine2Vector y0 = Affine2Vector(W);
  std::vector<int>::const_iterator it = pattern.begin();
  for (; it != pattern.end(); it++) {
    ivp_ode mode = ivp_ode( (sys.dynamics[*it]), 0.0, y0);
    simulation simu = simulation(&mode, sys.period, HEUN, 1e-5);
    simu.run_simulation();
    y0=*(simu.list_solution_j.back().box_jnh_aff);
  }
  //sys.states.push_back( y0.itv() );
  return y0.itv();
}



bool nextPattern(const sampledSwitchedSystem& sys, std::vector<int>& pattern) {
  int numModes = sys.dynamics.size();

  for (int i = pattern.size() - 1; i >= 0; i-- )
  {
    pattern[i] += 1 ;
    if ( pattern[i] > (numModes-1) ) // 5 -> it depends of number of modes.
    { 
      pattern[i] = 0 ;
      continue ;
    } 
    return true ;
  }
  return false;
}




bool constraint(const sampledSwitchedSystem& sys, const IntervalVector W, const IntervalVector B,
		const IntervalVector S, const std::vector<int> pattern) {

  Affine2Vector y1 = Affine2Vector(W);
  std::vector<int>::const_iterator it = pattern.begin();
  for (; it != pattern.end(); it++) {
    ivp_ode mode = ivp_ode((sys.dynamics[*it]), 0.0, y1);
    simulation simu = simulation(&mode, sys.period, HEUN, 1e-5);
    simu.run_simulation();
    if (simu.has_crossed(B) ) {
      return false;
    }
    if (!simu.stayed_in(S)) {
      return false;
    }
  }
  return true;
}


bool isforbidden(const vector<int>& pattern)
{ 
  for(int i=0;i<pattern.size()-1;i++)
  {
    if( 
      (pattern[i] == 4) && (pattern[i+1] == 6 ) ||
      (pattern[i] == 0) && (pattern[i+1] == 2 ) ||
      (pattern[i] == 5) && (pattern[i+1] == 7 ) ||
      (pattern[i] == 1) && (pattern[i+1] == 3 ) ||
      (pattern[i] == 4) && (pattern[i+1] == 7 ) ||
      (pattern[i] == 5) && (pattern[i+1] == 6 ) ||
      (pattern[i] == 1) && (pattern[i+1] == 2 ) ||
      (pattern[i] == 0) && (pattern[i+1] == 3 ) 
    )
    return true;
  }

  return false;
}





//find a pattern with new algo 
bool findPattern2 (const sampledSwitchedSystem& sys, const IntervalVector W,
		  const IntervalVector R, const IntervalVector B,
		  const IntervalVector S, unsigned int k,
		  std::list<std::vector<int> >& res_pattern_list) {

  node node_init;
  node_init.Yinit = new IntervalVector(W);
  node_init.Ycurrent = new Affine2Vector(W,true);
  node_init.pattern = vector<int>();
  
  list<node> list_node;
  list<pair <IntervalVector,vector<int> > > list_sol;
  
  list_node.push_back(node_init);
  
  //int nb_pattern = NB_M;
  int nb_pattern = sys.nb_dynamics;
  bool res = false;
  //bool res_temp = false;
  
  while(!list_node.empty())
  {    
    //std::cout << "size of list : " << list_node.size() << std::endl;    
    node node_current = list_node.front();
    list_node.pop_front();     
    for (int i=0; i < nb_pattern && node_current.pattern.size() < k; i++)
    {   
      if( node_current.pattern.size() > 0 )
      {
        int l = node_current.pattern.back();
        if( (l == 4  && i == 6) || //
          (l == 0  && i == 2) || //
          (l == 5  && i == 7) || //
          (l == 1  && i == 3) || //
          (l == 4  && i == 7) || //
          (l == 5  && i == 6) || //
          (l == 1  && i == 2) || //          
          (l == 0  && i == 3)    //
        )
        {
          std::cout << "forbidden pattern" << node_current.pattern << " + " << i << std::endl;
          continue;
        } 
      }
      

      //res_temp = false;
      if (node_current.pattern.empty())
	      std::cout << "current pattern : " << i << std::endl;
      else
      	std::cout << "current pattern : " << node_current.pattern << " + " << i << std::endl;
                  
      //ivp_ode mode = ivp_ode(*(sys.dynamics[i]), 0.0, *node_current.Ycurrent);
      ivp_ode mode = ivp_ode( (sys.dynamics[i]), 0.0, *node_current.Ycurrent);
      simulation simu = simulation(&mode, sys.period, HEUN, 1e-5);
      simu.run_simulation();
      
      
      bool fin_R = simu.finished_in(R);
      bool stay_S = simu.stayed_in(S);
      bool cross_B = simu.has_crossed(B);
      bool out_S = simu.go_out(S);
      bool fin_B = simu.finished_in(B);
      
      if (fin_R && stay_S)// && !cross_B)
      {       
        std::cout << "sol found !" << std::endl;
        node_current.pattern.push_back(i);        
        res_pattern_list.push_back(node_current.pattern);        
        res = true;
        //res_temp = true;                          
      }
      else
      {
        if (out_S)// || fin_B) //not only the last may be in obstacles...
        {
          std::cout << "Wrong direction !" << std::endl;
          //nop
        }
        else
        {
          
          if (stay_S)// && !cross_B)
          {
      //std::cout << "plop !" << std::endl;
            if (node_current.pattern.size() < k)
            {
              // In this part add  the filter
              std::cout << "Increment of pattern !" << std::endl;	      
              node new_node;
              new_node.Yinit = new IntervalVector(*node_current.Yinit);
              new_node.Ycurrent = new Affine2Vector(simu.get_last());              
              std::vector<int> new_pattern (node_current.pattern);
              new_pattern.push_back(i);
              new_node.pattern = new_pattern;
              list_node.push_back(new_node);	                                             
            }
          }
        }
      }
    }
    
  }
  return res;
}




// Search for a pattern of maximal length k which can prove the
// invariance
bool findPattern (sampledSwitchedSystem& sys, const IntervalVector W,
		  const IntervalVector R, const IntervalVector B,
		  const IntervalVector S, unsigned int k,
		  std::vector<int>&  res_pattern) {

  std::cerr << "\tINIT = " << W << std::endl;
  for (unsigned int i = 1; i <= k; i++) {
    std::vector<int> pattern(i, 0);

    do {  
      while( isforbidden(pattern))
      {
        nextPattern(sys, pattern);
      }      
      std::vector<int>::const_iterator it = pattern.begin();
      std::cerr << "\tPATTERN = (";
      for (; it != pattern.end(); it++)
      {
        std::cerr << *it << " " ;
      }
      std::cerr << ")" << std::endl;      
      IntervalVector res = post(sys, W, pattern);
      std::cerr << "Post(" << W << ") = " << res << " AND R = " << R << std::endl;
      if (res.is_subset(R) && constraint(sys,W,B,S,pattern)) {
          std::cerr << "\tPATTERN FOUND !!!" << std::endl;
          res_pattern = pattern;
          return true;
      }
    } while (nextPattern(sys,pattern));            
  }
  return false;
}






// The main algorithm of minimator
bool decompose (sampledSwitchedSystem& sys, const IntervalVector W,
		const IntervalVector R, const IntervalVector B,
		const IntervalVector S, unsigned int k, unsigned int d,
		vector< pair<IntervalVector,  list < vector<int> > > > & result) {

  list<vector<int>> res_pattern_list;

  // q is a queue of sub-state-space to explore to prove the invariance
  queue<IntervalVector> q;
  q.push (W);
  unsigned int nbStep = d;

  //  Parallelization

  /*
    pthread_t threads[6];
    struct thread_Data td[5];
    int rc:
    int i = d - nbStep;
  */


  //

  while (!q.empty() && nbStep > 0) {
    IntervalVector current = q.front ();
    q.pop();

    cout << "CURRENT: " << current << endl;

    bool flag = findPattern2 (sys, current, R, B, S, k, res_pattern_list);
    
    
    if (flag) {
      // Validated result, we keep it in the vector of results
      result.push_back ( pair< IntervalVector, list< vector<int> > > (current, res_pattern_list));
    }
    else {
          //if (current.diam().max() > 0.5)
          //{
      LargestFirst bbb(0.1,0.5);
      pair<IntervalVector,IntervalVector> p = bbb.bisect(current);
      q.push (p.first);
      q.push (p.second);
      nbStep--;
          //}
    }
  }

  if (nbStep <= 0) {
    return false;
  }
  else {
    return true;
  }
}


