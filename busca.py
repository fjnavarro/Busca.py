#!/usr/bin/env python
import commands
import sys
"Busca in python"
numberParams=len(sys.argv)
if(numberParams>1):
    findTxt='find . -type f'
    if(numberParams>2):
        findTxt+='|egrep "'
        for i in range(len(sys.argv)):
            if(i>1):
                findTxt+='\.'+sys.argv[i]
                if(i+1<numberParams):
                    findTxt+='|'
        findTxt+='"'
    find=commands.getoutput(findTxt)
    if(len(find)>1):
        for value in find.split('n'):
            value2=commands.getoutput('grep -nHi "'+sys.argv[1]+'" '+value)
            if value2!='':
                print value2
    else:
        print "no results"
else:
    print "Please, busca.py 'searchString' [typeFile typeFile ...]"
