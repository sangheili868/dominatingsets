#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    Copyright (C) 2012 Axel "0vercl0k" Souchet - http://www.twitter.com/0vercl0k
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import time
import pygraphviz as pgv
from z3 import *

#Contributed by @cbrewbs chad@dataculture.co
#Requires z3 >= 4.4.1 
def min_dom_set(graph):
    """Try to dominate the graph with the least number of verticies possible"""
    s = Optimize()
    nodes_colors = dict((node_name, Int('k%r' % node_name)) for node_name in graph.nodes())
    for node in graph.nodes():
           s.add(And(nodes_colors[node] >= 0, nodes_colors[node] <= 1)) # dominator or not
           dom_neighbor = Sum ([ (nodes_colors[j]) for j in graph.neighbors(node) ])
           s.add(Sum(nodes_colors[node], dom_neighbor ) >= 1 )
    s.minimize( Sum([ nodes_colors[y] for y in graph.nodes() ]) )

    if s.check() == sat:
        m = s.model()
        return dict((name, m[color].as_long()) for name, color in nodes_colors.iteritems())
    
    raise Exception('Could not find a solution.')

def build_fat_graph():
    """Build http://www.graphviz.org/content/twopi2"""
    G = pgv.AGraph('../networks/airport.gv')
    return (G, 'network', 'twopi')

def main(argc, argv):
    print 'Building the graph..'

    Gs = [
        build_fat_graph()
    ]

    for G, name, layout in Gs:
        print 'Trying to find min dom set for %s now (%d nodes, %d edges)..' % (repr(name), G.number_of_nodes(), G.number_of_edges())
        t1 = time.clock()
        s = min_dom_set(G)
        t2 = time.clock()

        print 'OK, found a solution with %d dominators (in %fs)' % (sum(s.values()), (t2 - t1))
        fd = open('dom_set.txt', 'w')
	for node in s:
		fd.write(str(node) + ',')

    return 1

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
