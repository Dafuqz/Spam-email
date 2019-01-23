import os

path = 'ham'
listing = os.listdir(path)
for infile in listing:
    print "current file is: " + infile