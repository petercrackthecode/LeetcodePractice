#include <vector>

using namespace std;

class Solution
{
public:
    /*  1. Sort the array of people ascendingly.
        2. Take the rightmost element (also the greatest), match it with the smallest element
        3. Move two pointers, keep matching until we find no remaining light-weight person to fit into the board.
        4. Iterate step 2 until rightPointer <= leftPointer
    */

    /*  Logic:
        For every heavy person taken from the right side of the array, see if we can fit
        a light-weight person into the boat with him/her.
        Keep doing it until the limit of heavy people and light-weight people crosses
        (no more person to be chosen from the list).
    */

    int numRescueBoats(vector<int> &people, int limit)
    {
        int rightPointer = people.size() - 1,
            leftPointer = 0,
            boatsCount = 0,
            remainingRoomInTheBoat = limit;

        std::sort(people.begin(), people.end());

        if (limit - people[0] < people[0])
            return people.size();

        while (leftPointer <= rightPointer)
        {
            remainingRoomInTheBoat -= people[rightPointer];

            if (leftPointer < rightPointer && remainingRoomInTheBoat >= people[leftPointer])
            {
                remainingRoomInTheBoat -= people[leftPointer];
                ++leftPointer;
            }

            remainingRoomInTheBoat = limit;
            ++boatsCount;
            --rightPointer;
        }

        return boatsCount;
    }
};