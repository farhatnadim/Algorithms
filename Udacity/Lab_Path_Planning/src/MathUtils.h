
#include <Eigen/Dense>
#include <vector>


//TODO: these bridges are most probably not needed 
std::vector<std::vector<int>> matrix_to_vector( const Eigen::MatrixXd & matrix)
{
    std::vector<std::vector<int>> vec(matrix.rows(),std::vector<int>(matrix.cols()));
    for (int i = 0; i < matrix.rows(); i++)
    {
        for (int j =0 ; j < matrix.cols(); j++)
            vec[i][j] = static_cast<int>(matrix(i,j));
    }

    return vec;
}

Eigen::MatrixXd vector_to_matrix(const std::vector<std::vector<int>>& vec) {
    if (vec.empty() || vec[0].empty()) {
        return Eigen::MatrixXd();
    }
    int rows = vec.size();
    int cols = vec[0].size();
    Eigen::MatrixXd matrix(rows, cols);
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            matrix(i, j) = vec[i][j];
        }
    }
    return matrix;
}


Eigen::MatrixXd forward_difference_matrix(int n)
{
    Eigen::MatrixXd D = Eigen::MatrixXd::Zero(n,n);
    for (int i = 0 ; i < n-1 ; ++i)
    {
        D(i,i) =  -1;
        D(i,i+1) = 1;
    }
    D(n-1,n-1) = -1;

    return D;
}
