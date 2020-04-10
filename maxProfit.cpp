// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

// Solution 1: Brute Force
// Traverse through the array, calculate all the possibilities, and use recursion to find the highest price.
// Time Complexity: O(n^n). Recursive function is called n^n times
// Space complexity: O(n). Depth of recursion is n.

int maxProfit(std::vector<int> &prices, int startPos)
{
    int highestProfit{0}, buyPos = startPos;

    for (int buyPos = startPos; buyPos < prices.size() - 1; ++buyPos)
    {
        for (int sellPos = buyPos + 1; sellPos < prices.size(); ++sellPos)
        {
            if (prices[sellPos] < prices[buyPos])
            {
                break;
            }
            else if (prices[sellPos] > prices[buyPos])
            {
                int currentMaxProfit = prices[sellPos] - prices[buyPos] + maxProfit(prices, sellPos + 1);

                if (highestProfit < currentMaxProfit)
                {
                    highestProfit = currentMaxProfit;
                }
            }
        }

        ++buyPos;
    }

    return highestProfit;
}

int maxProfit(std::vector<int> &prices)
{
    return maxProfit(prices, 0);
}

// Solution 2: Peak Valley Approach
// Time complexity: O(n). Single pass
// Space complexity: O(1). Constant space required.
int maxProfit(std::vector<int> prices) {
    int i{0},
        valley= prices[0],
        peak= prices[0],
        maxProfit= 0;

    while (i < prices.size() - 1) {
        while (i < prices.size() - 1 && prices[i] >= prices[i + 1])
            ++i;
        valley= prices[i];
        // valley is the local Minimum (the points where the stocks change from decrease to increase)
        // if the initial value is greater than its adjacent, we ignore it, we don't care.

        while (i < prices.size() - 1 && prices[i] <= prices[i + 1])
            ++i;
        peak= prices[i];
        // peak is the local Maxima (the points where the stocks change from increase to decrease)
        // as we already assign peak= prices[0], we don't worry if the initial value is smaller than its successing value.


        maxProfit+= peak - valley;
    }

    return maxProfit;
}

// Solution 3: Simple One Pass
int maxProfit(std::vector<int> prices) {
    int highestProfit{0};

    for (int i= 0; i < prices.size(); ++i) {
        if (prices[i] > prices[i - 1])
            highestProfit+= prices[i] - prices[i - 1];
    }

    return highestProfit;
}
// Time complexity: O(n), single pass.
// Space complexity: O(1). Constant space needed.

