cmake_minimum_required(VERSION 3.10)
project(MinimumCut)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create a static library named 'engine' from 'engine.cpp'
add_executable(mincut MinimumCut.cpp)

