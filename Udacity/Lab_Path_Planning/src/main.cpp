#include "main.h"
#include <iostream>


using std::cout; using std::endl; using std::vector;
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
    cout << "Start: " << planner.start[0] << " , " << planner.start[1] << endl;
    cout << "Goal: " << planner.goal[0] << " , " << planner.goal[1] << endl;
    cout << "Cost: " << planner.cost << endl;
    cout << "Robot Movements: " << planner.movements_arrows[0] << " , " << planner.movements_arrows[1] << " , " << planner.movements_arrows[2] << " , " << planner.movements_arrows[3] << endl;
    cout << "Delta:" << endl;
    print2DVector(planner.movements);    
    return 0;

}
