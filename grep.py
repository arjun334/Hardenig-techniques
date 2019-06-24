#!/usr/bin/env python
import os
import platform
import subprocess
import sys
import re
import glob

print "\n--------------------------------------------------.........."
print "[+]Executing Python Code For Finding Hardening Techniques "
print "----------------------------------------------------..........."



def check(pattern):
    for folder, subs, files in os.walk(rootdir):
        #with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:

        #print folder
        for filename in files:
                #pSrint filename
                for pattern in file_list_1:
                    #print "looking for" + pattern "in" + filename
                    #with open(os.path.join(folder, filename), 'r') as src:
                    #print src.read()
                    for i, line in enumerate(open(os.path.join(folder, filename))):
                        for match in re.finditer(pattern, line):
                            print 'Found on line %s: %s pattern Found %s' % (i+1, filename,pattern)




dir_name = sys.argv[1]
print dir_name
rootdir = "/home/arjun/Desktop/apk2"
file_list_1 = ['/system/app/Superuser.apk', '/sbin/su', '/system/xbin/su', '/data/local/xbin/su', '/data/local/bin/su', '/system/sd/xbin/su', '/system/bin/failsafe/su', '/data/local/su', '/su/bin/su']
for pattern in file_list_1:
    check(pattern)

print "..............File Exsistence check is Ended................"

print "..............checking for runtime check ...................."

file_list_2 = ['/system/xbin/which', 'su','Runtime.getRuntime().exec']
for pattern in file_list_2:
    check(pattern)
