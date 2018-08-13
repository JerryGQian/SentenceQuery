    // Complete the textQueries function below.
    static void textQueries(List<String> sentences, List<String> queries) {   
        List<HashMap<String, Integer>> sHash = new ArrayList<>();
        List<String[]> qArr = new ArrayList<>();
        
        //Cache query words in list of arrays
        for (int q = 0; q < queries.size(); q++) {
            qArr.add(queries.get(q).split(" "));
        }
        
        //Cache sentences words in a counter hashmap
        for (int s = 0; s < sentences.size(); s++) {
            HashMap<String, Integer> hash = new HashMap<>();
            for (String w : sentences.get(s).split(" ")) {
                if (hash.containsKey(w))
                    hash.put(w, hash.get(w)+1);
                else
                    hash.put(w, 1);
            }
            sHash.add(hash);
        }
        
        //Calculations and printing
        for (String[] q : qArr) {
            boolean found = false;

            for (int s = 0; s < sentences.size(); s++) {
                int lowest = 10; //tracks lowest count found word for printing

                for (String word : q) {
                    int count = 0;
                    
                    if (sHash.get(s).containsKey(word)) {
                        count = sHash.get(s).get(word);
                        if (count < lowest)
                            lowest = count;
                    }
                    else {
                        lowest = 0;
                        break;
                    }
                }
                
                for (int i = 0; i < lowest; i++) {
                    System.out.print(s + " ");
                    found = true;
                }

            }
            if (!found) 
                System.out.print("-1");
            System.out.println();
        }
    }
