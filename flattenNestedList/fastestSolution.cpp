class NestedIterator {
private:
	vector<int> list;
	int i;

	void flattenList(vector<NestedInteger> &nestedList, int i) {
		if (i == nestedList.size())
			return;
		if (nestedList[i].isInteger()) {
			list.push_back(nestedList[i].getInteger());
		}
		else {
			flattenList(nestedList[i].getList(), 0);
		}
		flattenList(nestedList, i + 1);
	}

	NestedIterator(vector<NestedInteger> &nestedList) {
		i = 0;
		flattenList(nestedList, 0);
	}

	int next() {
		return list[i++];
	}

	bool hasNext() {
		return i < list.size();
	}
}