#ifndef ALGORITHMS_DOUBLE_LINKED_LIST_HPP
#define ALGORITHMS_DOUBLE_LINKED_LIST_HPP

#include <optional>

namespace algorithms {

// TODO: User implements
template<typename T>
class DoubleLinkedList {
public:
    DoubleLinkedList() = default;
    ~DoubleLinkedList() = default;

    void pushFront(const T& value);
    void pushBack(const T& value);
    std::optional<T> popFront();
    std::optional<T> popBack();
    size_t size() const;
    bool empty() const;
};

} // namespace algorithms

#endif // ALGORITHMS_DOUBLE_LINKED_LIST_HPP
