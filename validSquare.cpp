typedef std::vector<int> vi;

bool isTooVectorsPerpendicular(const vi &v1, const vi &v2) {
    return v1[0] * v2[0] + v1[1] * v2[1] == 0;
}

bool doTwoVectorsHaveSameLength(const vi &v1, const vi &v2) {
    return pow(v1[0], 2) + pow(v1[1], 2) == pow(v2[0], 2) + pow(v2[1], 2);
}

bool validSquare(vector<int> &p1, vector<int> &p2, vector<int> &p3, vector<int> &p4) {
    if (p1 == p2 || p1 == p3 || p1 == p4)
        return false;
    if (p2 == p3 || p2 == p4)
        return false;
    if (p3 == p4)
        return false;

    vi p1p2 = {p2[0] - p1[0], p2[1] - p1[1]},
       p1p3 = {p3[0] - p1[0], p3[1] - p1[1]},
       p1p4 = {p4[0] - p1[0], p4[1] - p1[1]};

    vi p2p3 = {p3[0] - p2[0], p3[1] - p2[1]},
       p2p4 = {p4[0] - p2[0], p4[1] - p2[1]};

    vi p3p4 = {p4[0] - p3[0], p4[1] - p3[1]};

    if ((isTooVectorsPerpendicular(p1p2, p1p3) && doTwoVectorsHaveSameLength(p1p2, p1p3) && doTwoVectorsHaveSameLength(p1p2, p2p4) && doTwoVectorsHaveSameLength(p1p2, p2p3)) || (isTooVectorsPerpendicular(p1p2, p1p4) && doTwoVectorsHaveSameLength(p1p2, p1p4) && doTwoVectorsHaveSameLength(p1p2, p2p3) && doTwoVectorsHaveSameLength(p1p2, p3p4)) || (isTooVectorsPerpendicular(p1p4, p1p3) && doTwoVectorsHaveSameLength(p1p4, p1p3) && doTwoVectorsHaveSameLength(p1p4, p2p3) && doTwoVectorsHaveSameLength(p1p4, p2p4)))
        return true;
    else std::cout << "p1 failed\n";

    if ((isTooVectorsPerpendicular(p1p2, p2p3) && doTwoVectorsHaveSameLength(p1p2, p2p3) && doTwoVectorsHaveSameLength(p1p2, p1p4) && doTwoVectorsHaveSameLength(p1p2, p3p4)) || (isTooVectorsPerpendicular(p1p2, p2p4) && doTwoVectorsHaveSameLength(p1p2, p2p4) && doTwoVectorsHaveSameLength(p1p2, p1p3) && doTwoVectorsHaveSameLength(p1p2, p3p4)) || (isTooVectorsPerpendicular(p2p3, p2p4) && doTwoVectorsHaveSameLength(p2p3, p2p4) && doTwoVectorsHaveSameLength(p2p3, p1p3) && doTwoVectorsHaveSameLength(p2p3, p1p4)))
        return true;
    else std::cout << "p2 failed\n";

    if ((isTooVectorsPerpendicular(p1p3, p2p3) && doTwoVectorsHaveSameLength(p1p3, p2p3) && doTwoVectorsHaveSameLength(p1p3, p1p4) && doTwoVectorsHaveSameLength(p1p3, p2p4)) || (isTooVectorsPerpendicular(p1p3, p3p4) && doTwoVectorsHaveSameLength(p1p3, p3p4) && doTwoVectorsHaveSameLength(p1p3, p1p2) && doTwoVectorsHaveSameLength(p1p3, p2p4)) || (isTooVectorsPerpendicular(p2p3, p3p4) && doTwoVectorsHaveSameLength(p2p3, p3p4) && doTwoVectorsHaveSameLength(p2p3, p1p2) && doTwoVectorsHaveSameLength(p2p3, p1p4)))
        return true;
    else std::cout << "p3 failed\n";

    return false;
}
