#!/usr/bin/env python
#ssdeep insto hashin'! - since ssdeep is natively an unwieldy PITA.
#https://pypi.python.org/pypi/pydeep
#PhG

import sys, pydeep
pd1 = pydeep.hash_file(sys.argv[1])
pd2 = pydeep.hash_file(sys.argv[2])
percent = str(pydeep.compare(pd1, pd2))
print "SSDeep has determined that these files are " + percent +"% alike."

#pd0 = pydeep.hash_file("VirusShare_ab208f0b517ba9850f1551c9555b5313")
#pd1 = pydeep.hash_file("VirusShare_6570163cd34454b3d1476c134d44b9d9")
