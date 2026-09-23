class Solution {
    public int largestAltitude(int[] gain) {
        
        int n = gain.length;


        int[] arr = new int[n+1];
        arr[0] = 0;
        arr[1] = arr[0]+gain[0];
        int max_value = Integer.MIN_VALUE;

        for(int i=2; i<n+1; i++){

            arr[i] = arr[i-1] + gain[i-1];

            
        }

        for(int i=0; i<n+1; i++){
            if(arr[i] > max_value){
                max_value = arr[i];
            }

        }

        return max_value;

    }
}