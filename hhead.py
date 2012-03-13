#!/usr/bin/env python

# just show file columns by numbering.

import sys,os



if not sys.stdin.isatty():
    if len( sys.argv ) > 1: print >>sys.stderr, 'Note that hcol ONLY handle <stdin> or only 1 file at once!'
    handler = sys.stdin
elif sys.argv[ 1 ] == '-':
    if len( sys.argv ) > 2: print >>sys.stderr, 'Note that hcol ONLY handle <stdin> or only 1 file at once!'
    handler = sys.stdin
elif not os.path.isfile( sys.argv[ 1 ] ):
    print >>sys.stderr, 'File does not exist: <%s>'%sys.argv[ 1 ]
    exit( 0 )
else:
    if len( sys.argv ) > 2: print >>sys.stderr, 'Note that hcol ONLY handle <stdin> or only 1 file at once!'
    argv = sys.argv[ 1 ]
    fn = argv
    handler = open( fn )

table = []

for n, line in enumerate( handler ):
    if line.startswith( '#' ) or not line.strip():
        continue
    items = line.strip( '\n\r' ).split( '\t' )
    table.append( items )
    if n == 5:                      # only view first <n> lines.
        break

handler.close()

ncol = len( table[ 0 ] )
for n in xrange( ncol ):
    print '%s: '%(n+1), (', '.join( [ j[n] for j in table ] ) + '...' ).ljust( 80 )
