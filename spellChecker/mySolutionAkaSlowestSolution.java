// link: https://leetcode.com/problems/vowel-spellchecker/

/*
    1. Have 2 maps: firstAppearedIndexOfIgnoredCaseWords, doesWordExist.
       The first map saves the first index of the words that share the same uppercase value.
       The second map returns if the query exists in wordlist (case-sensitive).
    2. Loop through wordlist to populate two maps.
    3. Loop through queries, we have 3 cases:
        - If the query exists in the doesWordExist map, append the query to the ans array.
        - Else if the uppercased query exist in firstAppearedIndexOfIgnoredCaseWords, append wordlist.get(firstAppearedIndexOfIgnoredCaseWords.get(uppercased query)) to the ans array.
        - Else check if there is a vowel errors in query by replacing every single vowels in that query by another vowel (use String.toCharArray() for simpliscity), if yes, append wordlist.get(firstAppearedIndexOfIgnoredCaseWords.get(uppercased query)) to the ans array, 
        - Otherwise, append an empty string to the ans array.
*/
class Solution {
    private char[] vowels = new char[]{'A', 'E', 'I', 'O', 'U'};
    private HashMap<String, Integer> firstAppearedIndexOfIgnoredCaseWords = new HashMap<>();
    private HashMap<String, Boolean> doesWordExist = new HashMap<>();
    private HashMap<String, String> doesVowelsVariantExist = new HashMap<>();
    private String[] ans;
    private int ansNonEmptyStringCount = 0;
    
    private void addAnswer(String s) {
        ans[ansNonEmptyStringCount] = s;
        ++ansNonEmptyStringCount;
    }
    
    private boolean isVowel(char ch) {
        ch = Character.toUpperCase(ch);
        return (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U');
    }
    
    private void populateVowels(char[] ch, int index, String variant) {
        if (index >= ch.length) {
            if (!doesVowelsVariantExist.containsKey(variant))
                doesVowelsVariantExist.put(variant, String.valueOf(ch));
        }
        else if (isVowel(ch[index])) {
            for (char vowel : vowels)
                populateVowels(ch, index + 1, variant + vowel);
        }
        else populateVowels(ch, index + 1, variant + Character.toUpperCase(ch[index]));
    }
    
    public String[] spellchecker(String[] wordlist, String[] queries) {
        ans = new String[queries.length];
       
        String uppercasedWord = "";
        vowels = new char[]{'A', 'E', 'I', 'O', 'U'};
        
        for (int index = 0; index < wordlist.length; ++index) {
            uppercasedWord = wordlist[index].toUpperCase();
            if (!firstAppearedIndexOfIgnoredCaseWords.containsKey(uppercasedWord)) {
                firstAppearedIndexOfIgnoredCaseWords.put(uppercasedWord, index);
                populateVowels(wordlist[index].toCharArray(), 0, "");
            }
            if (!doesWordExist.containsKey(wordlist[index])) {
                doesWordExist.put(wordlist[index], true);
            }
        }
        
        for (String query : queries) {
            uppercasedWord = query.toUpperCase();
            if (doesWordExist.containsKey(query))
                addAnswer(query);
            else if (firstAppearedIndexOfIgnoredCaseWords.containsKey(uppercasedWord))
                addAnswer(wordlist[firstAppearedIndexOfIgnoredCaseWords.get(uppercasedWord)]);
            else if (doesVowelsVariantExist.containsKey(uppercasedWord))
                addAnswer(doesVowelsVariantExist.get(uppercasedWord));
            else addAnswer("");
            
        }
        
        return ans;
    }
}