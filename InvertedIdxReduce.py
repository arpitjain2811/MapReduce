#!/usr/bin/env python

import sys
from collections import defaultdict

inverted_idx = defaultdict(list)

for line in sys.stdin:
    key, doc_num, count = line.strip().split("\t")
    inverted_idx[key].append((int(doc_num),int(count)))

words = sorted(inverted_idx, key=inverted_idx.get, reverse=True)

for word in words:
    idx = inverted_idx[word]
    idx = sorted(idx, key = lambda t:(t[1],t[0]))
    print '%s\t' % (word),
    for i in range(0,len(idx)):
        if i<len(idx)-1:
            print '%04d %d,' % (idx[i][0], idx[i][1]),
        else:
            print '%04d %d' % (idx[i][0], idx[i][1]),
        
    print ''    
