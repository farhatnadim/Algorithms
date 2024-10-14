## Objectives
We have a 2D map of a robot and we are asked to find the shortest path between a start cell and an end cell.
First we implemented a search based on BFS 
Second we are planning to implement a search based on A* 



## Functions

### searchBFS
location : plan.h 
#### Description:
* Performs BFS  to map the distances between the start cell and other cells 
* Stores how many iterations until we reach a certain node 
* Stores Parents of the current Cell for path retrieval 

### searchA*
location : plan.h
#### Description :
* Performs a sorted type of BFS where the node  with the smallest distance value is expanded first
* The distance values are computed using index distance but also Heuristic distance 
* in this case we are using the manhatan distance $d = |{x_d}|  + |{y_d}|$
* and ${x_d}$ abd ${y_d}$ are computed as   
  ${x_d} = {x_{goal}} - {x_{cellposition}}$   
  ${y_d} = {y_{goal}} - {y_{cellposition}}$

 

### getPath
location : plan.h
#### Description 
* return the path between two cells by iterating over the Parents 2D grids 
* in case of BFS that's the shortest Path

### pathDifferential
location : plan.h
#### Description  
takes the shortest path and performs forward difference between the consequent cell elements to create a path differential

### setPolicy
location : plan.h
#### Description
* compute movements from getPath by substracting next cell from the previous cell , except for first and last cells . 
* maps the movements to the string movements 
* inserts the string movements in to the policy 2D grid.
* returns a 2D grid that contains the movememnts of the robot ">" ,"^", "<", "v"




*** GetPolicy
**** Description: 
The function visualize movements takes the coordinate from the list of shortest path found by shorted_path function and assigns the arrow directions in 2D map.

**** Specification
function name : visualize_movements
paremters : 3D vector representing shorted_path, 2D map initialized with '-'
calls: print2dVector 
output non 
