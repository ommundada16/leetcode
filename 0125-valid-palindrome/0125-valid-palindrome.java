class Solution {
    public boolean isPalindrome(String s) {
        // Convert the whole string to lowercase first
        s = s.toLowerCase();
        
        int i = 0;
        int j = s.length() - 1;
        
        while (i < j) {
            char leftChar = s.charAt(i);
            char rightChar = s.charAt(j);
            
            // If the left character is not alphanumeric, skip it
            if (!Character.isLetterOrDigit(leftChar)) {
                i++;
            }
            // If the right character is not alphanumeric, skip it
            else if (!Character.isLetterOrDigit(rightChar)) {
                j--;
            }
            // If both are alphanumeric, compare them
            else {
                if (leftChar == rightChar) {
                    i++;
                    j--;
                } else {
                    return false; // Mismatch found
                }
            }
        }
        
        return true; // All characters matched
    }
}