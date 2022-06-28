// link: https://leetcode.com/problems/flood-fill/
int maxCol, maxRow;

void fillPixel(std::vector<std::vector<int>> &image, const int &r, const int &c, const int &newColor, const int &savedColor)	{
    image[r][c] = newColor;
    if (r - 1 >= 0 && image[r - 1][c] == savedColor)
    {
        fillPixel(image, r - 1, c, newColor, savedColor);
    }
    if (r + 1 <= maxRow && image[r + 1][c] == savedColor)
    {
        fillPixel(image, r + 1, c, newColor, savedColor);
    }
    if (c - 1 >= 0 && image[r][c - 1] == savedColor)
    {
        fillPixel(image, r, c - 1, newColor, savedColor);
    }
    if (c + 1 <= maxCol && image[r][c + 1] == savedColor)
    {
        fillPixel(image, r, c + 1, newColor, savedColor);
    }
}

std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>> &image, int sr, int sc, int newColor)
{
    int savedColor = image[sr][sc];
    maxRow = image.size() - 1,
    maxCol = image[0].size() - 1;
    if (savedColor != newColor)
        fillPixel(image, sr, sc, newColor, savedColor);


    return image;
}