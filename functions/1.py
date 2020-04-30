#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:46:43 2020

@author: halowin
"""

import re
DNA = 'TAGCATCGGCATTACTGAC'
x = re.findall(r'G',DNA)
y = re.findall(r'C',DNA)
z =((len(x)+len(y))/len(DNA)*100)
w = ('%.2f' % z)
print (str(w)+'%')
