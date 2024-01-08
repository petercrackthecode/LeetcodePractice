# https://leetcode.com/problems/minimum-window-substring/
def min_window(s: str, t: str) -> str:
    # empty string scenario
    if t == '':
        return ''

    # creating the two hash maps
    req_count = {}
    window = {}

    # populating req_count hash map
    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)

    # populating window hash map
    for c in t:
        window[c] = 0

    # setting up the conditional variables
    current, required = 0, len(req_count)

    # setting up a variable containing the result's starting and ending point
    # with default values and a length variable
    res, res_len = [-1, -1], float('infinity')

    # setting up the sliding window pointers
    left = 0
    for right in range(len(s)):
        c = s[right]

        # if the current character also occurs in t, update its frequency in window hash map
        if c in t:
            window[c] = 1 + window.get(c, 0)

        # updating the current variable
        if c in req_count and window[c] == req_count[c]:
            current += 1

        # adjusting the sliding window
        while current == required:
            # update our result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # pop from the left of our window
            if s[left] in t:
                window[s[left]] -= 1

            # if the popped character was among the required characters and
            # removing it has reduced its frequency below its frequency in t, decrement current
            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            left += 1
    left, right = res

    # return the minimum window substring
    return s[left:right+1] if res_len != float('infinity') else ""
