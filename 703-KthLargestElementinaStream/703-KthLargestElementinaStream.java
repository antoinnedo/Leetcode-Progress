class KthLargest {
    private PriorityQueue<Integer> minHeap;
    private int k;

    // Constructor to initialize k and add elements from nums to the heap
    public KthLargest(int k, int[] nums) {
        this.k = k;
        minHeap = new PriorityQueue<>(k); // Min-Heap to store the k largest elements

        // Add elements from the initial array to the heap
        for (int num : nums) {
            add(num); // Use the add method to ensure heap properties are maintained
        }
    }

    // Method to add a new score and return the kth largest score
    public int add(int val) {
        // Add the new score if the heap size is less than k
        if (minHeap.size() < k) {
            minHeap.offer(val); // Directly add if the heap is not full
        } 
        // If the new score is larger than the smallest in the heap, replace it
        else if (val > minHeap.peek()) {
            minHeap.poll(); // Remove the smallest
            minHeap.offer(val); // Add the new larger value
        }
        
        // Return the kth largest element (the root of the min-heap)
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */