#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

"""
Copyright (C) 2017  Richard Möhn <richard.moehn+p2j@posteo.de>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, version 2.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

 * * * * *

Usage:

    $ python pomdp2json.py <in>.POMDP <out>.POMDP.json
"""

# Credits: https://github.com/amarack/python-rl/blob/master/pyrl/environments/pomdp.py

import collections
import json
import sys

import numpy as np
from scipy import sparse

import libpomdp


# Credits: https://github.com/amarack/python-rl/blob/master/pyrl/environments/pomdp.py
def buildSparseMatrix(rcd, shape):  # rcd = row col data
    return sparse.csr_matrix((rcd[2], (rcd[0], rcd[1])), shape=shape).todense()


def transition_matrix(alibpomdp):
    return np.array([buildSparseMatrix(k, (alibpomdp.getNumStates(),
                                           alibpomdp.getNumStates()))
                     for k in libpomdp.getSparseTransitionMatrix()])


def observation_matrix(alibpomdp):
    return np.array([buildSparseMatrix(k, (alibpomdp.getNumStates(),
                                           alibpomdp.getNumObservations()))
                     for k in libpomdp.getSparseObsMatrix()])


def reward_matrix(alibpomdp):
    return np.array([[alibpomdp.getReward(s, a, 0, 0)
                      for a in xrange(alibpomdp.getNumActions())]
                     for s in xrange(alibpomdp.getNumStates())])


def pyify(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    else:
        return o


def run(pomdp_path, json_path):
    if not libpomdp.readMDP(pomdp_path):
        raise RuntimeError("POMDP file invalid or not found at %s" % pomdp_path)

    pomdp = collections.OrderedDict([
        ('initial_belief',       libpomdp.getInitialBelief()),
        ('transition_matrix',    transition_matrix(libpomdp)),
        ('observation_matrix',   observation_matrix(libpomdp)),
        ('reward_matrix',        reward_matrix(libpomdp)),
        ('discount_factor',      libpomdp.getDiscount())
    ])

    with open(json_path, 'w') as f:
        json.dump(collections.OrderedDict((k, pyify(v))
                                          for k, v in pomdp.items()),
                  f,
                  indent=4)


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
