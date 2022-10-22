# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:50:05 2022

@author: Aftab Mallick
"""

import powerset as ps
s1={1,2,3,4}
s2={3,4,5,6}
o1=ps.PowerSet(s1)
o2=ps.PowerSet(s2)
o1+o2
o1*o2
o1-o2