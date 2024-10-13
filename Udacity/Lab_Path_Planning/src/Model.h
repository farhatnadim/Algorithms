#pragma once

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <utility>  // for std::move and std::pair

struct RobotData
{
    RobotData(int w, int h)
    {
        explored   = std::vector<std::vector<bool>>(w, std::vector<bool>(h, false));
        distance   = std::vector<std::vector<int>>(w, std::vector<int>(h, -1));
        iterations = std::vector<std::vector<int>>(w, std::vector<int>(h, -1));
        policy     = std::vector<std::vector<std::string>>(w, std::vector<std::string>(h, "-"));
        parents    = std::vector<std::vector<std::vector<int>>>(w, std::vector<std::vector<int>>(h, std::vector<int>{0, 0}));
    }

    std::vector<std::vector<bool>> explored;
    std::vector<std::vector<int>> distance;
    std::vector<std::vector<int>> iterations;
    std::vector<std::vector<std::string>> policy;
    std::vector<std::vector<std::vector<int>>> parents;
};

class Map 
{
    using rectangular_grid = std::vector<std::vector<std::uint32_t>>; 

public:
    Map(std::uint32_t width, std::uint32_t height, rectangular_grid g)
        : mapWidth{width}, mapHeight{height}, grid{std::move(g)} {}

    rectangular_grid& GetGrid()
    {
        return grid;
    }

    std::uint32_t GetWidth() const
    {
        return mapWidth;
    }

    std::uint32_t GetHeight() const
    {
        return mapHeight;
    }

    std::vector<std::uint32_t>& operator[](int i)
    {
        return grid[i];
    }

    const std::vector<std::uint32_t>& operator[](int i) const
    {
        return grid[i];
    }

private:
    std::uint32_t mapWidth;
    std::uint32_t mapHeight;
    rectangular_grid grid; 
};

class Planner
{
public:
    Planner(std::vector<int> s, std::vector<int> g, int c)
        : start{std::move(s)}, goal{std::move(g)}, cost{c}, map_arrow_to_move{} 
    {
        movements_arrows = {"^", "<", "v", ">"};
        movements = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        
        for (size_t i = 0; i < movements_arrows.size(); ++i) 
        {
            map_arrow_to_move[movements[i]] = movements_arrows[i];
        }
    }

    int cost;
    
    std::vector<std::vector<int>> GetMovements()
    {
        return movements;
    }

    std::vector<int> GetStart() const
    {
        return start;
    }

    std::vector<int> GetGoal() const
    {
        return goal;
    }

    std::map<std::vector<int>,std::string > GetMap() 
    {
        return map_arrow_to_move;
    }

private:
    std::vector<std::string> movements_arrows;
    std::vector<std::vector<int>> movements;
    std::map<std::vector<int>,std::string > map_arrow_to_move;
    std::vector<int> start;
    std::vector<int> goal;
};
