#!/bin/bash
export OMP_NUM_THREADS=1
# properties = {properties}

# exit on first error
set -o errexit
{exec_job}
