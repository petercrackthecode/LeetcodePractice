// link: https://leetcode.com/problems/keys-and-rooms/
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visitedRooms = new boolean[rooms.size()];
        moveBetweenRooms(rooms, 0, visitedRooms);
        
        for(boolean isRoomVisited: visitedRooms) {
            if(!isRoomVisited) {
                return false;
            }
        }
        
        return true;
    }
    
    private void moveBetweenRooms(List<List<Integer>> rooms, int curRoom, boolean[] visitedRooms) {
        
        if(visitedRooms[curRoom]) {
            return;
        }
        visitedRooms[curRoom] = true;
        List<Integer> accessibleRooms = rooms.get(curRoom);
        for(int room: accessibleRooms) {
            moveBetweenRooms(rooms, room, visitedRooms);
        }
    }
}

