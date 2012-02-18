#!/usr/bin/env python

# just show file columns by numbering.

import sys
argv = sys.argv[ 1 ]

fn = argv

table = []
with open( fn ) as handler:
    for n, line in enumerate( handler ):
        if line.startswith( '#' ) or not line.strip():
            continue
        items = line.strip( '\n\r' ).split( '\t' )
        table.append( items )
        if n == 5:                      # only view first <n> lines.
            break

ncol = len( table[ 0 ] )
for n in xrange( ncol ):
    print '%s: '%(n+1), (', '.join( [ j[n] for j in table ] ) + '...' ).ljust( 80 )
