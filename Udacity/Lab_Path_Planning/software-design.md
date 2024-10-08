## Objectives
We have a 2D map of a robot and we are asked to find the shortest path between a start cell and an end cell 




## Functions

### search
location : plan.h 
#### Description:
* Performs BFS  to map the distances between the start cell and other cells 
* Stores how many iterations until we reach a certain node 
* Stores Parents of the current Cell for path retrieval 
#### Specification 


### getPath
location : plan.h
#### Description 
* return the path between two cells by iterating over the Parents 2D grids 
* in case of BFS that's the shortest Path

### getPolicy
location : plan.h
#### Description
* compute movements from getPath by substracting next cell from the previous cell , except for first and last cells . 
* mapts the movements to the string movements 
* inserts the string movements in to the policy 2D grid.
* returns a 2D grid that contains the movememnts of the robot ">" ,"^", "<", "v"





: distance map of type vector<vector<int>>
output : a vector<vector<vector<int>>> 

*** GetPolicy
**** Description: 
The function visualize movements takes the coordinate from the list of shortest path found by shorted_path function and assigns the arrow directions in 2D map.

**** Specification
function name : visualize_movements
paremters : 3D vector representing shorted_path, 2D map initialized with '-'
calls: print2dVector 
output non 
