#pragma once
#include <Model.h>
#include <queue>

bool validCell( Map & map,  std::vector<int> & cell)
{
    return (cell[0] >= 0 && cell[0] < map.GetHeight() && cell[1] >= 0 && cell[1] < map.GetWidth());
}


void search( Map & map,  Planner & planner, std::vector<std::vector<int>> & distance, std::vector<std::vector<bool>> & explored)
{
    using cell = std::vector<int>;
    
    std::queue<cell> q;
    auto start = planner.GetStart();
    // TODO: validate if cell is valid later
    q.push(start);
    explored[start[0]][start[1]] = true;
    distance[start[0]][start[1]] = 0;
    while (!q.empty())
    {
        
        auto current = q.front();
        q.pop();
        if ( current == planner.GetGoal())
        {
            return;
        }
        // {{-1,0},{0,-1},{1,0},{0,1}}; 
        for ( auto movement : planner.GetMovements())
        {
            auto next = current;
            next[0] += movement[0];
            next[1] += movement[1];
            if ( validCell(map,next) && !explored[next[0]][next[1]] && map[next[0]][next[1]] == 0) 
            {
                q.push(next);
                explored[next[0]][next[1]] = true;
                distance[next[0]][next[1]] = distance[current[0]][current[1]] + 1;
            }
        }
    
    }
}