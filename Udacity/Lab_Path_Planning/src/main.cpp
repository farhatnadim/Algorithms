#include "main.h"
#include <iostream>
#include "BFS.h"
#include <iomanip>
using std::cout; using std::endl; using std::vector;




template <typename T>
void print2DVector(const T & grid)
{
    for (auto && row : grid)
    {
        for (auto && column : row )
        {
            cout << std::right << std::setw(2) << column << " ";
        }
        cout << "\n";
    }
}


int main()
{
    // Instantiate map and planner objects

    constexpr int width = 6;
    constexpr int height = 5;
    const vector<int> start = {0,0};
    const vector<int> goal = {4,5};
    const int cost = 1;
    Planner planner(start,goal,cost);
    std::vector<std::vector<uint>> grid = 
        {{ 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 0, 0, 1, 1, 0 }};
    
    Map map{width,height,grid};


    // Print classes variables
    
    cout << "Map:" << endl;
    print2DVector(map.GetGrid());
    cout << "Planner:" << endl;
    cout << "Start: " << planner.GetStart()[0] << " , " << planner.GetStart()[1] << endl;
    cout << "Goal: " << planner.GetGoal()[0] << " , " << planner.GetGoal()[1] << endl;
    cout << "Cost: " << planner.cost << endl;
    cout << "Movements: " << endl;
    print2DVector(planner.GetMovements());
    cout << "Movements arrows: " << planner.movements_arrows[0] << endl;
    // Search for the path
    RobotData data(height,width);

    search(map, planner, data);
    print2DVector(data.movements);
    print2DVector(data.distance);
  
    cout << endl;
    return 0;

}
