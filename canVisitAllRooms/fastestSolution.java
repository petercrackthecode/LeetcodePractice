// link: https://leetcode.com/problems/keys-and-rooms/
class Solution {
    private boolean[] visitedRooms = new boolean[rooms.size()];

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        moveBetweenRooms(rooms, 0);

        for (boolean isRoomVisited : visitedRooms) {
            if (!isRoomVisited)
                return false;
        }

        return true;
    }

    private void moveBetweenRooms(List<List<Integer>> rooms, int currRoom) {
        if (visitedRooms[currRoom])
            return;
        visitedRooms[currRoom] = true;
        List<Integer> accessibleRooms = rooms.get(currRoom);
        for (int room : accessibleRooms)
            moveBetweenRooms(rooms, room);
    }
}

