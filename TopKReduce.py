#!/usr/bin/env python

import sys
from collections import defaultdict

k=100
cur_key = None
cur_count = 0
global_count = defaultdict(int)
for line in sys.stdin:
    key, value = line.split()
    if key == cur_key:
        cur_count += int(value)
    else:
        if cur_key:
        	global_count[cur_key] = cur_count
        cur_key = key
        cur_count = int(value)

global_count[cur_key] = cur_count
top_keys_global = sorted(global_count, key=global_count.get, reverse=True)
for key in top_keys_global[:min(k,len(top_keys_global))]:
	print '%s\t%s' % (key, global_count[key])