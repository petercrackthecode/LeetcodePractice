class Solution {
public:
    /* ASSESSMENT:
       reassign: liveCellsCount = 0
       Check the top 3 elements right above the current cell. (A[i-1][j-1], A[i-1][j], A[i-1][j+1])
       Check the left cell & right cell.
       Check the bottom 3 elements right below the current cell. ((A[i+1][j-1], A[i+1][j], A[i+1][j+1]))
       Be careful with borders everytime you check those aforementioned cases.
       Everytime we see a cell with the result != 0 && result != 3, ++liveCellsCount;
       // cell status: 0: dead cell in both phases, 1: unchecked alive cell, 2: alive in phase I but dead in phase II
       // 3: dead cell in phase I but alive in phase II, 4: alive in both phases.
       if (liveCellsCount == 3 && currentCell == 0): currentCell = 3
       else if (liveCellsCount < 2 && currentCell == 1): currentCell = 2
       else if (liveCellsCount <= 3 && currentCell == 1): currentcell = 4
       else if (liveCellsCount > 3 && currenCell == 1): currentCell = 2
    */
    
    /* 1. Traverse through the 2D array.
       2. Start the assessment.
       3. Traverse through the 2D array again:
            If (currentCell == 2) currentCell = 0
            else if (currenCell == 3 || currentCell == 4): currentCell = 1
    */
    auto adjustCellStatus(vector<vector<int>> &board, const int &row, const int &col) -> void {
        int liveCellsCount = 0;
        // check top
        if (row - 1 >= 0) {
            if (col - 1 >= 0 && board[row-1][col-1] != 0 && board[row-1][col-1] != 3)
                ++liveCellsCount;
            if (board[row-1][col] != 0 && board[row-1][col] != 3)
                ++liveCellsCount;
            if (col + 1 < board[0].size() && board[row-1][col+1] != 0 && board[row-1][col+1] != 3)
                ++liveCellsCount;
        }
        // check left:
        if (col - 1 >= 0 && board[row][col-1] != 0 && board[row][col-1] != 3)
            ++liveCellsCount;
        // check right:
        if (col + 1 < board[0].size() && board[row][col+1] != 0 && board[row][col+1] != 3)
            ++liveCellsCount;
        
        // check bottom:
        if (row + 1 < board.size()) {
            if (col - 1 >= 0 && board[row+1][col-1] != 0 && board[row+1][col-1] != 3)
                ++liveCellsCount;
            if (board[row+1][col] != 0 && board[row+1][col] != 3)
                ++liveCellsCount;
            if (col + 1 < board[0].size() && board[row+1][col+1] != 0 && board[row+1][col+1] != 3)
                ++liveCellsCount;
        }
        
        if (liveCellsCount == 3 && board[row][col] == 0) 
            board[row][col] = 3;
        else if (liveCellsCount < 2 && board[row][col] == 1) 
            board[row][col] = 2;
        else if (liveCellsCount <= 3 && board[row][col] == 1) 
            board[row][col] = 4;
        else if (liveCellsCount > 3 && board[row][col] == 1) 
            board[row][col] = 2;
    }
    
    void gameOfLife(vector<vector<int>>& board) {
        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board[0].size(); ++col) {
                adjustCellStatus(board, row, col);
            }
        }
        
        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board[0].size(); ++col) {
                if (board[row][col] == 2)
                    board[row][col] = 0;
                else if (board[row][col] == 3 || board[row][col] == 4)
                    board[row][col] = 1;
            }
        }
    }
};