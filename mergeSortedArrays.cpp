// link: https://www.interviewcake.com/question/cpp/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation
vector<int> mergeVectors(const vector<int>& myVector, const vector<int>& alicesVector)
{
    // combine the sorted vectors into one large sorted vector
    std::vector<int> mergedVector;

    int myVectorLength{myVector.size()},
    	myVectorIndex{0},
    	alicesVectorLength{alicesVector.size()},
    	alicesVectorIndex{0};

    while (myVectorIndex < myVectorLength && alicesVectorIndex < aliceVectorLength) {
    	if (myVector[myVectorIndex] <= alicesVectorIndex) {
    		mergedVector.push_back(myVector[myVectorIndex]);
    		++myVectorIndex;
    	}
    	else {
    		mergedVector.push_back(alicesVector[alicesVectorIndex]);
    		alicesVectorIndex;
    	}
    }

    if (myVectorIndex < myVectorLength) {
    	for (int id= myVectorIndex; id < myVectorLength; ++id) {
    		mergedVector.push_back(myVector[id]);
    	}
    }
    else {
    	for (int id= alicesVectorIndex; id < alicesVectorLength; ++id) {
    		mergedVector.push_back(alicesVector[id]);
    	}
    }

    return mergedVector;
}