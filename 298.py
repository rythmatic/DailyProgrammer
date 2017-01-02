#!/usr/bin/env python

# Removes unnecessary parentheses from an expression.
# Challenge link: https://www.reddit.com/r/dailyprogrammer/comments/5llkbj 
import sys

expr = sys.stdin.readline().strip('\n')
pairs = []
for i, char in enumerate(expr):
    if char == '(':
        pairs.append([i, -1])
    elif char == ')':
        k = -1
        while pairs[k][1] != -1:
            k -= 1
        pairs[k][1] = i

filter_list = []
for i in range(len(pairs)):
    if i < len(pairs) - 1:
        if (pairs[i][0] == pairs[i + 1][0] - 1 and pairs[i][1] == pairs[i + 1][1] + 1):
            filter_list += pairs[i]
    if pairs[i][0] == pairs[i][1] - 1: 
        filter_list += pairs[i]

result = [expr[i] for i in range(len(expr)) if i not in filter_list]
print(''.join(result))
