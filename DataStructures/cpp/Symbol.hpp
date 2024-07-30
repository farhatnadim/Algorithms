#pragma once 
#include "Graph.hpp"
#include <string>
#include <map>
#include <vector>
/**  */
using symbol_table = std::map<std::string,int> ;


class SymbolGraph
{
    public:
    SymbolGraph();
    std::vector<std::string> m_keys;
    symbol_table m_st;
    Graph m_g;

}; // end of class SymbolGraph