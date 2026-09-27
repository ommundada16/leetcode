class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int min_price = Integer.MAX_VALUE;
        
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min_price) {
                // Update the lowest price seen so far
                min_price = prices[i];
            } else if (prices[i] - min_price > max_profit) {
                // Update max profit if selling today is better
                max_profit = prices[i] - min_price;
            }
        }
        
        return max_profit;
    }
}