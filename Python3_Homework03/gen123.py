"""
gen123.py: generate sequences from a base list, repeating
           each element one more time than the last 
"""

def gen123(m):
    n = 0
    for item in m:
        n += 1
        for i in range(n):
            yield item
