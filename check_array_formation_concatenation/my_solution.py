from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        '''
        - arr is a 1D array, pieces is a 2D array
        - arr has distinct integers, integers in pieces are distinct
        - form arr by concatenating the arrays in pieces
        
        arr    = [91, 4, 64, 78]
        
        pieces = [[78], [4, 64], [91]]
                    0    1         2 
        - save the index of the subarray of each number in pieces
        
        indices_in_pieces:Dict[int, int] = {
            78: 0,
            4: 1,
            64: 1
            91: 2
        }
        - loop thru pieces to initialize indices_in_pieces
        - have an array called pieces_unpack:List[int] = []
        - i = 0
        - loop: while i is smaller than arr's length:
            - num:int = arr[i]
            - if num doesn't exist in indices_in_pieces: return False immediately
            - otherwise, lookup the index in pieces: idx_in_pieces:int = indices_in_pieces[num]
            - get the sub_array: subarray = pieces[idx_in_pieces]
            - add subarray to pieces_unpack: pieces_unpack += subarray
            - increment i by the length of subarray
            
        - return arr == pieces_unpack
        '''
        # (num:int, index: int)
        indices_in_pieces:Dict[int, int] = {}
        
        for i, piece in enumerate(pieces):
            for num in piece:
                indices_in_pieces[num] = i
        
        pieces_unpack:List[int] = []
        i:int = 0
            
        while i < len(arr):
            num:int = arr[i]
            if not num in indices_in_pieces:
                return False
            idx_in_pieces:int = indices_in_pieces[num]
            piece:List[int] = pieces[idx_in_pieces]
            
            pieces_unpack += piece
            
            i += len(piece)
            
        return arr == pieces_unpack
        
        
        
        
        