cmake_minimum_required(VERSION 3.14)
project(Algorithms VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable testing
enable_testing()

# Add Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Add subdirectories for each module
add_subdirectory(sort)
add_subdirectory(search)
add_subdirectory(select)
add_subdirectory(data_structures)
add_subdirectory(linear_algebra)
add_subdirectory(integer_multiplication)
add_subdirectory(minimum_cut)
add_subdirectory(misc)

# portpal parity runner (JSON/dispatch glue; see cpp/parity/registry.cpp)
option(PORTPAL_PARITY "Build the portpal parity runner" ON)
if(PORTPAL_PARITY)
  add_subdirectory(parity)
endif()
