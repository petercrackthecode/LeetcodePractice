# https://leetcode.com/problems/minimum-window-subsequence/
def min_window(str1, str2):
    # save the size of str1 and str2
    size_str1, size_str2 = len(str1), len(str2)

    # initialize min_sub_len to a very large number (infinity)
    min_sub_len = float('inf')

    # initialize pointers to zero and the min_subsequence to an empty string
    index_s1, index_s2 = 0, 0
    min_subsequence = ""

    # iterate over str1
    while index_s1 < size_str1:
        # check if the character pointed by index_s1 in str1
        # is the same as the character pointed by index_s2 in str2
        if str1[index_s1] == str2[index_s2]:
            # if the pointed character is the same
            # in both strings increment index_s2
            index_s2 += 1

            # check if index_s2 has reached the end of str2
            if index_s2 == size_str2:
                # initialize start to the index where all characters of
                # str2 were present in str1
                start, end = index_s1, index_s1
                index_s2 -= 1

                # decrement pointer index_s2 and start a reverse loop
                while index_s2 >= 0:
                    # decrement pointer index_s2 until all characters of
                    #  str2 are found in str1
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1

                    # decrement start pointer everytime to find the
                    # starting point of the required subsequence
                    start -= 1
                start += 1

                # check if min_sub_len of sub sequence pointed
                # by start and end pointers is less than current min min_sub_len
                if end - start < min_sub_len:
                    # update min_sub_len if current sub sequence is shorter
                    min_sub_len = end - start

                    # update minimum subsequence string
                    # to this new shorter string
                    min_subsequence = str1[start:end+1]
                # move to the next character where our possible start substring with str2
                # as a subsequence could occur
                start += 1
                # set index_s1 to start to continue checking in str1
                # after this discovered subsequence
                index_s1 = start
                index_s2 = 0

        # increment pointer index_s1 to check next character in str1
        index_s1 += 1

    # return the minimum window subsequence
    return min_subsequence
