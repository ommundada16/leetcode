class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String,List<String>> map = new HashMap<>();

        for(String str : strs){

            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted_word = new String(chars);


            if(!map.containsKey(sorted_word)){
                map.put(sorted_word, new ArrayList<>());
            }

            map.get(sorted_word).add(str);
        }

        List<List<String>> result = new ArrayList<>();

        for(List<String> anagram : map.values()){

            result.add(anagram);

        }

        return result;

    }
}