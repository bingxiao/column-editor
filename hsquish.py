#!/usr/bin/env python

## compress specific column of a file. Note that there's no other purpose, such as unique other lines.

import sys, os
from collections import defaultdict

try:
    fn, columns_str = sys.argv[ 1 ].rsplit( '/', 1 )
except:
    print """Usage: hsquish.py [file|-]/[col] """
    exit()


COL = int( columns_str )
DELIM = '|'

if fn == '-':
    handler = sys.stdin
elif not os.path.isfile( fn ):
    print >>sys.stderr, 'File does not exist: <%s>'%fn
    exit( 0 )
else:
    handler = open( fn )
    

dic = defaultdict( list )
for line in handler:
    if line.startswith( '#' ) or not line.strip():
        #print line.strip( '\n\r' )  # no change to the comment line.
        continue
    items = line.strip( '\n\r' ).split( '\t' )
    key = '\t'.join( [ items[ i ] for i in xrange( 0, len( items ) ) if i != (COL-1) ] )
    dic[ key ].append( items[ COL -1 ] )
    
for key, value in dic.iteritems():
    items = key.split( '\t' )
    items.insert( DOL-1, DELIM.join( value ) )
    print '\t'.join( items )

