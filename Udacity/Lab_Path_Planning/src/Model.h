#pragma once
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include "Model.h"


struct RobotData

{
    RobotData(int w, int h)
    {
        explored = std::vector<std::vector<bool>>(w,std::vector<bool>(h,false));
        distance = std::vector<std::vector<int>>(w,std::vector<int>(h,-1));
        iterations = std::vector<std::vector<int>>(w,std::vector<int>(h,-1));
        movements = std::vector<std::vector<std::string>>(w,std::vector<std::string>(h,""));
    }
    
};
class Map 
{
    using rectangular_grid = std::vector<std::vector<uint>>; 

public:
    Map(uint width, uint height, rectangular_grid g)
        : mapWidth{width}, mapHeight{height}, grid{std::move(g)} {}

    rectangular_grid& GetGrid()
    {
        return grid;
    }

    uint GetWidth() const
    {
        return mapWidth;
    }

    uint GetHeight() const
    {
        return mapHeight;
    }

    // Modified operator[]
    std::vector<uint>& operator[](int i)
    {
        return grid[i];
    }

    // Optional: Const version of operator[]
    const std::vector<uint>& operator[](int i) const
    {
        return grid[i];
    }

private:
    uint mapWidth;
    uint mapHeight;
    rectangular_grid grid; 
};


class Planner
{
public:
    Planner( std::vector<int> s, std::vector<int> g, int c ): start{s}, goal{g}, cost{c}{};

// small class i don't think setter and getters are necessary for now ;
    
    int cost;
    std::vector<std::vector<int>> GetMovements()
    {
        return movements;
    }
    std::vector<int> GetStart()
    {
        return start;
    }
    std::vector<int> GetGoal()
    {
        return goal;
    }
    std::string movements_arrows {{'^'},{'<'},{'v'},{'>'}};
private:
    std::vector<std::vector<int>> movements  {{-1,0},{0,-1},{1,0},{0,1}}; 
    std::vector<int> start;
    std::vector<int> goal;
};

