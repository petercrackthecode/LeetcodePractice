// link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) 
    {
        string newstring1,newstring2;
        for(int i=0 ; i<word1.size() ; i++)
        {
            newstring1+=word1[i];
        }
        for(int i=0 ; i<word2.size() ; i++)
        {
            newstring2+=word2[i];
        }
        if(newstring1==newstring2)
            return true;
        else
            return false;
        
    }
};