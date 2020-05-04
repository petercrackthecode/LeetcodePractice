// link: https://leetcode.com/problems/number-complement/submissions/
int findComplement(int num) {
	std::string stringComplement{""};

	while (num != 0) {
		stringComplement = (num % 2 == 0 ? '1' : '0') + stringComplement;
		num /= 2;
	}

	// translate the string complement to an integer
	int complement{0};
	long int base2{1};

	for (int index = stringComplement.length() - 1; index >= 0; --index) {
		if (stringComplement[index] == '1') {
			complement += base2;
		}
		base2 *= 2;
	}

	return complement;
}