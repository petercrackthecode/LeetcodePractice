//https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
/*
    1. Find the number of soldiers are there in each row, save it to soldiersWatch Map (key - value: row - number of soldiers)
    2. Sort the array ascendingly based on the number of soldiers (use both of the maps to track):
        If the number of soldiers are the same, sort them based on their indexes.
    3. Return the first k elements in the array of indexes.
*/
class Solution { 
    public int[] kWeakestRows(int[][] mat, int k) {
        HashMap<Integer, Integer> soldiersCountOnRow = new HashMap<Integer, Integer>();
        
        Integer[] rows = new Integer[mat.length];
        int numberOfSoldiersOnCurrentRow;
        
        for (int index = 0; index < mat.length; ++index) {
            numberOfSoldiersOnCurrentRow = 0;
            for (int person : mat[index]) {
                if (person == 1) {
                    ++numberOfSoldiersOnCurrentRow;
                }
            }
            
            soldiersCountOnRow.put(index, numberOfSoldiersOnCurrentRow);
            rows[index] = index;
        }
        
        Arrays.sort(rows, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                Integer soldiersOnA = soldiersCountOnRow.get(a),
                        soldiersOnB = soldiersCountOnRow.get(b);
                
                if (soldiersOnA.compareTo(soldiersOnB) != 0) {
                    return soldiersOnA.compareTo(soldiersOnB);
                }
                else return a.compareTo(b);
            }
        });
        
        int[] ans = new int[k];
        
        for (int index = 0; index < k; ++index) {
            ans[index] = rows[index];
        }
        
        return ans;
    }
}