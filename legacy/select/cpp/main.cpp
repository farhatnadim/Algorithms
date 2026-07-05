#include <iostream>
// include input file stream
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;
int partition( vector<int> & array)
{
    auto pivot = array[0];
    int i = 1;
    for (int j =1 ; j < array.size(); j++ )
    { 
        if (array[j] < pivot )
        {
            swap(array[i], array[j]);
            i++;    
        }
    } 
    swap(array[0], array[i-1]);
    return i-1;
}


// reads file and return vector of ints
void read_file(string file_name, vector<int> &vec)
{   
    try {
        ifstream file(file_name);
        if (file.is_open())
        {
            string line;
            while (getline(file, line))
            {
                vec.push_back(stoi(line));
            }
            file.close();
        }
        else
        {
            cout << "Unable to open file" << endl;
        }
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    
}




int main(int argc , char * argv[])
{
    if (argc < 1)
    {
        std::cout << "Usage: " << argv[0] << std::endl;
        return 1;
    }
    string file_name = argv[1];
    vector<int> input_vec;
    read_file(file_name, input_vec);
    for (auto &element : input_vec)
    {
        cout << element << endl;
    }   
}
