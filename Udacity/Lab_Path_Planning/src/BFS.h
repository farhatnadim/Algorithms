#pragma once
#include <Model.h>
#include <queue>

bool validCell(const Map & map, const std::vector<int> & cell)
{
    return (cell[0] >= 0 && cell[0] < map.GetHeight() && cell[1] >= 0 && cell[1] < map.GetWidth());
}
void search(const Map & map, const Planner & planner)
{
    using cell = vector<int>;
    std::vector<std::vector<bool>> explored(map.GetHeight(), std::vector<bool>(map.GetWidth(), false));
    std::vector<std::vector<int>> distance(map.GetHeight(), std::vector<int>(map.GetWidth(), -1));
    
    std::queue<cell> q;
    auto start = planner.GetStart();
    // TODO: validate if cell is valid later
    q.enqueue(start);
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
        for ( auto movement:planner.Getmovements())
        {
            auto new = current;
            new[0] += movement[0];
            new[1] += movement[1];
            if ( validCell(map,new) && !explored[new[0]][new[1]] && map[new[0]][new[1]] == 0) 
            {
                q.push(new);
                explored[new[0]][new[1]] = true;
                distance[new[0]][new[1]] = distance[current[0]][current[1]] + 1;
            }
        }
    
    }
}