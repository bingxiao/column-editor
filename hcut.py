#!/usr/bin/env python

# In the future:
# 1. consider multiple files. Joinning files with the same rows.
# 2. consider parsing standard input.

import sys, os

def parse_segment( columns_str, columns_max ):
    NF = columns_max                    # 1 based.
    stack = []
    for segment in columns_str.split( ',' ):
        if '-' in segment:
            a, b = segment.split( '-' )
            a = int( a ) if a != '' else 1  
            b = int( b ) if b != '' else NF
            stack.extend( range( a-1, b ) )
        else:
            if segment != '':
                stack.append( int( segment )-1 )
    # print stack                             # note that after parsing, numbers are converted to 0-based.
    return stack


if len( sys.argv ) == 1:
    print 'Show usage:'
    exit( 0 )


argv = sys.argv[ 1 ]
fn, columns_str = argv.rsplit( '/', 1 )

if fn == '-':
    handler = sys.stdin
elif not os.path.isfile( fn ):
    print >>sys.stderr, 'File does not exist: <%s>'%fn
    exit( 0 )
else:
    handler = open( fn )
    
# print argv
# print fn, columns_str


flag_diffField = False

segment_stack = None
for line in handler:
    if line.startswith( '#' ) or not line.strip():
        print line.strip( '\n\r' )  # keep the comment lines.
        continue
    items = line.strip( '\n\r' ).split( '\t' )
    if segment_stack == None:
        max_col = len( items )
        segment_stack = parse_segment( columns_str, max_col )
    else:                           # just check column numbers are the same.
        if max_col != len( items ):
            flag_diffField = True
    rearranged_items = [ items[i] for i in segment_stack ]
    print '\t'.join( rearranged_items )

handler.close()

if flag_diffField:
    print >>sys.stderr,  "NF consistency. Numbers of columns for <%s> should be: <%d>"%( fn, max_col )
