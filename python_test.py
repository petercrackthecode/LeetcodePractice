from collections import defaultdict


def deletion_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)

    str1_characters_freq = defaultdict(int)
    str2_characters_freq = defaultdict(int)
    common_characters_freq = defaultdict(int)

    for ch_1 in str1:
        str1_characters_freq[ch_1] += 1

    for ch_2 in str2:
        str2_characters_freq[ch_2] += 1
    print('str1_characters_freq = ', str1_characters_freq)
    print('str2_characters_freq = ', str2_characters_freq)

    # find the common_characters_freq
    for (ch, freq) in str1_characters_freq.items():
        if ch in str2_characters_freq:
            common_characters_freq[ch] = min(
                str1_characters_freq[ch], str2_characters_freq[ch])

    # print('still working here')

    [i, j] = [0, 0]
    substr_length = 0

    while i < len(str1) and j < len(str2):
        ch_1 = str1[i]
        if common_characters_freq[ch_1] > 0:
            ch_2 = str2[j]
            if ch_1 == ch_2:
                common_characters_freq[ch_1] -= 1
                substr_length += 1
                i += 1
            j += 1
        else:
            i += 1

    return (len(str1) - substr_length) + (len(str2) - substr_length)


str_1 = "hit"
str_2 = "heat"
print(deletion_distance(str_1, str_2))
