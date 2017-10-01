"""
Copyright (C) 2017  Richard Möhn <richard.moehn+p2j@posteo.de>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

# Credits: https://github.com/amarack/python-rl/blob/master/pyrl/environments/pomdp.py

import sys

import numpy as np
from scipy import sparse

import libpomdp

def run(pomdp_path, json_path):
    if not libpomdp.readMDP(pomdp_path):
        raise RuntimeError("POMDP file invalid or not found at %s" % pomdp_path)

    initial_belief = libpomdp.getInitialBelief()
    print initial_belief

    O = map(lambda k: buildSparseMatrix(
                            k,
                            (libpomdp.getNumStates(),
                             libpomdp.getNumObservations())),
                 libpomdp.getSparseObsMatrix())
    print np.array(O)
    # This gives us |A| x |S| x |O|
    #                at   st+1  ot+1.

    P = map(lambda k: buildSparseMatrix(
                            k,
                            (libpomdp.getNumStates(), libpomdp.getNumStates())),
                 libpomdp.getSparseTransitionMatrix())
    print np.array(P)
    # This gives us |A| x |S| x |S|
    #                a     s     s'.


    # Want also |S| x |A|
    #            s     a  - Reward for taking action a in state s.


def buildSparseMatrix(rcd, shape): # row col data
    return sparse.csr_matrix((rcd[2], (rcd[0],rcd[1])), shape=shape).todense()


run(sys.argv[1], sys.argv[2])
