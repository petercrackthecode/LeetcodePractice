// link: https://leetcode.com/problems/letter-case-permutation/
class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> list = new LinkedList<>();
        permHelper( S.toCharArray(), 0, list);
        return list;        
    }
    
    private void permHelper( char[] strArr, int pos, List<String> list ){
        if( pos == strArr.length ){
            list.add(new String(strArr));
            return;
        }
        
        if( strArr[pos] >='0' && strArr[pos] <= '9' ){
            permHelper( strArr, pos + 1, list);
            return;
        }
                
        strArr[pos] = Character.toUpperCase(strArr[pos]);
        permHelper( strArr, pos + 1, list);

        strArr[pos] = Character.toLowerCase(strArr[pos]);
        permHelper( strArr, pos + 1, list);
        
    }
}