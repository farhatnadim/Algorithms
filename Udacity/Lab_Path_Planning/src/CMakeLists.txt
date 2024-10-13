# Set the C++ standard (optional)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Specify the directory where Eigen is located
set(EIGEN_DIR "/Users/nedfarhat/Documents/source/eigen")  # Replace this with the actual path to the Eigen library
include_directories(${EIGEN_DIR})

add_executable(Main
  # Add your source files here
  main.cpp
)

target_include_directories(Main PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${EIGEN_DIR})