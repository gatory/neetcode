class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> arr = new HashSet<>();
        for (int num : nums) {
            if (arr.contains(num)) {
                return true;
            }
            arr.add(num);
        }
        return false;
    }
}
