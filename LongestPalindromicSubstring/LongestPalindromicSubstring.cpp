string longestPalindrome(string s) {
  if (s.length() <= 1)
    return s;

  string longestPalindrome{""};
  int longestPalindromeLength{0};

  for (int index = 0; index < s.length() - 1; ++index) {
    int oneCharacterCentralLength = expandAroundCenter(s, index, index),
        twoCharactersCentralLength = expandAroundCenter(s, index, index + 1),
        longest =
            std::max(oneCharacterCentralLength, twoCharactersCentralLength);

    if (longest > longestPalindromeLength) {
      longestPalindromeLength = longest;
      int startIndex = index - (longest - 1) / 2;
      longestPalindrome = s.substr(startIndex, longest);
    }
  }

  return longestPalindrome;
}

int expandAroundCenter(string s, int left, int right) {
  while (left >= 0 && right < s.length() && s.at(left) == s.at(right)) {
    --left;
    ++right;
  }

  return right - left - 1;
}