#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;
using rectangular_grid =vector<vector<uint>>; 
/* TODO: Define a Map class
   Inside the map class, define the mapWidth, mapHeight and grid as a 2D vector
*/
class Map 
{
public:
    Map (uint width, uint height) : mapWidth{width}, mapHeight{height}
    {
        // initialization fo the grid
        vector<uint> empty_row;
        empty_row.assign(width,0);
        for ( auto i = 0 ; i < height ; i++)
        {
            grid.push_back(empty_row);
        }
    }
    rectangular_grid GetGrid()
    {
        return grid;
    }
private:
    uint mapWidth;
    uint mapHeight;
    rectangular_grid grid; 

}; // end of class Map

struct point {
    uint x;
    uint y;
};
class Planner
{
    private:
    vector<int> start;
    vector<int> goal;
    int cost;
    rectangular_grid movements; 
    rectangular_grid movements_arrows;

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
    Map map{6,5};
    //Planner planner;

    // Print classes variables
    cout << "Map:" << endl;
    print2DVector(map.GetGrid());
    /**
    cout << "Start: " << planner.start[0] << " , " << planner.start[1] << endl;
    cout << "Goal: " << planner.goal[0] << " , " << planner.goal[1] << endl;
    cout << "Cost: " << planner.cost << endl;
    cout << "Robot Movements: " << planner.movements_arrows[0] << " , " << planner.movements_arrows[1] << " , " << planner.movements_arrows[2] << " , " << planner.movements_arrows[3] << endl;
    cout << "Delta:" << endl;
    print2DVector(planner.movements);
    */
    return 0;
}
