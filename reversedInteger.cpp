int reverse(int x) {
    long int reversedX{0};
    long int absolutedX = std::abs(x);
    int digit{0};

    while (absolutedX != 0) {
        digit = absolutedX % 10;
        absolutedX /= 10;

        reversedX = (reversedX * 10) + digit;
    }

    if (x < 0)
        reversedX = -reversedX;

    // check if the number is within the range of 32-bit signed integer or not
    if (static_cast<int>(reversedX) == reversedX) return reversedX;
    else return 0;
}