#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:46:43 2020

@author: halowin
"""

import re
DNA = 'TAGCATCGGCATTACTGAC'
print(str(round(len(re.findall(r'G|C',DNA))/len(DNA)*100,2))+'%')
