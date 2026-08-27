#!/usr/bin/env python3
"""URLReducer.py"""
import sys

COUNT_THRESHOLD = 5
current_url = None
current_count = 0

def emit(url, count):
    if count > COUNT_THRESHOLD:
        print('%s\t%s' % (url, count))

for line in sys.stdin:
    line = line.strip()
    try:
        url, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue

    if url == current_url:
        current_count += count
    else:
        if current_url is not None:
            emit(current_url, current_count)
        current_url = url
        current_count = count

if current_url is not None:
    emit(current_url, current_count)
