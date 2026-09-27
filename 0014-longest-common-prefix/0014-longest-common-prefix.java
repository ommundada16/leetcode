class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int n = strs.length;

        if(strs.length == 0){
            return "";
        }

        String res = "";

        for(int i=0 ; i <strs[0].length();i++){

            char ch = strs[0].charAt(i);

            for(int j=1 ; j<n; j++){

                if(strs[j].length() == i || strs[j].charAt(i) != ch){
                    return res;
                }
            }

            res += ch;
        }
return res;
    }
}