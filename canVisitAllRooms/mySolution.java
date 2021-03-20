// link: https://leetcode.com/problems/keys-and-rooms/
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        HashMap<Integer, Boolean> openedRooms = new HashMap<>();
        for (int index = 0; index < rooms.size(); ++index) {
            openedRooms.put(index, false);
        }
        
        LinkedList<Integer> toBeVisitedRoom = new LinkedList<>();
        
        toBeVisitedRoom.add(0);
        List<Integer> keys = new ArrayList<>();
        int roomNumber;
        
        while (!toBeVisitedRoom.isEmpty()) {
            roomNumber = toBeVisitedRoom.poll();
            if (openedRooms.containsKey(roomNumber) && openedRooms.get(roomNumber))
                continue;
            else {
                openedRooms.put(roomNumber, true);
                keys = rooms.get(roomNumber);
                for (Integer key : keys) {
                    toBeVisitedRoom.add(key);
                }
            }
        }
        
        for (Map.Entry<Integer, Boolean> room : openedRooms.entrySet()) {
            if (!room.getValue())
                return false;
        }
        
        return true;
    }
}