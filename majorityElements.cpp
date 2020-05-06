// link: https://leetcode.com/problems/majority-element/
int majorityElement(vector<int> &nums) {
	int majorityNum{nums[0]},
		size= nums.size(),
		numVote{0};

	for (int index{0}; index < size; ++index) {
		if (nums[index] == majorityNum) {
			++numVote;
		}
		else {
			--numVote;
			if (numVote == 0) {
				numVote= 1;
				majorityNum= nums[index];
			}
		}
	}

	return majorityNum;
}