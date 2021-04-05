/*
	Because the count of local should <= count of global, all we care is when local < global happens.
The difference between local and global is global also include nonadjacent i and j, so simplify	the question to for
every i, find in range 0 to i-2, see if there is an element larger than A[i], if it exists, we can return false
directly. And we can maintain a variable max for the linear implementation.
*/

public boolean isIdealPermutation(int[] A) {
	int max = -1;
	for (int i = 0; i < A.length - 2; ++i) {
		max = Math.max(max, A[i]);
		if (max > A[i + 2])
			return false;
	}

	return true;
}