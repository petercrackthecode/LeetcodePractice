// link: https://leetcode.com/problems/brick-wall/
class Solution {
public:
    int leastBricks(vector < vector < int >> & wall) {
        map < int, int > rowsWhichContainALine;

        // 1. Translate the wall bricks array into a line array
        int linePosition = 0;
        for (int index = 0; index < wall.size(); ++index) {
            linePosition = 0;

            for (int i = 0; i < wall[index].size() - 1; ++i) {
                linePosition += wall[index][i];
                ++rowsWhichContainALine[linePosition];
            }
        }

        int ans = wall.size();

        for (auto const& [line, rowsWithThatLineCounter]: rowsWhichContainALine) {
            ans = std::min(ans, int(wall.size() - rowsWithThatLineCounter));
        }

        return ans;
    }
};