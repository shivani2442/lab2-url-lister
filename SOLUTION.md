# Lab 2 - URLCount

## Solution

I converted the provided Hadoop WordCount application into a URLCount
application using Hadoop Streaming and Python.

`URLMapper.py` reads the input HTML files and extracts values from
`href="..."` attributes, emitting each URL with a count of 1.

`URLReducer.py` aggregates the counts for each URL and outputs only
URLs whose count is greater than 5.

The solution was developed and tested on CSEL and was also run on
Google Cloud Dataproc for the required performance comparison.

## Dataproc Performance

The same input and URLCount job were run on clusters with 2 and 4
worker nodes.

| Cluster | Worker Nodes | Execution Time |
|---|---:|---:|
| 2-worker | 2 | 68.354 seconds |
| 4-worker | 4 | 52.188 seconds |

Increasing the number of workers from 2 to 4 reduced the execution
time by 16.166 seconds, giving approximately a 23.65% improvement
and a 1.31x speedup.

The improvement was less than 2x because Hadoop has fixed overhead
from job setup, task scheduling, shuffle/sort, and communication
between nodes. The input dataset is also relatively small.

## Resources

I used the course-provided Lab 2 repository and README, Hadoop
Streaming documentation, and the Google Cloud Dataproc lab for the
performance experiment.
