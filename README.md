pomdp2json
==========

This is a converter from Anthony Cassandra's (Tony's) **[POMDP File
Format](http://www.pomdp.org/code/pomdp-file-spec.html) to JSON**. I've spent an
entire morning (my mornings are long) trying to load a POMDP file into Python.
The existing tools are incomplete or hidden in large repositories or give me
compilation headaches. I don't want anyone else to have to spend an entire
morning, so I'm writing this tool that gives you a JSON file that can be read
easily from most programming environments.

Note that this program will also be incomplete, but in a better way. Given a
POMDP file, it will produce a JSON file with the following contents:

 - Discount factor: `number`
 - Initial belief: `|S|: [s]`
 - Transition probability matrix: `|S| x |A| x |S|: [st, at, st+1]`
 - Observation probability matrix: `|A| x |S| x |O|: [at, st+1, ot+1]`
 - Reward matrix: `|S| x |A|: [st, at]`

Where is it **incomplete**? The POMDP format allows the **reward** to depend on
action, state before action, state after action and observation. I leave out the
dependency on state after action and observation, because I don't need it. It
will be easy to add later if anyone needs it.


Compiling
---------

    $ cat build.sh  # See that it's small and benign.
    $ ./build.sh

You might need to **install** development tools like CMake or gcc before you can
compile. **Let me know if you have any difficulties.**


Usage
-----

    $ python pomdp2json.py <in>.POMDP <out>.POMDP.json


Based on: pyrl.environments.libPOMDP
------------------------------------

I'm reusing a Python interface and compilation setup from Will Dabney's
[python-rl](https://github.com/amarack/python-rl). All files except
`pomdp2json.py` stem from the directory
[libPOMDP](https://github.com/amarack/python-rl/tree/a1c1f5bc42cb20f5d9630818d1908f2100916ef4/pyrl/environments/libPOMDP).
Here is Will's description:

> This is primarily code from pomdp-solve written by Anthony R. Cassandra. I've only added a
> new makefile, which is not as sophisticated as the original, and some code to allow the whole thing
> to be compiled into a Python module.
>
> At present this only contains the code relevant for reading and writing the MDP/POMDP specification
> files, and interacting with the information contained within them. However, pomdp-solve itself
> has many useful implementations in pure C that may later be brought into this module for use in python.
>
> This has been tested on Mac OS X, but 'should' also work in Linux.


Exception about rewards
-----------------------

As noted before, pomdp2json does not deal with POMDP files that specify the
rewards to depend on more than action and state before action. If an input POMDP
doesn't stick to that, pomdp2json will raise an exception.

What can you do? In general, there is no easy way to convert a POMDP with a
R(st, at, st+1, ot+1) reward function to a POMDP with a R(st, at) reward
function. There might be a sophisticated way that I don't know. But there are
also easy cases where you can **fiddle with the original POMDP file**. For
example, `hallway.POMDP` defines this reward function:

```
# Rewards
# (R: <action> : <start-state> : <end-state> : <observation> %f)
R: * : * : 56 : * 1.000000
R: * : * : 57 : * 1.000000
R: * : * : 58 : * 1.000000
R: * : * : 59 : * 1.000000
```

If you swap columns like this…

```
R: * : 56 : * : * 1.000000
R: * : 57 : * : * 1.000000
R: * : 58 : * : * 1.000000
R: * : 59 : * : * 1.000000
```

…then the POMDP (file) will be compatible with pomdp2json and in turn with tools
like [piglet_pbvi](https://github.com/rmoehn/piglet_pbvi). Is it the **same
POMDP as the original?** Maybe not. But I guess it's almost the same.


To do
-----

- Maybe add automatic downloading and unpacking of POMDP files.
- Maybe unify documentation (reStructuredText) and add usage information to
  `pomdp2json.py`.


LICENSE
-------

Anthony Cassandra's original code for pomdp-solve includes a `COPYING` file with
the text of the GNU General Public License, Version 2. Therefore, I assume that
that license applies to the POMDP file reading code and I release pomdp2json
under the same license.
