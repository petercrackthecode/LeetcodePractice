// link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

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