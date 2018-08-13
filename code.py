import math
import os
import random
import re
import sys
import collections
import time

def textQueries(sentences, queries):
    #code optimized by splitting operations reducing processing in triple loop
    
    sLen = len(sentences) # Number of sentences
    qLen = len(queries)   # Number of query strings
    sDict = {} # dict of sentence word counters {sentence#:[word1:count, word2:count]...}
    qDict = {} # dict of query word counters {query#:[word1:count, word2:count]...}
    
    # generate counter data
    for s in range(0, sLen):
        counter = collections.Counter()
        for w in sentences[s].split():
            counter[w] += 1
        sDict[s] = counter
    for q in range(0, qLen):
        counter = collections.Counter()
        for w in queries[q].split():
            counter[w] += 1
        qDict[q] = counter

    # process/print data   
    for q in range(0, qLen):
        found = False
        for s in range(0, sLen):
            count = 0
            rem = collections.Counter()
            rem = sDict[s].copy()
            
            while len(qDict[q]) is len(rem & qDict[q]):
                rem -= qDict[q]
                count += 1
            if count > 0:
                sys.stdout.write((str(s) + " ") * count)
                found = True
                
        if not found:
            print("-1")
        else:
            print("")
                             
    print("Time: ", time.clock(), "ms")




if __name__ == '__main__':
    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    textQueries(sentences, queries)
