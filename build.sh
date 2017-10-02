#!/bin/bash

mkdir -p build
cd build

export ENV_NUMPY_INC=$(python2.7 <<'EOF'
import os.path
import numpy
print os.path.join(numpy.get_include(), "numpy")
EOF
)

cmake ..
make
