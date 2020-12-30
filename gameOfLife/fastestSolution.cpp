class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        
        //0,1, 2:1 to 0, 3:0 to 1
        int c ;
        for(int i =0; i<board.size(); i++)
        {
            for(int j =0; j<board[i].size(); j++)
            {
                c = 0;
                for(int k = i-1; k<= i+1; k++)
                {
                    for(int l = j-1; l<= j+1; l++)
                    {
                        if(l>=0 && l<board[i].size() && k>=0 && k<board.size()&& (board[k][l] == 1 || board[k][l] == 2))
                            c++;
                    }
                }
                
                if(board[i][j] == 1)
                    c--;
                
                if(c<2 && board[i][j] == 1)
                    board[i][j] = 2;
                else if(c>3 && board[i][j] == 1)
                    board[i][j] = 2;
                else if(c == 3 && board[i][j] == 0)
                    board[i][j] = 3;
            }
        }
        
        for(int i =0; i<board.size(); i++)
        {
            for(int j =0; j<board[i].size(); j++)
            {
                if(board[i][j] == 2)
                    board[i][j] = 0;
                else if(board[i][j] == 3)
                    board[i][j]=1;
            }
        }
        
    }
};