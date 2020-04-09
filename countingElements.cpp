// link: https://github.com/petercrackthecode/LeetcodePractice

int countElements(vector<int>& arr) {
	std::map<int, int> numberLookup;
	int counter{0};
        
	for (int elem : arr) {
		++numberLookup[elem];
	}
        
    for (auto pair : numberLookup) {
        if (numberLookup.count((pair.first) + 1) != 0) {
            counter+= pair.second;
        }
    }

	return counter;
}

// Not the most optimal solution, will figure out a better solution later.