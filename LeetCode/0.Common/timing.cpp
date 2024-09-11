#include "timing.hpp"
template <typename Func, typename... Args>
auto measure_time(Func&& func, Args&&... args) {
    static_assert(std::is_invocable_v<Func, Args...>, "Provided arguments are not valid for the function!");

    // Record the start time
    auto start = std::chrono::high_resolution_clock::now();
    
    // Execute the function with its arguments
    if constexpr (std::is_void_v<std::invoke_result_t<Func, Args...>>) {
        // If the function returns void, just call it
        std::invoke(std::forward<Func>(func), std::forward<Args>(args)...);
    } else {
        // If the function has a return type, capture and return it
        auto result = std::invoke(std::forward<Func>(func), std::forward<Args>(args)...);
        
        // Record the end time
        auto end = std::chrono::high_resolution_clock::now();

        // Calculate the elapsed time in microseconds
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        
        std::cout << "Execution time: " << duration << " microseconds\n";

        return result;
    }

    // Record the end time for void functions
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time in microseconds
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    
    std::cout << "Execution time: " << duration << " microseconds\n";
}
