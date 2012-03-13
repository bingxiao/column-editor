#!/usr/bin/env python


import sys
from optparse import OptionParser
usage = '''
Method 1: hjoin.py -a [n1] -b [n2] [file1] [file2]
Method 2: hjoin.py [file1]/[n1] [file2]/[n2]
Note: the input files must ALWAYS be deliminated by TABs.
'''

parser = OptionParser( usage )
parser.add_option( "-a", "--a", dest='col1', help='by which column in file 1. A number' )
parser.add_option( "-b", "--b", dest='col2', help='by which column in file 2. A number' )
parser.add_option( "-r", "--reverse", action="store_true", dest="reverse", default=False, help="Substract B file from A file instead of really JOIN.")
#parser.add_option( "-v", "--verbose", action="store_true", dest="verbose", default=False, help="Verbose output A file.")
( options, args ) = parser.parse_args()

try:
    if options.col1 == None and options.col2 == None:
        a, b = args[:2]
        in_file, col1 = a.rsplit( '/', 1 )
        db_file, col2 = b.rsplit( '/', 1 )
        col1, col2 = int( col1 ), int( col2 )
    elif len( args ) !=2 or not (options.col1 and options.col2):
        print >>sys.stderr, options.col1, options.col2
        print >>sys.stderr, 'Illegal arguments.' 
        exit( 1 )
    else:
        in_file, db_file = args[:2]
        col2 = int( options.col2 )
        col1 = int( options.col1 )
except:
    print >>sys.stderr, 'Parsing argument failed.'
    parser.print_help()
    exit( 0 )
    
flag_dup = False
db = {}

if db_file == '-': handler = sys.stdin
else: handler = open( db_file )

for line in handler:
    if line.startswith( '#' ): continue
    items = line.strip( '\n\r' ).split( '\t' )
    key = items[ col2 - 1 ]
    if key in db:
        flag_dup = True
    db[ key ] = items

handler.close()


if in_file == '-': handler = sys.stdin
else: handler = open( in_file )

for line in handler:
    if line.startswith( '#' ): continue
    items = line.strip( '\n\r' ).split( '\t' )
    key = items[ col1 - 1 ]
    if options.reverse:
        if key not in db:
            print '\t'.join( items )
    else:
        if key in db:
            print '\t'.join( items + db[ key ] )

handler.close()


if flag_dup:
    print >>sys.stderr, '## ALERT( At least one duplication in db_file:<%s>. The last value was taken. )'%db_file

