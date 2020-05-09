// link: https://leetcode.com/problems/valid-perfect-square/
bool isPerfectSquare(int num)	{
    int traversingNum = 1;

    if (num == 1)	{
        return true;
    }

    while (traversingNum <= num / 2)	{
        if (static_cast<double>(num) / traversingNum == traversingNum)	{
            return true;
        }

        ++traversingNum;
    }

    return false;
}