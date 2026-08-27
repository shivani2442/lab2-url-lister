#!/usr/bin/env python3
"""URLMapper.py"""
import sys
import re

HREF_PATTERN = re.compile(r'href="([^"]*)"')

for line in sys.stdin:
    line = line.strip()
    urls = HREF_PATTERN.findall(line)
    for url in urls:
        print('%s\t%s' % (url, 1))
