#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>

int countAdjacent(const std::vector<std::vector<int>> &arr, int row, int col) {
    int count = 0;
    int directions[8][2] = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},          {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };
    for (const auto& dir : directions) {
        int newRow = row + dir[0];
        int newCol = col + dir[1];
        if (newRow < 0 || newRow >= static_cast<int>(arr.size()) ||
            newCol < 0 || newCol >= static_cast<int>(arr[0].size())) {
            continue;
        } else {
            count += arr[newRow][newCol];
        }
    }
    return count;
}

int task1() {

    int output = 0;
    
    std::ifstream infile("input.data");
    std::string line;
    // Read all lines into memory
    if (!infile.is_open()) {
        std::cerr << "Failed to open input.data" << std::endl;
        return -1;
    }

    std::vector<std::string> lines;
    while (std::getline(infile, line)) {
        lines.push_back(line);
    }
    infile.close();

    if (lines.empty()) {
        std::cerr << "input.data is empty" << std::endl;
        return -1;
    }

    // y = number of rows, x = row length
    int y = static_cast<int>(lines.size());
    int x = lines[0].size();

    // allocate a row-major 2D array: rows (y) x cols (x)
    std::vector<std::vector<int>> arr(y, std::vector<int>(x, 0));

    // fill array: arr[row][col]
    for (int row = 0; row < y; ++row) {
        const std::string &l = lines[row];
        for (int col = 0; col < static_cast<int>(l.size()); ++col) {
            char c = l[col];
            if (c == '@') arr[row][col] = 1;
            else arr[row][col] = 0;
        }
    }

    for (int idy = 0; idy < y; idy++) {
        for (int idx = 0; idx <x; idx++) {
            if (arr[idx][idy] == 1 && countAdjacent(arr, idx, idy) < 4) {
                output++;
            }
        }
    }


    return output;
}

int task2() {

    int output = 0;
    
    std::ifstream infile("input.data");
    std::string line;
    if (!infile.is_open()) {
        std::cerr << "Failed to open input.data" << std::endl;
        return -1;
    }

    std::vector<std::string> lines;
    while (std::getline(infile, line)) {
        lines.push_back(line);
    }
    infile.close();

    if (lines.empty()) {
        std::cerr << "input.data is empty" << std::endl;
        return -1;
    }

    // y = number of rows, x = row length
    int y = static_cast<int>(lines.size());
    int x = lines[0].size();

    // allocate a row-major 2D array: rows (y) x cols (x)
    std::vector<std::vector<int>> arr(y, std::vector<int>(x, 0));

    // fill array: arr[row][col]
    for (int row = 0; row < y; ++row) {
        const std::string &l = lines[row];
        for (int col = 0; col < static_cast<int>(l.size()); ++col) {
            char c = l[col];
            if (c == '@') arr[row][col] = 1;
            else arr[row][col] = 0;
        }
    }

    int temp = 67;

    while (temp != 0) {
        temp = 0;

        for (int idy = 0; idy < y; idy++) {
            for (int idx = 0; idx <x; idx++) {
                if (arr[idx][idy] == 1 && countAdjacent(arr, idx, idy) < 4) {
                    arr[idx][idy] = 0;
                    temp++;
                }
            }
        }
        output += temp;
    }
    return output;
}

int main() {
    std::cout << "task1: " << task1() << std::endl;
    std::cout << "task2: " << task2() << std::endl;
}
