#pragma once
#include <string>
#include <vector>
#include <algorithm>


class Map 
{

    using rectangular_grid = std::vector<std::vector<uint>>; 

public:
    Map (uint width, uint height, rectangular_grid g) : mapWidth{width}, mapHeight{height},grid{g} {};

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
    Planner( std::vector<int> s, std::vector<int> g, int c ): start{s}, goal{g}, cost{c}{};

// small class i don't think setter and getters are necessary for now ;
    std::vector<int> start;
    std::vector<int> goal;
    int cost;
    std::vector<std::vector<int>> movements  {{-1,0},{0,-1},{1,0},{0,1}}; 
    std::string movements_arrows {{'^'},{'<'},{'V'},{'>'}};


};

