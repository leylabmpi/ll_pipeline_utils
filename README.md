ll_pipeline_utils
=================

Boilerplate code used by all/most of the Ley Lab snakemake pipelines

The repo acts as a "submodule" in the git repos of each pipeline.
Submodules are repos inside other repos that can be updated separately
from the main (parent) repo.

The repo also includes [snakeamke profiles](https://github.com/Snakemake-Profiles)
for running snakemake on a cluster (SGE & SLURM currently supported). You do **NOT**
need to add the profile(s) to your `~/.config/snakemake/` directory! 

# How to update this submodule in an existing pipeline

```
cd /path/to/PIPELINE/
git submodule update --remote --init --recursive
```

# How to add this submodule to an existing pipeline repository

```
cd /path/to/PIPELINE/
cd bin/
git submodule add git@gitlab.tuebingen.mpg.de:leylabmpi/pipelines/ll_pipeline_utils.git
```

# How to clone a pipeline repo and include the updated submodule

```
git clone --recurse-submodules git@URL_OF_THE_PIPELINE_CHANGE_THIS
```

***

# Troubleshooting

If you get the following error:

```
Submodule 'bin/ll_pipeline_utils' (git@gitlab.tuebingen.mpg.de:leylabmpi/pipelines/ll_pipeline_utils.git) registered for path 'bin/ll_pipeline_utils'
Cloning into '/ebio/abt3_scratch/jsutter/llmgp/bin/ll_pipeline_utils'...
git@gitlab.tuebingen.mpg.de: Permission denied (publickey).
fatal: Could not read from remote repository.
```

...then you probably need to [add an ssh key to your GitLab account](https://docs.gitlab.com/ee/ssh/).
Basically, you just need to paste in the public ssh key from your `~/.ssh/id_rsa.pub` file that is in your home directory on `/ebio/`.
If you do not have a `~/.ssh/id_rsa.pub` file, then you need to create one (see the docs above).

NOTE: You may have to re-clone the parent repo (eg., `LLMGQC`) via the ssh url in order to fix the issue.

