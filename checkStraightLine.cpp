// link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
bool checkStraightLine(vector<vector<int>> &coordinates) {
	double rateOfChange = static_cast<double>(coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0]);

	const int FIRST_COORD_X = coordinates[0][0],
			  FIRST_COORD_Y = coordinates[0][1];

	for (int index = 2; index < coordinates.size(); ++index) {
		double currRateOfChange = static_cast<double>(coordinates[index][1] - FIRST_COORD_Y) / (coordinates[index][0] - FIRST_COORD_X);

		if (std::fabs(currRateOfChange - rateOfChange) > 0.00005)
			return false;
	}

	return true;
}