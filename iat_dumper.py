#!/usr/bin/env python
#Simple script to dump IAT's.
#something used, something borrowed. https://code.google.com/p/pefile/wiki/UsageExamples
#PhG

import sys, pefile
print "IAT for file: " + (sys.argv[1]) + "\n"
pe = pefile.PE(sys.argv[1])
pe.parse_data_directories()

for entry in pe.DIRECTORY_ENTRY_IMPORT:
  print entry.dll
  for imp in entry.imports:
    print '\t', hex(imp.address), imp.name
