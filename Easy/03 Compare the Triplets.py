'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If ai>bi, then Alice is awarded  point.
If bi>ai, then Bob is awarded  point.
If ai==bi, then neither person receives a point.
Comparison points is the total points a person earned.

Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

Sample Input

5 6 7
3 6 10
Sample Output

1 1 

'''


#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_score = ((1 if a0>b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0))
    bob_score = ((1 if b0>a0 else 0) + (1 if b1 > a1 else 0) + (1 if b2 > a2 else 0))
    print(alice_score,bob_score)
    # Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)