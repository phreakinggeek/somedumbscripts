#!/usr/bin/env python
#ssdeep massive comparision engine (fancy way of saying... shitty script)
#there's no reason to do this... idk wtf I was doing. This makes no sense. Broken.

import sys
import pydeep
pd0 = pydeep.hash_file(sys.argv[1])
pd1 = sys.argv[2]
#Import our ssdeep file.
def deepImp(pd1) :
                deepDict = []
                with open(pd1, 'r') as deepFiles:
                    for row in deepFiles:
                        deepDict.append(row[1])
                return ssdeepDir
deepImpList = deepImp(pd1)
x = str(pydeep.compare(pd0, pd1))
print "SSDeep has determined that the DeepImportHash between" + (sys.argv[1]) + " and " + deepImpList + " are " + x +"% alike."