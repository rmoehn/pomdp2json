pomdp2json
==========

**Note** Program and documentation are not finished yet. I expect to finish it
by 2017-10-06.

This is a converter from Anthony Cassandra's (Tony's) [POMDP File
Format](http://www.pomdp.org/code/pomdp-file-spec.html) to JSON. I've spent an
entire morning (my mornings are long) trying to load a POMDP files into Python.
The existing tools are incomplete or hidden in large repositories or give me
compilation headaches. I don't want anyone else to have to spend an entire
morning, so I'm writing this tool that gives you a JSON file that can be read
easily from most programming environments.

Note that this program will also be incomplete, but in a better way. Given a
POMDP file, it will produce a JSON file with the following contents:

 - Discount factor: `number`
 - Initial belief: `[number]`
 - Transition probability matrix: `|S| x |A| x |S|: [st, at, st+1]`
 - Observation probability matrix: `|A| x |S| x |O|: [at, at+1, ot+1]`
 - Reward matrix: `|S| x |A|: [st, at]`

Where is it incomplete? The POMDP format allows the reward to depend on action,
start state, end state and observation. I leave out the dependency on end state
and observation, because I don't need it. It will be easy to add later if anyone
needs it.


Based on: pyrl.environments.libPOMDP
------------------------------------

I'm reusing a Python interface and compilation setup from Will Dabney's
[python-rl](https://github.com/amarack/python-rl). All files except
`pomdp2json.py` stem from the directory
[libPOMDP](https://github.com/amarack/python-rl/tree/a1c1f5bc42cb20f5d9630818d1908f2100916ef4/pyrl/environments/libPOMDP)
. Here's Will's description:

> This is primarily code from pomdp-solve written by Anthony R. Cassandra. I've only added a
> new makefile, which is not as sophisticated as the original, and some code to allow the whole thing
> to be compiled into a Python module.
>
> At present this only contains the code relevant for reading and writing the MDP/POMDP specification
> files, and interacting with the information contained within them. However, pomdp-solve itself
> has many useful implementations in pure C that may later be brought into this module for use in python.
>
> This has been tested on Mac OS X, but 'should' also work in Linux.


LICENSE
-------

Anthony Cassandra's original code for pomdp-solve included a `COPYING` file with
the text of the GNU General Public License, Version 2. Therefore, I assume that
that license applies to the POMDP file reading code and I release pomdp2json
under the same license.
