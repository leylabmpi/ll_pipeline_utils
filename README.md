ll_pipeline_utils
=================

Boilerplate code used by all/most of the Ley Lab snakemake pipelines

The repo acts as a "submodule" in the git repos of each pipeline.
Submodules are repos inside other repos that can be updated separately
from the main (parent) repo.

# How to update this submodule in an existing pipeline

```
cd /path/to/PIPELINE/
git submodule update --init --recursive
```

# How to add this submodule to an existing pipeline repository

```
cd /path/to/PIPELINE/
cd bin/
git submodule add git@gitlab.tuebingen.mpg.de:leylabmpi/pipelines/ll_pipeline_utils.git
```

