import numpy as np



def is_in_zonotope(currentState, zon):
    #if currentState.T > 75:
    #    print( "T: ", currentState.T, " - V:", currentState.V , " T[]: " ,zon.item(0,0),"-",zon.item(0,1), " V[]: ", zon.item(1,0), "-", zon.item(1,1)  )
    if  zon.item(0,0) <= currentState.T and currentState.T <= zon.item(0,1):
        #if currentState.T > 75:
        #    print("FOUND")            
            return True
    else:
            return False


def query( X ):
    zon = np.matrix("[40, 40.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;1,4,1;0,0,1]');
    zon = np.matrix("[40.3125, 40.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;1,4,1;0,0,1]');
    zon = np.matrix("[40.625, 40.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;0,1,7;1,4,1;0,0,1]');
    zon = np.matrix("[40.9375, 41.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;0,1,7;1,4,1;0,0,1]');
    zon = np.matrix("[41.25, 41.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;0,1,7;1,4,1;0,0,1]');
    zon = np.matrix("[41.5625, 41.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,5,-1;0,1,-1;0,1,7;1,4,1;0,0,1]');
    zon = np.matrix("[41.875, 42.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[42.1875, 42.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[42.5, 42.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[42.8125, 43.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[43.125, 43.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[43.4375, 43.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[43.75, 44.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[44.0625, 44.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[44.375, 44.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[44.6875, 45] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[45, 45.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[45.3125, 45.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[45.625, 45.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[45.9375, 46.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[46.25, 46.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[46.5625, 46.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[46.875, 47.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[47.1875, 47.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[47.5, 47.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[47.8125, 48.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[48.125, 48.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,7;0,0,1]');
    zon = np.matrix("[48.4375, 48.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[48.75, 49.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[49.0625, 49.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[49.375, 49.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[49.6875, 50] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[50, 50.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[50.3125, 50.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[50.625, 50.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[50.9375, 51.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[51.25, 51.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[51.5625, 51.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5;0,0,1]');
    zon = np.matrix("[51.875, 52.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[1,-1,-1;1,4,-1;1,4,5;0,1,-1;0,1,5]');
    zon = np.matrix("[52.1875, 52.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,1,-1;0,1,4]');
    zon = np.matrix("[52.5, 52.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,1,-1;0,1,4]');
    zon = np.matrix("[52.8125, 53.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,1,-1;0,1,4]');
    zon = np.matrix("[53.125, 53.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[53.4375, 53.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[53.75, 54.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[54.0625, 54.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[54.375, 54.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[54.6875, 55] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[55, 55.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[55.3125, 55.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[55.625, 55.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[55.9375, 56.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[56.25, 56.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[56.5625, 56.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[56.875, 57.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[57.1875, 57.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[57.5, 57.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[57.8125, 58.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[58.125, 58.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[58.4375, 58.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[58.75, 59.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[59.0625, 59.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[59.375, 59.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[59.6875, 60] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[60, 60.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[60.3125, 60.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[60.625, 60.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[60.9375, 61.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[61.25, 61.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[61.5625, 61.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[61.875, 62.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[62.1875, 62.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[62.5, 62.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[62.8125, 63.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[63.125, 63.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[63.4375, 63.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[63.75, 64.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[64.0625, 64.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[64.375, 64.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[64.6875, 65] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[65, 65.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[65.3125, 65.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[65.625, 65.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[65.9375, 66.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[66.25, 66.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[66.5625, 66.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[66.875, 67.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[67.1875, 67.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[67.5, 67.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[67.8125, 68.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[68.125, 68.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[68.4375, 68.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[68.75, 69.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[69.0625, 69.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[69.375, 69.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[69.6875, 70] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[70, 70.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[70.3125, 70.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[70.625, 70.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[70.9375, 71.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[71.25, 71.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[71.5625, 71.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[71.875, 72.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[72.1875, 72.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[72.5, 72.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[72.8125, 73.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[73.125, 73.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[73.4375, 73.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[73.75, 74.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[74.0625, 74.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[74.375, 74.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[74.6875, 75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[75, 75.3125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1;0,4,5]');
    zon = np.matrix("[75.3125, 75.625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[75.625, 75.9375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[75.9375, 76.25] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[76.25, 76.5625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[76.5625, 76.875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[76.875, 77.1875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[77.1875, 77.5] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[77.5, 77.8125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[77.8125, 78.125] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[78.125, 78.4375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[78.4375, 78.75] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[78.75, 79.0625] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[79.0625, 79.375] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[79.375, 79.6875] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,-1,-1;0,4,-1]');
    zon = np.matrix("[79.6875, 80] ; [0.09, 0.61]"); 
    if is_in_zonotope(X,zon): 	 
        return np.matrix('[0,4,-1;2,4,-1;0,0,4;2,0,4;2,2,4;4,0,4;4,2,4]');

    return  np.matrix('[-1,-1,-1]')