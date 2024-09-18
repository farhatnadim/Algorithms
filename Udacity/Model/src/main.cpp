#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
using rectangular_grid = vector<vector<uint>>; 
/* TODO: Define a Map class
   Inside the map class, define the mapWidth, mapHeight and grid as a 2D vector
*/
class Map 
{

public:
    Map (uint width, uint height, rectangular_grid g) : mapWidth{width}, mapHeight{height},grid{g}
    {
        // initialization fo the grid
        vector<uint> empty_row;
        //empty_row.assign(width,0);
        //grid.assign(height,empty_row);
    }

    // Assignment Constructor 


    rectangular_grid GetGrid()
    {
        return grid;
    }
private:
    uint mapWidth;
    uint mapHeight;
    rectangular_grid grid; 

}; // end of class Map


class Planner
{
public:
    Planner( vector<int> s, vector<int> g, int c ): start{s}, goal{g}, cost{c}
    {

    }

// small class i don't think setter and getters are necessary for now ;
    vector<int> start;
    vector<int> goal;
    int cost;
    vector<vector<int>> movements  {{-1,0},{0,-1},{1,0},{0,1}}; 
    string movements_arrows {{'^'},{'<'},{'V'},{'>'}};


};
/* TODO: Define a Planner class
   Inside the Planner class, define the start, goal, cost, movements, and movements_arrows
   Note: The goal should be defined it terms of the mapWidth and mapHeight
*/

/* TODO: Define a print2DVector function which will print 2D vectors of any data type
   Example
   
   Input: 
   vector<vector<int> > a{{ 1, 0 },{ 0, 1 }};
   print2DVector(a);
   vector<vector<string> > b{{ "a", "b" },{ "c", "d" }};
   print2DVector(b);
   
   Output:
   1 0
   0 1
   a b
   c d
   
*/
template <typename T>
void print2DVector(const T & grid)
{
    for (auto && row : grid)
    {
        for (auto && column : row )
        {
            cout << column << " ";
        }
        cout << "\n";
    }
}

/*############ Don't modify the main function############*/
int main()
{
    // Instantiate map and planner objects
    
    Planner planner({0,0},{4,5},1);
    rectangular_grid grid = 
        {{ 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 0, 0, 1, 1, 0 }};
    
    Map map{6,5,grid};
    // Print classes variables
    cout << "Map:" << endl;
    print2DVector(map.GetGrid());
    
    cout << "Start: " << planner.start[0] << " , " << planner.start[1] << endl;
    cout << "Goal: " << planner.goal[0] << " , " << planner.goal[1] << endl;
    cout << "Cost: " << planner.cost << endl;
    cout << "Robot Movements: " << planner.movements_arrows[0] << " , " << planner.movements_arrows[1] << " , " << planner.movements_arrows[2] << " , " << planner.movements_arrows[3] << endl;
    cout << "Delta:" << endl;
    print2DVector(planner.movements);
    
    return 0;
}
