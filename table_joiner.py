#!/usr/bin/env python


import sys
from optparse import OptionParser
usage = 'Usage: $0 -a # -b # [file 1] [file 2] \nAlways deliminate by TAB.'
parser = OptionParser( usage )
parser.add_option( "-a", "--a", dest='col1', help='a number, which column in file 1' )
parser.add_option( "-b", "--b", dest='col2', help='a number, which column in file 2' )
(options, args) = parser.parse_args()


if len( args ) !=2 or not (options.col1 and options.col2):
    print usage
    print 'Illegal arguments.'
    print "opts:", options
    print "args:", args
    exit( 0 )

in_file, db_file = args[:2]
flag_dup = False

db = {}
col2 = int( options.col2 )
with open( db_file ) as handler:
    for line in handler:
        if line.startswith( '#' ): continue
        items = line.strip( '\n\r' ).split( '\t' )
        key = items[ col2 - 1 ]
        if key in db:
            flag_dup = True
        db[ key ] = items

col1 = int( options.col1 )
with open( in_file ) as handler:
    for line in handler:
        if line.startswith( '#' ): continue
        items = line.strip( '\n\r' ).split( '\t' )
        key = items[ col1 - 1 ]
        if key in db:
            print '\t'.join( items + db[ key ] )

if flag_dup:
    print >>sys.stderr, '## ALERT( Duplications in db_file:<%s>. Using the last value. )'%db_file
