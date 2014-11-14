#!/usr/bin/env python
#Simple script to do IAT hashing and PE Section Hashing and pull the EP
#https://www.mandiant.com/blog/tracking-malware-import-hashing/ - Requires >= pefile 1.2.10-139
#PhG

import sys, pefile
pe = pefile.PE(sys.argv[1])
print "Hash information for : " + (sys.argv[1]) + "\n"
print "Import Hash : %s" % pe.get_imphash()
print
print "Section Names and Hashes:"
for section in pe.sections:
    print section.get_hash_md5() + " " + section.Name.rstrip('\0')
print
h = pe.OPTIONAL_HEADER.AddressOfEntryPoint
print "Entry Point : " + str(hex(h)).strip("'")
