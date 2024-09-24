#pragma once
#include <Model.h>
#include <queue>

bool validCell( Map & map,  std::vector<int> & cell)
{
    return (cell[0] >= 0 && cell[0] < map.GetHeight() && cell[1] >= 0 && cell[1] < map.GetWidth());
}


void search( Map & map,  Planner & planner, RobotData & data)
{
    using cell = std::vector<int>;
    int count {0};
    std::queue<cell> q;
    auto start = planner.GetStart();
    // TODO: validate if cell is valid later
    q.push(start);
    data.explored[start[0]][start[1]] = true;
    data.distance[start[0]][start[1]] = 0;
    data.iterations[start[0]][start[1]] = 0;
    while (!q.empty())
    {
        
        auto current = q.front();
        q.pop();
        data.iterations[current[0]][current[1]] = count;
        count++;
                
        
        if ( current == planner.GetGoal())
        {
            return;
        }

        auto movements = planner.GetMovements();
        // Switching to a indexed for loop to iterate over the movements
        for ( int i = 0; i < movements.size(); ++i) 
        {
            auto next = current;
            auto movement = movements[i];
            next[0] += movement[0];
            next[1] += movement[1];
            if ( validCell(map,next) && !data.explored[next[0]][next[1]] && map[next[0]][next[1]] == 0) 
            {
                q.push(next);
                data.explored[next[0]][next[1]] = true;
                data.distance[next[0]][next[1]] = data.distance[current[0]][current[1]] + 1;
                data.movements[next[0]][next[1]] = planner.movements_arrows[i];

            }
        }
    
    }
}