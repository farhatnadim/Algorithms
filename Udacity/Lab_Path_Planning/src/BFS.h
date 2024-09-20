#pragma once
#include <Model.h>
#include <queue>

void search(const Map & map, const Planner & planner)
{
    using cell = vector<int>;
    std::vector<std::vector<bool>> explored(map.GetHeight(), std::vector<bool>(map.GetWidth(), false));
    std::vector<std::vector<int>> distance(map.GetHeight(), std::vector<int>(map.GetWidth(), -1));
    
    std::queue<cell> q;
    auto start = planner.GetStart();
    q.enqueue(start);
    while (!q.empty())
    {{
        auto current = q.front();
        q.pop();
        if ( current == planner.GetGoal())
        {
            return;
        }
    }}
}