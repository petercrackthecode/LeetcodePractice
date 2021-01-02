typedef std::map<int, int> mii;
typedef std::vector<int> vi;
typedef std::vector<vector<int>> vii;

class Solution {
public:
    /* Step 1: Label the positions of all the elements in arr, put them into a map
       Step 2: Sort the sub array in pieces based on their elements' indices in the map (the smaller the indices the earlier)
       Step 3: Flatten the sub array, put all of their elements into a map <key, value> = <element, index>
       Step 4: Traverse through the array arr, for each element, search for its position in the expanded array through the map. If the searched element isn't found or its found index is smaller than the lastIndex, return false.
       Step 5: Return true;
    */
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        bool ans = true;
        
        mii arrPositionLookup,
            expandedPiecesPositionLookup;
        
        for (int index = 0; index < arr.size(); ++index) {
            arrPositionLookup[arr[index]] = index + 1;
        }
        
        std::sort(pieces.begin(), pieces.end(), [&arrPositionLookup](vi a, vi b) -> bool {
            int firstAppearIndexInA = 0,
                firstAppearIndexInB = 0;
            
            while (firstAppearIndexInA < a.size() && arrPositionLookup.count(a.at(firstAppearIndexInA)) == 0)
                ++firstAppearIndexInA;
            
            while (firstAppearIndexInB < b.size() && arrPositionLookup.count(b.at(firstAppearIndexInB)) == 0)
                ++firstAppearIndexInB;
            
            // both arrays don't have any number shown up in arr, sort 'em however you want.
            if (firstAppearIndexInA >= a.size() && firstAppearIndexInB >= b.size())
                return a[0] < b[0];
            else if (firstAppearIndexInA >= a.size())
                return false;
            else if (firstAppearIndexInB >= b.size())
                return true;
            // both firstAppearIndexInA < a.size() && firstAppearIndexInB < b.size()
            else return arrPositionLookup[a.at(firstAppearIndexInA)] < arrPositionLookup[b.at(firstAppearIndexInB)];
        });
        
        /*
        for (vi piece : pieces) {
            for (int num : piece)
                std::cout << num << " ";
        }
        
        std::cout << "\n";
        */
        
        int flattenArraySize = 0;
        
        for (vi piece : pieces) {
            for (int num : piece) {
                ++flattenArraySize;
                expandedPiecesPositionLookup[num] = flattenArraySize;
            }
        }
        
        int lastPosition = INT_MIN;
        
        for (int num : arr) {
            if (expandedPiecesPositionLookup.count(num) != 0 && expandedPiecesPositionLookup[num] > lastPosition)
                lastPosition = expandedPiecesPositionLookup[num];
            else {
                ans = false;
                break;
            }
        }
        
        return ans;
    }
};