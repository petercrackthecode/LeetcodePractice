// link: https://leetcode.com/problems/k-closest-points-to-origin/

class Key {

    private final int x;
    private final int y;

    public Key(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Key)) return false;
        Key key = (Key) o;
        return x == key.x && y == key.y;
    }
    
    @Override
    public int hashCode() {
        int result = x;
        result = 31 * result + y;
        return result;
    }
}


class Solution {
    /*
        1. Save each pair of points into a map of <point, distance to origin>
        2. Sort the array of points ascendingly based on their value (distance) in the map.
        3. Return the first K elements in the array.
    */
    
    private Integer[][] toObjectArray(int[][] arr) {
        Integer[][] objectArr = new Integer[arr.length][arr[0].length];
        for (int index = 0; index < arr.length; ++index)
            for (int j = 0; j < arr[0].length; ++j)
                objectArr[index][j] = arr[index][j];
        
        return objectArr;
    }
    
    private int[][] toPrimitiveArray(Integer[][] arr) {
        int[][] objectArr = new int[arr.length][arr[0].length];
        for (int index = 0; index < arr.length; ++index)
            for (int j = 0; j < arr[0].length; ++j)
                objectArr[index][j] = arr[index][j];
        
        return objectArr;
    }
    
    private Double getDistance(Integer point[]) {
        return Math.sqrt(point[0] * point[0] + point[1] * point[1]);
    }
    
    public int[][] kClosest(int[][] points, int K) {
        HashMap<Key, Double> pointToDistance = new HashMap<Key, Double>();
        
        Integer[][] IntegerPoints = toObjectArray(points);
        
        for (Integer[] point : IntegerPoints) {
            pointToDistance.put(new Key(point[0], point[1]), getDistance(point));
        }
        
        Arrays.sort(IntegerPoints, new Comparator<Integer[]>() {
            public int compare(Integer[] a, Integer[] b) {
                return pointToDistance.get(new Key(a[0], a[1])).compareTo(pointToDistance.get(new Key(b[0], b[1])));
            }
        });
        
        return Arrays.copyOf(toPrimitiveArray(IntegerPoints), K);
    }
}