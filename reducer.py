# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:43:00 2017

@author: Sushidhar
"""

#!/usr/bin/env python

import sys
dict = {}
for line in sys.stdin:
    words = line.strip().split('\t')
    if len(words) == 2:
        word = words[0]
        dict.setdefault(word,{})
        filename = words[1].split(':')[0]
        count = int(words[1].split(':')[1])
        dict[word].setdefault(filename,0)
        dict[word][filename] += count
for key in dict:
    print '%s\t%s'%(key,dict[key].keys())