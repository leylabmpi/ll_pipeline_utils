ll_pipeline_utils
=================

Boilerplate code used by all/most of the Ley Lab snakemake pipelines

* Version: 0.1.0
* Authors:
  * Nick Youngblut <nyoungb2@gmail.com>
* Maintainers:
  * Nick Youngblut <nyoungb2@gmail.com>

The repo acts as a "submodule" in the git repos of each pipeline.
Submodules are repos inside other repos that can be updated separately
from the main (parent) repo.

The repo also includes [snakemake profiles](https://github.com/Snakemake-Profiles)
for running snakemake on a cluster.  SGE & SLURM are currently supported, but
you may want to edit each, depending on your cluster setup. You do **NOT**
need to add the profile(s) to your `~/.config/snakemake/` directory! 

# Setup

## How to update this submodule in an existing pipeline

```
cd /path/to/PIPELINE/
git submodule update --remote --init --recursive
```

## How to add this submodule to an existing pipeline repository

```
cd /path/to/PIPELINE/
cd bin/
git submodule add git@gitlab.tuebingen.mpg.de:leylabmpi/pipelines/ll_pipeline_utils.git
git submodule update --remote --init --recursive
```

## How to clone a pipeline repo and include the updated submodule

```
git clone --recurse-submodules git@URL_OF_THE_PIPELINE_CHANGE_THIS
```

***

# Troubleshooting

If you get the following error:

```
Cloning into '/path/to/by/pipeline/bin/ll_pipeline_utils'...
git@gitlab.tuebingen.mpg.de: Permission denied (publickey).
fatal: Could not read from remote repository.
```

...then you probably need to add an ssh key to your [Github](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)/[GitLab](https://docs.gitlab.com/ee/ssh/) account.
Basically, you just need to paste in the public ssh key from your `~/.ssh/id_rsa.pub` file that is in your home directory.
If you do not have a `~/.ssh/id_rsa.pub` file, then you need to create one (see the docs above).

If you get an error like this:

```
Error: profile given but no config.yaml found. Profile has to be given as either absolute path, relative path or name of a directory available in either /etc/xdg/snakemake or /ebio/abt3/USERNAME/.config/snakemake.
```

...then make sure to update the submodule: `git submodule update --init --remote`
