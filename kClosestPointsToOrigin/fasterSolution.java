// link: https://leetcode.com/problems/k-closest-points-to-origin/

class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> (b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]));
        // Store first K points in the maxHeap
        for (int i = 0; i < K; ++i) {
            maxHeap.add(points[i]);
        }
        /* for the rest of the points in input array, compare each point
           with the max value in maxHeap, if points[i] distance is smaller
           than maxHeap.peek() distance, remove the max point in maxHeap
           and add the points[i] in maxHeap.
        */
        for (int i = K; i < points.length; ++i) {
            int pDist = points[i][0] * points[i][0] + points[i][1]*points[i][1];
            int[] maxPoint = maxHeap.peek();
            int maxDist = maxPoint[0]*maxPoint[0] + maxPoint[1]*maxPoint[1];

            if (pDist < maxDist) {
                maxHeap.poll();
                maxHeap.add(points[i]);
            }
        }

        int[][] res = new int[K][2];

        for (int i = 0; i < K; ++i) {
            res[i] = maxHeap.remove();
        }

        return res;
    }
}