#!/bin/python

import argparse

print "Sample Argument Parser code"

parser = argparse.ArgumentParser()
#parser.add_argument('-f', '--my-foo', default='foobar')
#parser.add_argument('-b', '--bar-value', default=3.14)
parser.add_argument('-f', '--foo', default='foobar',help='this is arg 1',required=True)
parser.add_argument('-b', '--value', default=3.14,help='this is arg 2')
#args = parser.parse_args()       # values accessed as args.foo and args.value
args = vars(parser.parse_args())  # creates a dictionary of args

#print args.my_foo
#print args.bar_value
#print args.foo
#print args.value
print args['foo']
print args['value']
