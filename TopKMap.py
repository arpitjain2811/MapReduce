#!/usr/bin/python

import sys
import string
import re
from collections import defaultdict

k=100
# input comes from STDIN (stream data that goes to the program)
regex = re.compile('[%s0-9]' % re.escape(string.punctuation))
stop = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
local_count = defaultdict(int)
for line in sys.stdin:
    l = line.strip().split()
    for word in l:
        word = regex.sub('',word)
        # output goes to STDOUT (stream data that the program writes)
        if word not in stop and len(word)==7:
        	local_count[word] += 1

top_keys = sorted(local_count, key=local_count.get, reverse=True)
for key in top_keys[:max(k,len(top_keys))]:
	print "%s\t%d" %( key, local_count[key] )