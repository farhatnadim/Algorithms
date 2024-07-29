cmake_minimum_required(VERSION 3.10)
project(GraphTestProgram)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the engine directory as a subdirectory if you have other CMakeLists.txt files in subdirectories
# include(.)

# Add an executable named 'GraphTest' that is built from 'graph_test_program.cpp'
add_executable(GraphTest graph_test_program.cpp)

# Add the Graph source files
set(SOURCES Graph.cpp Symbol.cpp)

# Add the Graph header files
set(HEADERS Graph.hpp Symbol.hpp)

# Include the current directory for header files
include_directories(${CMAKE_SOURCE_DIR})

# Link the executable 'GraphTest' with the Graph source files
target_sources(GraphTest PRIVATE ${SOURCES} ${HEADERS})