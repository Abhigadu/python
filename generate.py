#!/usr/bin/env python3

import random
import sys

defined_char = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%<>{}[]'

#desired_pass = ''

def generate(length):
    desired_pass = ''
    for i in range(int(length)):
        desired_pass += random.choice(defined_char)
    print(desired_pass)

if not len(sys.argv) > 1:
    generate(12)
else:
    generate(sys.argv[1])

# generate(12)

# print(len(sys.argv))